"""Standbild-Animator für Stoische Karriere (Pillow, NumPy, ffmpeg; deterministisch).

Macht aus Standbildern (zum Beispiel vier Startbilder für die Clips 46 bis 49) je einen
Clip von 8 bis 10 Sekunden im Kanallook. Bewegt werden Kamera und Licht, nicht die Figur:
  langsame Fahrt hinein oder heraus, Schwenk, wandernder Lichtkegel, Atmen des Lichts,
  feines Filmkorn. Figuren, Staub oder Sand bewegen sich NICHT. Dafür bleibt Flow
  („Frames to Video“) zuständig. Dieses Werkzeug ist die Lösung für Bilder, die nur
  ruhig „leben“ sollen, und für den Fall, dass Flow kein Guthaben oder Wasserzeichen hat.

Ausgabe je Bild (Kanalnorm M1): 1920×1080 (oder 1080×1920), 30 fps, H.264 9 Mbit/s,
Schlüsselbild alle 60 Bilder, stille AAC-Tonspur 160 kbit/s, 8 bis 10 Sekunden.
Dazu ein Prüfblatt (JPG) mit einem Stichbild je Sekunde für die Wasserzeichen-Prüfung (M3).

Aufruf (Beispiele):
  python standbild_animator.py bild46.png bild47.png bild48.png bild49.png -o render --start-nr 46
  python standbild_animator.py bild.png --bewegung schwenk_links --dauer 10 -o render
  python standbild_animator.py a.png b.png c.png d.png -o render --bewegung fahrt_rein,licht,schwenk_rechts,fahrt_raus
  python standbild_animator.py a.png b.png c.png d.png -o render --zusammen "Alle_vier.mp4"
  python standbild_animator.py a.png -o render --format 9x16 --vorschau

Bewegungen (--bewegung, eine für alle oder je Bild durch Komma getrennt):
  fahrt_rein      langsame Fahrt ins Bild (Dolly in)
  fahrt_raus      langsame Fahrt aus dem Bild
  schwenk_links   Kamera gleitet nach links, mit leichter Fahrt hinein
  schwenk_rechts  Kamera gleitet nach rechts, mit leichter Fahrt hinein
  licht           kaum Fahrt, ein weicher Lichtkegel wandert von links nach rechts
  auto            Standard: die vier Bewegungen fahrt_rein, schwenk_links, licht, fahrt_raus
                  im Wechsel, damit kein Clip wie der vorige aussieht.

Weitere Schalter:
  --dauer 8..10        Länge je Clip in Sekunden (Standard 9). Außerhalb 8 bis 10: Abbruch.
  --format 16x9|9x16   Standard 16x9.
  --fokus-x, --fokus-y Bildausschnitt 0 bis 1, wenn das Bild nicht 16:9 ist (Standard 0.5 / 0.45).
  --zoom 1.06..1.25    Stärke der Fahrt (Standard 1.12).
  --korn 0..10         Filmkorn (Standard 3, 0 = aus).
  --licht-tuerkis      Lichtkegel mit einem Hauch Türkis statt reinem Weiß.
  --ohne-grading       kein Grading (leichte Entsättigung, mildes Gamma, sanfte Vignette).
  --vorschau           schnelle Probe: 960×540, 15 fps, Dateiname mit _VORSCHAU.
  --zusammen NAME.mp4  zusätzlich alle Clips mit 0,8 s weicher Blende in einer Datei.
  --parallaxe          Figur und Hintergrund getrennt bewegen (zwei Ebenen, räumliche Tiefe).
                       Die Figur wird mit rembg freigestellt (pip install rembg, läuft auf der CPU,
                       lädt beim ersten Lauf ein Modell von rund 170 MB). Das Loch hinter der Figur
                       wird nur aus Hintergrundpixeln gefüllt, damit kein heller Saum entsteht.
                       Je Clip entsteht NAME_freistellung.png zur Kontrolle der Maske.
  --maske DATEI        eigene Maske statt rembg (weiß = Figur, schwarz = Hintergrund), je Bild
                       durch Komma getrennt, „-“ für rembg. Setzt --parallaxe voraus.
  --tiefe 0..0.9       wie viel weniger sich der Hintergrund bewegt (Standard 0.6: der Hintergrund
                       macht vierzig Prozent der Bewegung der Figur).
  --rembg-modell NAME  Standard u2net. Alternative isnet-general-use, wenn die Maske schlecht ist.
  --start-nr 46        Dateinamen Clip_46.mp4, Clip_47.mp4, ... (ohne: Name des Bildes).

Regeln, die das Skript erzwingt (Abbruch mit Exitcode 1): Dauer 8 bis 10 Sekunden, höchstens
fünf Bilder (Zusatzclips 46 bis 50), Bild lesbar. Ist ein Bild kleiner als die Ausgabe,
warnt es (Hochskalierung, Schärfe prüfen). Ein Bild in Ausgabegröße wird bei der engsten
Einstellung um den Zoomfaktor vergrößert (Standard zwölf Prozent), das ist normal. Wasserzeichen erkennt es nicht: dafür das
Prüfblatt ansehen (vier Ecken und Mitte je Sekunde).
Braucht Python 3 mit Pillow und NumPy sowie ffmpeg und ffprobe im Pfad; für --parallaxe rembg.
Die Freistellung muss ein Mensch prüfen (NAME_freistellung.png): Fehlt ein Stück der Figur oder
hängt Hintergrund an ihr, eigene Maske mit --maske geben oder ohne --parallaxe rendern.
"""
import argparse, json, math, shutil, subprocess, sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
SCHRIFT = ROOT / "outro" / "projekt" / "assets" / "fonts" / "BebasNeue-Regular.ttf"
WEISS, TUERKIS = (255, 255, 255), (0, 229, 255)
FORMATE = {"16x9": (1920, 1080), "9x16": (1080, 1920)}
BEWEGUNGEN = ["fahrt_rein", "fahrt_raus", "schwenk_links", "schwenk_rechts", "licht"]
AUTO_FOLGE = ["fahrt_rein", "schwenk_links", "licht", "fahrt_raus", "schwenk_rechts"]
FPS = 30
BLENDE = 0.8            # Sekunden weiche Blende zwischen Clips (M3)
MAX_BILDER = 5          # Zusatzclips 46 bis 50
SEED = 7                # festes Korn: gleiche Eingabe, gleiches Video


def fehler(msg):
    print("FEHLER:", msg)
    sys.exit(1)


def warnung(msg):
    print("WARNUNG:", msg)


# ---------------------------------------------------------------- Bildvorbereitung

def bild_laden(pfad):
    try:
        img = Image.open(pfad)
        img = ImageOps.exif_transpose(img)
    except Exception as e:
        fehler(f"{pfad}: Bild nicht lesbar ({e})")
    if img.mode in ("RGBA", "LA", "P"):
        # Transparenz auf Schwarz legen: der Kanalhintergrund ist schwarz
        rgba = img.convert("RGBA")
        grund = Image.new("RGBA", rgba.size, (0, 0, 0, 255))
        img = Image.alpha_composite(grund, rgba)
    return img.convert("RGB")


def grundbild(img, W, H, zoom_max, fokus_x, fokus_y, still=False):
    """Bild formatfüllend auf W*zoom_max × H*zoom_max bringen (Ausschnitt nach Fokus).

    Bei Zoom = zoom_max zeigt der Clip genau 1:1-Pixel dieser Fläche, bei Zoom = 1 die ganze
    Fläche verkleinert. So wird nie über die Vorlage hinaus vergrößert.
    Nur mit RGB- oder L-Bildern aufrufen: Pillow multipliziert beim Skalieren von RGBA mit dem
    Alphakanal vor, dadurch würde der ganze Hintergrund hinter einer Maske schwarz."""
    BW, BH = int(round(W * zoom_max)), int(round(H * zoom_max))
    bw, bh = img.size
    if (bw < W or bh < H) and not still:
        warnung(f"Bild {bw}×{bh} ist kleiner als die Ausgabe {W}×{H}. "
                f"Es wird deutlich hochskaliert, Schärfe im Prüfblatt kontrollieren.")
    skala = max(BW / bw, BH / bh)
    nw, nh = int(math.ceil(bw * skala)), int(math.ceil(bh * skala))
    img = img.resize((nw, nh), Image.LANCZOS)
    x0 = int(round((nw - BW) * min(max(fokus_x, 0.0), 1.0)))
    y0 = int(round((nh - BH) * min(max(fokus_y, 0.0), 1.0)))
    return img.crop((x0, y0, x0 + BW, y0 + BH))


def grading(arr):
    """Low-Key-Look, schattenschonend: Farben leicht zurück (Marmor bleibt neutral), Mitten
    über ein mildes Gamma etwas tiefer. Kein Schwarzpunkt, keine S-Kurve: Der Kanalhintergrund
    liegt bei rund zehn von 255, eine harte Kurve würde ihn zu reinem Schwarz machen."""
    a = arr / 255.0
    grau = a @ np.array([0.299, 0.587, 0.114], np.float32)
    a = a * 0.8 + grau[..., None] * 0.2            # Entsättigen um zwanzig Prozent
    a = np.clip(a, 0, 1) ** 1.06                    # Mitten leicht tiefer, Schatten bleiben
    return a * 255.0


def vignette(W, H):
    y, x = np.mgrid[0:H, 0:W].astype(np.float32)
    d = np.sqrt(((x - W / 2) / (W * 0.62)) ** 2 + ((y - H * 0.45) / (H * 0.78)) ** 2)
    # sanft: Mitte 1,0, Ecken rund 0,8. Die Bilder sind schon Low-Key, mehr nimmt Zeichnung weg.
    return np.clip(1.04 - d * 0.22, 0.78, 1.0)[..., None].astype(np.float32)


def lichtkoordinate(W, H):
    """Diagonale Koordinate 0..1 von links oben nach rechts unten, für den Lichtkegel."""
    y, x = np.mgrid[0:H, 0:W].astype(np.float32)
    u = (x / W) * 0.85 + (y / H) * 0.15
    return (u - u.min()) / (u.max() - u.min())


# ---------------------------------------------------------------- Parallaxe (zwei Ebenen)

_REMBG_SITZUNGEN = {}


def maske_erzeugen(img, maske_pfad, modell):
    """Liefert die Figur-Maske (L, 255 = Figur) in Bildgröße: eigene Datei oder rembg."""
    if maske_pfad and maske_pfad != "-":
        try:
            m = Image.open(maske_pfad).convert("L")
        except Exception as e:
            fehler(f"Maske {maske_pfad} nicht lesbar ({e})")
        if m.size != img.size:
            v1, v2 = m.size[0] / m.size[1], img.size[0] / img.size[1]
            if abs(v1 - v2) > 0.01:
                fehler(f"Maske {maske_pfad} hat ein anderes Seitenverhältnis als das Bild.")
            m = m.resize(img.size, Image.LANCZOS)
        return m
    try:
        from rembg import new_session, remove
    except ImportError:
        fehler("rembg fehlt. Installieren mit: pip install rembg   (oder eigene Maske mit --maske)")
    if modell not in _REMBG_SITZUNGEN:
        _REMBG_SITZUNGEN[modell] = new_session(modell)
    out = remove(img, session=_REMBG_SITZUNGEN[modell])
    alpha = out.split()[-1]
    anteil = np.asarray(alpha, np.float32).mean() / 255.0
    if anteil < 0.02 or anteil > 0.90:
        warnung(f"rembg hat {anteil * 100:.0f} Prozent des Bildes als Figur erkannt. "
                f"Maske in der Datei _freistellung.png prüfen, notfalls --maske oder --rembg-modell.")
    return alpha


def _kasten(a, r, achse):
    """Gleitender Mittelwert über 2r+1 Werte entlang einer Achse (Randwerte wiederholt)."""
    pad = [(0, 0)] * a.ndim
    pad[achse] = (r, r)
    c = np.cumsum(np.pad(a, pad, mode="edge"), axis=achse, dtype=np.float64)
    null = np.zeros_like(np.take(c, [0], axis=achse))
    c = np.concatenate([null, c], axis=achse)
    n = a.shape[achse]
    summe = np.take(c, range(2 * r + 1, 2 * r + 1 + n), axis=achse) - np.take(c, range(0, n), axis=achse)
    return (summe / (2 * r + 1)).astype(np.float32)


def _blur_f(arr2d, radius):
    """Weichzeichner für Fließkomma-Felder: dreifacher Kastenfilter, nahe an einer Gaußglocke."""
    a = arr2d
    for _ in range(3):
        a = _kasten(_kasten(a, radius, 0), radius, 1)
    return a


def hintergrund_fuellen(rgb, alpha):
    """Füllt das Loch hinter der Figur nur aus Hintergrundpixeln (normalisierte Faltung).

    Die Figurmaske wird erst erweitert, damit keine hellen Randpixel der Figur übrig bleiben.
    Dann werden Hintergrundfarben in mehreren Stufen von nah nach fern nach innen gezogen.
    So entsteht kein heller Saum, wie ihn ein Weichzeichnen des ganzen Bildes erzeugen würde."""
    h, w = alpha.shape
    rand = max(6, int(round(min(w, h) * 0.008)))
    erweitert = Image.fromarray((alpha * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(2 * rand + 1))
    erweitert = erweitert.filter(ImageFilter.GaussianBlur(2))
    loch = np.asarray(erweitert, np.float32) / 255.0          # 1 = muss gefüllt werden
    halt = 1.0 - loch                                        # Gewicht der echten Hintergrundpixel
    fuellung = np.zeros_like(rgb)
    gewicht = np.zeros((h, w), np.float32)
    for radius in (8, 32, 128, 400):
        den = _blur_f(halt, radius)
        offen = (gewicht < 0.5) & (den > 0.03)
        if not offen.any():
            break
        for k in range(3):
            num = _blur_f(rgb[:, :, k] * halt, radius)
            fuellung[:, :, k][offen] = (num / np.maximum(den, 1e-4))[offen]
        gewicht[offen] = 1.0
    # Rest (sehr große Löcher): mittlere Hintergrundfarbe
    rest = gewicht < 0.5
    if rest.any():
        mittel = (rgb * halt[..., None]).sum(axis=(0, 1)) / max(halt.sum(), 1.0)
        fuellung[rest] = mittel
    return rgb * halt[..., None] + fuellung * loch[..., None]


def freistellung_speichern(basis_rgb, alpha_weich, ziel):
    """Kontrollbild: Figur auf türkisem Grund, damit Fehler der Maske sofort auffallen."""
    fg = basis_rgb.copy()
    fg.putalpha(alpha_weich)
    grund = Image.new("RGBA", fg.size, TUERKIS + (255,))
    bild = Image.alpha_composite(grund, fg).convert("RGB")
    bild.thumbnail((1280, 1280), Image.LANCZOS)
    bild.save(ziel, quality=85)


# ---------------------------------------------------------------- Bewegung

def rampe(t, linear=0.35):
    """Weich an- und ausfahren, ohne je ganz zu stehen (kein Standbild, M3).

    Mischung aus geradem Lauf (Anteil 'linear') und weicher Kurve. Am Anfang und Ende
    läuft die Kamera mit rund einem Drittel der mittleren Geschwindigkeit weiter."""
    weich = t * t * (3 - 2 * t)
    return linear * t + (1 - linear) * weich


def kamera(bewegung, t, zoom_max, W, H, BW, BH):
    """Liefert den Bildausschnitt (x0, y0, x1, y1) in Koordinaten des Grundbilds."""
    p = min(max(rampe(t), 0.0), 1.0)         # 0..1 mit weichen Enden
    z_min, z_max = 1.0, zoom_max
    if bewegung == "fahrt_rein":
        z = z_min + (z_max - z_min) * p
        cx, cy = 0.5, 0.5
    elif bewegung == "fahrt_raus":
        z = z_max - (z_max - z_min) * p
        cx, cy = 0.5, 0.5
    elif bewegung in ("schwenk_links", "schwenk_rechts"):
        # leichte Fahrt hinein, dabei seitlich gleiten; Bewegungsraum hängt vom Zoom ab
        z = 1.0 + (z_max - 1.0) * (0.55 + 0.45 * p)
        spiel = (1 - 1 / z) / 2 * 0.9        # halbe freie Breite in Anteilen der Fläche
        richtung = -1 if bewegung == "schwenk_links" else 1
        cx = 0.5 + richtung * spiel * (2 * p - 1)
        cy = 0.5
    elif bewegung == "licht":
        z = 1.0 + (z_max - 1.0) * (0.35 + 0.30 * p)   # fast still, nur minimale Fahrt
        cx, cy = 0.5, 0.5
    else:
        fehler(f"unbekannte Bewegung {bewegung}")
    w, h = BW / z, BH / z
    x0 = cx * BW - w / 2
    y0 = cy * BH - h / 2
    x0 = min(max(x0, 0.0), BW - w)
    y0 = min(max(y0, 0.0), BH - h)
    return (x0, y0, x0 + w, y0 + h)


def licht_faktor(bewegung, t, u, tuerkis):
    """Multiplikator für das Licht: Atmen bei allen, wandernder Kegel bei 'licht'."""
    atmen = 1.0 + 0.03 * math.sin(2 * math.pi * t * 0.5 - math.pi / 2)   # eine Welle je 2 s
    if bewegung != "licht":
        return np.float32(atmen)
    pos = -0.25 + 1.5 * t                       # Kegel läuft von links außen nach rechts außen
    band = np.exp(-((u - pos) / 0.22) ** 2).astype(np.float32)
    staerke = 0.32
    if tuerkis:
        farbe = np.array([0.80, 1.00, 1.06], np.float32)   # Hauch Türkis #00E5FF
    else:
        farbe = np.array([1.0, 1.0, 1.0], np.float32)
    return (atmen * (1.0 + staerke * band[..., None] * farbe)).astype(np.float32)


# ---------------------------------------------------------------- Rendern

def ffmpeg_pruefen():
    for w in ("ffmpeg", "ffprobe"):
        if shutil.which(w) is None:
            fehler(f"{w} nicht gefunden. ffmpeg installieren und in den Pfad legen.")


def encoder_start(ziel, W, H, fps, bitrate):
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-",
           "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
           "-map", "0:v", "-map", "1:a", "-shortest",
           "-c:v", "libx264", "-preset", "slow", "-profile:v", "high", "-level", "4.2",
           "-b:v", bitrate, "-maxrate", bitrate, "-bufsize", "18M",
           "-g", "60", "-keyint_min", "60", "-sc_threshold", "0",
           "-pix_fmt", "yuv420p", "-r", str(fps), "-movflags", "+faststart",
           "-c:a", "aac", "-b:a", "160k", "-ar", "48000",
           str(ziel)]
    return subprocess.Popen(cmd, stdin=subprocess.PIPE)


def clip_rendern(bild_pfad, ziel, bewegung, dauer, W, H, fps, a, maske_pfad=None):
    img = bild_laden(bild_pfad)
    basis = grundbild(img, W, H, a.zoom, a.fokus_x, a.fokus_y)
    alpha = None
    if a.parallaxe:
        # Maske getrennt vom Bild skalieren (gleiche Parameter, gleicher Ausschnitt), nie als RGBA
        alpha = grundbild(maske_erzeugen(img, maske_pfad, a.rembg_modell), W, H, a.zoom, a.fokus_x, a.fokus_y, still=True)
    if not a.ohne_grading:
        # Farbkurve einmal auf das Grundbild, nicht je Einzelbild (sie hängt nur vom Pixel ab)
        basis = Image.fromarray(grading(np.asarray(basis, dtype=np.float32)).astype(np.uint8))
    BW, BH = basis.size
    basis_bg = basis_fg = None
    if a.parallaxe:
        alpha_f = np.asarray(alpha, np.float32) / 255.0
        basis_bg = Image.fromarray(np.clip(hintergrund_fuellen(np.asarray(basis, np.float32), alpha_f), 0, 255).astype(np.uint8))
        alpha_weich = alpha.filter(ImageFilter.GaussianBlur(1.5))
        basis_fg = basis.copy()
        basis_fg.putalpha(alpha_weich)
        freistellung_speichern(basis, alpha_weich, ziel.with_name(ziel.stem + "_freistellung.png"))
        zoom_bg = 1.0 + (a.zoom - 1.0) * (1.0 - a.tiefe)
    vig = vignette(W, H) if not a.ohne_grading else None
    u = lichtkoordinate(W, H) if bewegung == "licht" else None
    rng = np.random.default_rng(SEED)
    n = int(round(dauer * fps))
    bitrate = "9M" if not a.vorschau else "3M"
    enc = encoder_start(ziel, W, H, fps, bitrate)
    stichbilder = {}
    print(f"  {bewegung}, {dauer} s, {n} Bilder -> {ziel.name}")
    for i in range(n):
        t = i / max(n - 1, 1)
        box = kamera(bewegung, t, a.zoom, W, H, BW, BH)
        if a.parallaxe:
            # Figur folgt der vollen Kamerabewegung, der Hintergrund nur einem Teil davon
            box_bg = kamera(bewegung, t, zoom_bg, W, H, BW, BH)
            hinten = basis_bg.resize((W, H), Image.LANCZOS, box=box_bg, reducing_gap=None).convert("RGBA")
            vorne = basis_fg.resize((W, H), Image.LANCZOS, box=box, reducing_gap=None)
            frame = Image.alpha_composite(hinten, vorne).convert("RGB")
        else:
            frame = basis.resize((W, H), Image.LANCZOS, box=box, reducing_gap=None)
        arr = np.asarray(frame, dtype=np.float32)
        if not a.ohne_grading:
            arr = arr * vig
        arr = arr * licht_faktor(bewegung, t, u, a.licht_tuerkis)
        if a.korn > 0:
            # feines, deterministisches Korn; im Schwarz etwas schwächer, damit es nicht rauscht
            korn = rng.standard_normal((H, W), dtype=np.float32) * (a.korn * 0.9)
            gewicht = 0.35 + 0.65 * np.clip(arr[:, :, 1] / 255.0, 0, 1)
            arr = arr + (korn * gewicht)[..., None]
        out = np.clip(arr, 0, 255).astype(np.uint8)
        enc.stdin.write(out.tobytes())
        if i % fps == 0 or i == n - 1:
            stichbilder[round(i / fps, 1)] = Image.fromarray(out)
    enc.stdin.close()
    if enc.wait() != 0:
        fehler(f"ffmpeg meldet Fehler beim Schreiben von {ziel}")
    return stichbilder


# ---------------------------------------------------------------- Prüfung

def ffprobe(pfad):
    cmd = ["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", str(pfad)]
    info = json.loads(subprocess.run(cmd, capture_output=True, text=True, check=True).stdout)
    v = next(s for s in info["streams"] if s["codec_type"] == "video")
    a_ = [s for s in info["streams"] if s["codec_type"] == "audio"]
    num, den = v["r_frame_rate"].split("/")
    fps = float(num) / float(den)
    dauer = float(info["format"]["duration"])
    kbit = int(info["format"]["bit_rate"]) / 1000
    ton = f"{a_[0]['codec_name']} {int(a_[0].get('bit_rate', 0)) // 1000} kbit/s" if a_ else "KEINE TONSPUR"
    return v["width"], v["height"], fps, dauer, kbit, ton, v["codec_name"]


def pruefblatt(stichbilder, ziel, titel, W, H):
    """Ein Stichbild je Sekunde als Übersicht. Ecken und Mitte auf Wasserzeichen prüfen (M3)."""
    zeiten = sorted(stichbilder)
    tw = 640 if W >= H else 360
    th = int(round(tw * H / W))
    spalten = 4 if W >= H else 6
    reihen = math.ceil(len(zeiten) / spalten)
    rand, kopf = 16, 70
    blatt = Image.new("RGB", (spalten * (tw + rand) + rand, kopf + reihen * (th + rand + 28) + rand), (8, 10, 11))
    d = ImageDraw.Draw(blatt)
    try:
        f_gross = ImageFont.truetype(str(SCHRIFT), 40)
        f_klein = ImageFont.truetype(str(SCHRIFT), 26)
    except OSError:
        f_gross = f_klein = ImageFont.load_default()
    d.text((rand, 14), titel.upper(), fill=TUERKIS, font=f_gross)
    for k, z in enumerate(zeiten):
        x = rand + (k % spalten) * (tw + rand)
        y = kopf + (k // spalten) * (th + rand + 28)
        blatt.paste(stichbilder[z].resize((tw, th), Image.LANCZOS), (x, y))
        d.rectangle((x, y, x + tw - 1, y + th - 1), outline=(40, 44, 46))
        d.text((x, y + th + 2), f"{z:.1f} S", fill=WEISS, font=f_klein)
    blatt.save(ziel, quality=88)


def zusammenfuegen(clips, ziel, fps, dauer):
    """Alle Clips mit 0,8 s weicher Blende hintereinander (xfade), Ton still."""
    if len(clips) == 1:
        shutil.copy(clips[0], ziel)
        return
    eing = []
    for c in clips:
        eing += ["-i", str(c)]
    filt, vorher, offset = [], "[0:v]", 0.0
    for k in range(1, len(clips)):
        offset += dauer - BLENDE
        aus = f"[v{k}]" if k < len(clips) - 1 else "[vout]"
        filt.append(f"{vorher}[{k}:v]xfade=transition=fade:duration={BLENDE}:offset={offset:.3f}{aus}")
        vorher = aus
    gesamt = len(clips) * dauer - (len(clips) - 1) * BLENDE
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *eing,
           "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
           "-filter_complex", ";".join(filt), "-map", "[vout]", "-map", f"{len(clips)}:a",
           "-t", f"{gesamt:.3f}",
           "-c:v", "libx264", "-preset", "slow", "-b:v", "9M", "-maxrate", "9M", "-bufsize", "18M",
           "-g", "60", "-keyint_min", "60", "-sc_threshold", "0", "-pix_fmt", "yuv420p", "-r", str(fps),
           "-movflags", "+faststart", "-c:a", "aac", "-b:a", "160k", str(ziel)]
    if subprocess.run(cmd).returncode != 0:
        fehler(f"ffmpeg meldet Fehler beim Zusammenfügen nach {ziel}")


# ---------------------------------------------------------------- Hauptprogramm

def main():
    p = argparse.ArgumentParser(description="Standbilder zu 8 bis 10 s Clips im Kanallook animieren.",
                                formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    p.add_argument("bilder", nargs="+", help="1 bis 5 Standbilder (PNG oder JPG)")
    p.add_argument("-o", "--ausgabe", default="render", help="Zielordner (Standard: render)")
    p.add_argument("--dauer", type=float, default=9.0, help="Sekunden je Clip, 8 bis 10 (Standard 9)")
    p.add_argument("--bewegung", default="auto", help="auto oder " + ", ".join(BEWEGUNGEN) + " (je Bild durch Komma)")
    p.add_argument("--format", choices=FORMATE, default="16x9")
    p.add_argument("--zoom", type=float, default=1.12, help="Stärke der Fahrt 1.06 bis 1.25 (Standard 1.12)")
    p.add_argument("--fokus-x", type=float, default=0.5)
    p.add_argument("--fokus-y", type=float, default=0.45)
    p.add_argument("--korn", type=float, default=3.0, help="Filmkorn 0 bis 10 (Standard 3)")
    p.add_argument("--licht-tuerkis", action="store_true")
    p.add_argument("--ohne-grading", action="store_true")
    p.add_argument("--vorschau", action="store_true", help="960×540, 15 fps, schnelle Probe")
    p.add_argument("--zusammen", metavar="NAME.mp4", help="alle Clips mit 0,8 s Blende in einer Datei")
    p.add_argument("--start-nr", type=int, help="Dateinamen Clip_NN.mp4 ab dieser Nummer, z. B. 46")
    p.add_argument("--parallaxe", action="store_true", help="Figur und Hintergrund getrennt bewegen (rembg)")
    p.add_argument("--maske", help="eigene Masken statt rembg, je Bild durch Komma, - für rembg")
    p.add_argument("--tiefe", type=float, default=0.6, help="Anteil, um den der Hintergrund weniger mitgeht, 0 bis 0.9")
    p.add_argument("--rembg-modell", default="u2net", help="rembg-Modell (Standard u2net)")
    a = p.parse_args()

    ffmpeg_pruefen()
    if not (8.0 <= a.dauer <= 10.0):
        fehler(f"Dauer {a.dauer} s liegt nicht zwischen 8 und 10 Sekunden (M3, Zusatzclips).")
    if not (1.06 <= a.zoom <= 1.25):
        fehler("Zoom muss zwischen 1.06 und 1.25 liegen.")
    if not (0 <= a.korn <= 10):
        fehler("Korn muss zwischen 0 und 10 liegen.")
    if a.maske and not a.parallaxe:
        fehler("--maske setzt --parallaxe voraus.")
    if not (0.0 <= a.tiefe <= 0.9):
        fehler("--tiefe muss zwischen 0 und 0.9 liegen.")
    masken = [None] * len(a.bilder)
    if a.maske:
        masken = a.maske.split(",")
        if len(masken) != len(a.bilder):
            fehler(f"{len(masken)} Masken für {len(a.bilder)} Bilder angegeben.")
        for m in masken:
            if m != "-" and not Path(m).is_file():
                fehler(f"Maske nicht gefunden: {m}")
    if len(a.bilder) > MAX_BILDER:
        fehler(f"Höchstens {MAX_BILDER} Bilder je Aufruf (Zusatzclips 46 bis 50), es sind {len(a.bilder)}.")
    for b in a.bilder:
        if not Path(b).is_file():
            fehler(f"Bild nicht gefunden: {b}")

    bewegungen = a.bewegung.split(",") if a.bewegung != "auto" else [AUTO_FOLGE[i % len(AUTO_FOLGE)] for i in range(len(a.bilder))]
    if len(bewegungen) == 1 and len(a.bilder) > 1:
        bewegungen = bewegungen * len(a.bilder)
    if len(bewegungen) != len(a.bilder):
        fehler(f"{len(bewegungen)} Bewegungen für {len(a.bilder)} Bilder angegeben.")
    for bw in bewegungen:
        if bw not in BEWEGUNGEN:
            fehler(f"unbekannte Bewegung '{bw}'. Erlaubt: {', '.join(BEWEGUNGEN)}")
    if len(set(bewegungen)) < len(bewegungen):
        warnung("Mehrere Clips haben dieselbe Bewegung. Erlaubt, aber im Video sehen sie sich ähnlich.")

    W, H = FORMATE[a.format]
    fps = FPS
    if a.vorschau:
        W, H, fps = W // 2, H // 2, 15
    aus = Path(a.ausgabe)
    aus.mkdir(parents=True, exist_ok=True)

    fertige = []
    print(f"Ausgabe {W}×{H}, {fps} fps, {len(a.bilder)} Clip(s) à {a.dauer:g} s nach {aus}/"
          + (f", Parallaxe (Tiefe {a.tiefe:g})" if a.parallaxe else ""))
    for k, (bild, bw) in enumerate(zip(a.bilder, bewegungen)):
        name = f"Clip_{a.start_nr + k}" if a.start_nr is not None else Path(bild).stem
        if a.vorschau:
            name += "_VORSCHAU"
        ziel = aus / f"{name}.mp4"
        print(f"[{k + 1}/{len(a.bilder)}] {bild}")
        stich = clip_rendern(bild, ziel, bw, a.dauer, W, H, fps, a, masken[k])
        pruefblatt(stich, aus / f"{name}_pruefblatt.jpg", f"{name}  ·  {bw}  ·  Stichbilder je Sekunde", W, H)
        w, h, f, d, kbit, ton, codec = ffprobe(ziel)
        ok = (w, h) == (W, H) and abs(f - fps) < 0.01 and abs(d - a.dauer) < 0.15 and codec == "h264"
        print(f"  geprüft: {w}×{h}, {f:g} fps, {d:.2f} s, {kbit:.0f} kbit/s gesamt, {codec}, Ton {ton}"
              + ("" if ok else "  <- ABWEICHUNG"))
        fertige.append(ziel)

    if a.zusammen:
        ziel = aus / a.zusammen
        print(f"Zusammenfügen mit {BLENDE} s Blende -> {ziel}")
        zusammenfuegen(fertige, ziel, fps, a.dauer)
        w, h, f, d, kbit, ton, codec = ffprobe(ziel)
        print(f"  geprüft: {w}×{h}, {f:g} fps, {d:.2f} s, {kbit:.0f} kbit/s, Ton {ton}")

    print("Fertig. Vor dem Einbau: Prüfblatt ansehen (vier Ecken und Mitte je Sekunde, Wasserzeichen, Schärfe).")


if __name__ == "__main__":
    main()
