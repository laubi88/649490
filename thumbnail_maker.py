"""Thumbnail-Generator für Stoische Karriere (Pillow, deterministisch).

Erzeugt ein 1920x1080-JPG (unter 2 MB) im Kanal-Look:
  dunkler Carrara-Marmor im Low-Key-Licht, Schattenverlauf links,
  Marmorbüste rechts, Text links: Zeile 1 Türkis #00E5FF (klein), Zeile 2 Weiß #FFFFFF (groß).

Aufruf (Beispiele):
  python thumbnail_maker.py --zeile1 "WAS ER" --zeile2 "VERSCHWEIGT" --bild buese.png -o "V15 Was ein Mann für sich behält THUMBNAIL.jpg"
  python thumbnail_maker.py --zeile1 "NIE MEHR" --zeile2 "KLEIN BEIGEBEN" --bild standbild.jpg --fokus 0.8 -o test.jpg

--bild  PNG mit Transparenz (freigestellte Büste)  -> wird rechts auf den Marmor gesetzt.
        JPG/PNG ohne Transparenz (Standbild 16:9)   -> füllt das Bild, Ausschnitt per --fokus.
        ohne --bild                                 -> nur Marmor (Probeansicht für den Text).

Regeln, die das Skript erzwingt (Abbruch mit Exitcode 1): zwei bis vier Wörter gesamt,
keine Ziffern, keine Bindestriche. Englische Wörter kann es nicht sicher erkennen: selbst prüfen.
Schrift: Anton (schriften/Anton-Regular.ttf, SIL Open Font License 1.1, Lizenz in schriften/OFL.txt).
Fehlt die Datei, nimmt das Skript Bebas Neue als Ersatz und meldet das.
"""
import argparse, re, subprocess, sys, tempfile
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps

W, H = 1920, 1080
WEISS, TUERKIS, SCHWARZ = (255, 255, 255), (0, 229, 255), (0, 0, 0)
ROOT = Path(__file__).resolve().parent
MARMOR_SKRIPT = ROOT / "outro" / "werkzeuge" / "marmor.py"
SCHRIFTEN = [ROOT / "schriften" / "Anton-Regular.ttf",
             ROOT / "outro" / "projekt" / "assets" / "fonts" / "BebasNeue-Regular.ttf"]
RAND_LINKS = 96            # Abstand Text zum linken Rand
TEXT_MAX_BREITE = 0.52     # Text bleibt in der linken Hälfte, die Büste rechts frei
MAX_BYTES = 2 * 1024 * 1024  # 2 MB, Grenze für Upload vom Handy


def fehler(msg):
    print("FEHLER:", msg); sys.exit(1)


def text_pruefen(z1, z2):
    woerter = (z1 + " " + z2).split()
    if not z1.strip() or not z2.strip():
        fehler("beide Zeilen brauchen Text")
    if not 2 <= len(woerter) <= 4:
        fehler(f"{len(woerter)} Wörter, erlaubt sind zwei bis vier")
    if re.search(r"\d", z1 + z2):
        fehler("Ziffern sind im Thumbnail-Text verboten, Zahlen ausschreiben")
    if re.search(r"[-–—]", z1 + z2):
        fehler("keine Bindestriche im Thumbnail-Text")
    return z1.strip().upper(), z2.strip().upper()


def marmor():
    """Dunkler Marmor über das Kanal-Skript, damit Hintergründe überall gleich aussehen."""
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "marmor.jpg"
        subprocess.run([sys.executable, str(MARMOR_SKRIPT), str(p), str(W), str(H)],
                       check=True, capture_output=True)
        return Image.open(p).convert("RGBA")


def low_key(im, staerke=0.85):
    """Mitten absenken, Lichter behalten: Low-Key-Look ohne Farbstich."""
    lut = [round(255 * (i / 255) ** (1 / staerke)) for i in range(256)]
    r, g, b, a = im.split()
    return Image.merge("RGBA", (r.point(lut), g.point(lut), b.point(lut), a))


def bild_einsetzen(grund, pfad, fokus):
    bild = Image.open(pfad)
    bild = ImageOps.exif_transpose(bild).convert("RGBA")
    freigestellt = bild.getextrema()[3][0] < 250
    if freigestellt:  # Büste rechts, volle Höhe, unten bündig
        f = H / bild.height
        b = bild.resize((max(1, round(bild.width * f)), H), Image.LANCZOS)
        x = W - b.width + round(b.width * 0.08)  # leicht angeschnitten, wirkt näher
        x = max(x, round(W * 0.42))
        grund.alpha_composite(low_key(b), (x, 0))
        return grund
    # Standbild füllt die Fläche, horizontaler Ausschnitt nach --fokus
    f = max(W / bild.width, H / bild.height)
    b = bild.resize((round(bild.width * f), round(bild.height * f)), Image.LANCZOS)
    links = round((b.width - W) * fokus); oben = (b.height - H) // 2
    return low_key(b.crop((links, oben, links + W, oben + H)))


def schatten_links(im):
    """Dunkler Verlauf von links (fast schwarz) bis rund 62 Prozent der Breite."""
    maske = Image.new("L", (W, 1))
    ende = W * 0.62
    for x in range(W):
        t = min(x / ende, 1.0)
        t = t * t * (3 - 2 * t)  # weicher Übergang
        maske.putpixel((x, 0), round(240 * (1 - t)))
    maske = maske.resize((W, H))
    # unten zusätzlich leicht abdunkeln, damit die Videolänge-Ecke ruhig bleibt
    unten = Image.linear_gradient("L").resize((W, H)).point(lambda v: round(max(0, v - 150) * 0.9))
    maske = ImageChops.lighter(maske, unten)
    schwarz = Image.new("RGBA", (W, H), SCHWARZ + (255,))
    schwarz.putalpha(maske)
    im.alpha_composite(schwarz)
    return im


def schrift_laden(pfad):
    kandidaten = [Path(pfad)] if pfad else SCHRIFTEN
    for k in kandidaten:
        if k.is_file():
            if "Anton" not in k.name:
                print(f"Hinweis: Schrift {k.name} (Ersatz). Standard ist schriften/Anton-Regular.ttf.")
            return str(k)
    fehler("keine Schrift gefunden, --schrift angeben")


def text_setzen(im, z1, z2, schrift):
    max_breite = W * TEXT_MAX_BREITE
    g2 = 330  # Startgröße Zeile 2, wird bei Bedarf verkleinert
    while True:
        g1 = round(g2 * 0.62)
        f1, f2 = ImageFont.truetype(schrift, g1), ImageFont.truetype(schrift, g2)
        if max(f1.getlength(z1), f2.getlength(z2)) <= max_breite or g2 <= 135:
            break
        g2 -= 4
    # Höhe über die echten Buchstaben-Kästen (Großbuchstaben, keine Unterlängen)
    b1, b2 = f1.getbbox(z1, anchor="ls"), f2.getbbox(z2, anchor="ls")
    h1, h2 = -b1[1], -b2[1]
    abstand = round(g2 * 0.10)
    block = h1 + abstand + h2
    oben = round(H * 0.46 - block / 2)
    y1, y2 = oben + h1, oben + h1 + abstand + h2

    ebene = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ebene)
    for txt, f, y, farbe, g in ((z1, f1, y1, TUERKIS, g1), (z2, f2, y2, WEISS, g2)):
        d.text((RAND_LINKS, y), txt, font=f, fill=farbe + (255,), anchor="ls",
               stroke_width=max(2, round(g * 0.035)), stroke_fill=SCHWARZ + (255,))
    # weicher Schatten: Textmaske verschoben und weichgezeichnet
    schatten = Image.new("RGBA", (W, H), SCHWARZ + (0,))
    schatten.putalpha(ebene.getchannel("A").point(lambda a: round(a * 0.85)))
    schatten = schatten.transform((W, H), Image.AFFINE, (1, 0, -9, 0, 1, -12)).filter(ImageFilter.GaussianBlur(21))
    im.alpha_composite(schatten)
    im.alpha_composite(ebene)
    return block, g1, g2


def speichern(im, ziel):
    rgb = im.convert("RGB")
    for q in (95, 92, 88, 84, 80):
        rgb.save(ziel, "JPEG", quality=q, optimize=True, progressive=True, subsampling=0)
        if ziel.stat().st_size <= MAX_BYTES:
            return q
    fehler(f"{ziel.name} bleibt über 2 MB")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--zeile1", required=True, help="Zeile 1, Türkis #00E5FF, kleiner")
    ap.add_argument("--zeile2", required=True, help="Zeile 2, Weiß #FFFFFF, groß")
    ap.add_argument("--bild", help="Büste (PNG mit Transparenz) oder Standbild")
    ap.add_argument("--fokus", type=float, default=0.75, help="Ausschnitt bei Standbildern, 0 links bis 1 rechts")
    ap.add_argument("--schrift", help="Pfad zur TTF, Standard schriften/Anton-Regular.ttf")
    ap.add_argument("-o", "--ausgabe", default="thumbnail.jpg")
    a = ap.parse_args()

    z1, z2 = text_pruefen(a.zeile1, a.zeile2)
    ziel = Path(a.ausgabe)
    ziel.parent.mkdir(parents=True, exist_ok=True)

    im = marmor()
    if a.bild:
        im = bild_einsetzen(im, a.bild, min(max(a.fokus, 0.0), 1.0))
    else:
        print("Hinweis: ohne --bild fehlt die Marmorbüste rechts. Nur als Textprobe verwenden.")
    im = schatten_links(im)
    block, g1, g2 = text_setzen(im, z1, z2, schrift_laden(a.schrift))
    q = speichern(im, ziel)

    vorschau = ziel.with_name(ziel.stem + "_vorschau_168px.png")
    im.convert("RGB").resize((168, 95), Image.LANCZOS).save(vorschau)

    anteil = block / H * 100
    print(f"OK {ziel} {W}x{H}, JPG Qualität {q}, {ziel.stat().st_size / 1024:.0f} KB")
    print(f"Text: '{z1}' türkis {g1} px / '{z2}' weiß {g2} px, Textblock {anteil:.0f} % der Bildhöhe")
    if anteil < 20:
        print("WARNUNG: Textblock unter 20 % der Bildhöhe, Wörter kürzen")
    print(f"Lesbarkeit prüfen: {vorschau}")


if __name__ == "__main__":
    main()
