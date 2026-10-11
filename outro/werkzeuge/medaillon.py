import sys, numpy as np
from PIL import Image, ImageDraw, ImageFilter
src, out_tq, out_bz = sys.argv[1], sys.argv[2], sys.argv[3]
im = Image.open(src).convert("RGB")
cx, cy, r = 964, 550, 511
box = (cx-r-4, cy-r-4, cx+r+4, cy+r+4)
crop = im.crop(box)
S = crop.size[0]
# feathered circular alpha
mask = Image.new("L", (S*4, S*4), 0)
ImageDraw.Draw(mask).ellipse((16, 16, S*4-17, S*4-17), fill=255)
mask = mask.resize((S, S), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.2))
a = np.asarray(crop).astype(float)/255
lum = 0.2126*a[...,0] + 0.7152*a[...,1] + 0.0722*a[...,2]
lum = np.clip((lum - 0.02) / 0.80, 0, 1) ** 0.85
# gradient map: near-black teal -> deep teal -> turquoise -> pale highlight
stops = np.array([0.0, 0.30, 0.65, 1.0])
cols = np.array([[0x02,0x0A,0x0C],[0x00,0x3E,0x46],[0x00,0xE5,0xFF],[0xE8,0xFD,0xFF]], float)/255
tq = np.stack([np.interp(lum, stops, cols[:,c]) for c in range(3)], -1)
# keep 12 % of original colour for metal texture
tq = 0.88*tq + 0.12*a
out = np.dstack([np.clip(tq,0,1)*255, np.asarray(mask)]).astype(np.uint8)
Image.fromarray(out, "RGBA").resize((720,720), Image.LANCZOS).save(out_tq, optimize=True)
bz = np.dstack([a*255, np.asarray(mask)]).astype(np.uint8)
Image.fromarray(bz, "RGBA").resize((720,720), Image.LANCZOS).save(out_bz, optimize=True)
print("ok", crop.size)
