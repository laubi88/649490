import sys, numpy as np
from PIL import Image
W, H = int(sys.argv[2]), int(sys.argv[3])
rng = np.random.default_rng(7)
def noise(scale):
    gh, gw = H//scale+2, W//scale+2
    g = rng.random((gh, gw))
    img = Image.fromarray((g*255).astype(np.uint8)).resize((gw*scale, gh*scale), Image.BICUBIC)
    return np.asarray(img).astype(float)[:H,:W]/255
fbm = sum(noise(s)*w for s,w in [(320,.5),(160,.25),(80,.13),(40,.07),(20,.05)])
y, x = np.mgrid[0:H, 0:W].astype(float)
veins = np.abs(np.sin((x*0.0026 + y*0.0041) * np.pi * 3 + fbm*9.0))
veins = (1 - veins) ** 18          # thin bright veins
veins2 = (1 - np.abs(np.sin((x*-0.0018 + y*0.0030)*np.pi*2 + fbm*7.0))) ** 30
base = np.array([0x13,0x17,0x19], float)
dark = np.array([0x08,0x0A,0x0B], float)
t = np.clip((fbm-0.3)*1.6, 0, 1)[...,None]
img = dark*(1-t) + base*t
vein_col = np.array([0x9A,0xB5,0xB1], float)
img = img + (vein_col-img)*(veins*0.06 + veins2*0.04)[...,None]
# vignette
cx, cy = W/2, H*0.42
d = np.sqrt(((x-cx)/(W*0.62))**2 + ((y-cy)/(H*0.75))**2)
img *= np.clip(1.15 - d*0.75, 0.35, 1.05)[...,None]
Image.fromarray(np.clip(img,0,255).astype(np.uint8)).save(sys.argv[1], quality=94)
print("ok")
