"""Erzeugt Profilbild und Kanalbanner für Stoische Karriere (PIL, deterministisch).
Aufruf: python branding.py <projekt_assets_dir> <ausgabe_dir>"""
import sys, subprocess, numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ASSETS, OUT = Path(sys.argv[1]), Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)
FONT = str(ASSETS / "fonts" / "BebasNeue-Regular.ttf")
WEISS, TUERKIS = (255, 255, 255), (0, 229, 255)
MED = Image.open(ASSETS / "img" / "medaillon_tuerkis.png").convert("RGBA")
MARMOR = Path(__file__).with_name("marmor.py")

def marmor(w, h):
    p = OUT / f"_marmor_{w}x{h}.jpg"
    subprocess.run([sys.executable, str(MARMOR), str(p), str(w), str(h)], check=True, capture_output=True)
    im = Image.open(p).convert("RGBA"); p.unlink(); return im

def text_spaced(img, xy, text, size, fill, tracking=0.0, anchor="l", glow=None):
    """Schreibt Text mit Laufweite (tracking in em). anchor l/m = links/mittig, y = Grundlinie."""
    f = ImageFont.truetype(FONT, size)
    sp = tracking * size
    widths = [f.getlength(c) for c in text]
    total = sum(widths) + sp * (len(text) - 1)
    x, y = xy
    if anchor == "m": x -= total / 2
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    cx = x
    for c, w in zip(text, widths):
        d.text((cx, y), c, font=f, fill=fill + (255,), anchor="ls"); cx += w + sp
    if glow:
        g = layer.filter(ImageFilter.GaussianBlur(glow[0]))
        a = np.asarray(g).astype(float); a[..., 3] *= glow[1]
        img.alpha_composite(Image.fromarray(a.astype(np.uint8), "RGBA"))
    img.alpha_composite(layer)
    return total

def medaillon(img, cx, cy, d, rim=True):
    m = MED.resize((d, d), Image.LANCZOS)
    if rim:  # weiches türkises Leuchten hinter dem Medaillon
        halo = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ImageDraw.Draw(halo).ellipse((cx - d/2 - 6, cy - d/2 - 6, cx + d/2 + 6, cy + d/2 + 6), fill=TUERKIS + (90,))
        img.alpha_composite(halo.filter(ImageFilter.GaussianBlur(d * 0.06)))
    img.alpha_composite(m, (int(cx - d/2), int(cy - d/2)))

# ---------- Profilbild 800x800 ----------
def profil(name, zoom=1.0, center=(0.5, 0.5)):
    S = 800
    bg = marmor(S, S)
    big = MED.resize((int(720 * zoom * S / 720 * 0.94), ) * 2, Image.LANCZOS)
    bw = big.size[0]
    ox = int(S / 2 - center[0] * bw); oy = int(S / 2 - center[1] * bw)
    if zoom == 1.0:
        medaillon(bg, S / 2, S / 2, int(S * 0.94))
    else:
        bg.alpha_composite(big, (ox, oy))
    out = bg.convert("RGB")
    out.save(OUT / f"{name}.png", optimize=True)
    return out

pA = profil("profilbild_A_medaillon")
pB = profil("profilbild_B_ausschnitt", zoom=1.75, center=(0.50, 0.40))

# Vorschau: Kreis in 98, 48, 32 px auf hellem und dunklem Grund
def kreis(im, s):
    m = Image.new("L", (s * 4, s * 4), 0); ImageDraw.Draw(m).ellipse((0, 0, s * 4 - 1, s * 4 - 1), fill=255)
    m = m.resize((s, s), Image.LANCZOS)
    t = im.resize((s, s), Image.LANCZOS).convert("RGBA"); t.putalpha(m); return t
sheet = Image.new("RGBA", (800, 420), (255, 255, 255, 255))
ImageDraw.Draw(sheet).rectangle((0, 210, 800, 420), fill=(15, 15, 15, 255))
for row, im in enumerate([pA, pB]):
    for band, y0 in enumerate((0, 210)):
        x = 20 + row * 390
        for s in (160, 98, 48, 32):
            sheet.alpha_composite(kreis(im, s), (x, y0 + 25 + (160 - s) // 2))
            x += s + 14
sheet.convert("RGB").save(OUT / "vorschau_profilbild_klein.png")

# ---------- Banner 2560x1440 ----------
W, H = 2560, 1440
SAFE = (W / 2 - 1546 / 2, H / 2 - 423 / 2, W / 2 + 1546 / 2, H / 2 + 423 / 2)  # = 1235x338 bei 2048x1152
b = marmor(W, H)
# Medaillon links im sicheren Bereich, Text rechts daneben
md = 330
gap = 56
t1, t2, t3 = "STOISCHE KARRIERE", "STOIZISMUS UND PSYCHOLOGIE", "FÜR MÄNNER IM BERUF UND ZU HAUSE"
f1, f2, f3 = 165, 66, 52
w1 = sum(ImageFont.truetype(FONT, f1).getlength(c) for c in t1) + 0.04 * f1 * (len(t1) - 1)
block = md + gap + w1
x0 = W / 2 - block / 2
cy = H / 2
medaillon(b, x0 + md / 2, cy, md)
tx = x0 + md + gap
text_spaced(b, (tx, cy - 20), t1, f1, WEISS, 0.04, glow=(14, 0.25))
d = ImageDraw.Draw(b); d.rectangle((tx, cy + 6, tx + w1, cy + 9), fill=TUERKIS + (255,))
text_spaced(b, (tx, cy + 88), t2, f2, TUERKIS, 0.06)
text_spaced(b, (tx, cy + 152), t3, f3, (235, 240, 240), 0.06)
banner = b.convert("RGB")
banner.save(OUT / "banner_2560x1440.jpg", quality=92, optimize=True)

# Kontrollbild: sichere Fläche (Handy) und Tablet-/Desktop-Bereich einzeichnen
k = banner.copy(); kd = ImageDraw.Draw(k)
kd.rectangle(SAFE, outline=(255, 60, 60), width=6)
kd.rectangle((0, H / 2 - 423 / 2, W, H / 2 + 423 / 2), outline=(255, 200, 0), width=4)
k.resize((1280, 720), Image.LANCZOS).save(OUT / "vorschau_banner_sichere_flaeche.jpg", quality=88)
print("ok", (OUT / "banner_2560x1440.jpg").stat().st_size, "Bytes; Textblock", int(block), "px breit; sicher", int(SAFE[2] - SAFE[0]))
