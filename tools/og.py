"""Generate assets/img/og.png (1200x630) — requires Pillow. Uses a CJK font if available."""
import os
from PIL import Image, ImageDraw, ImageFont
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "img", "og.png")
W, H = 1200, 630
img = Image.new("RGB", (W, H)); d = ImageDraw.Draw(img)
for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(0x7E + 0x4A * t), int(0x0A + 6 * t), int(0x1C + 0x12 * t)))
d.rectangle([24, 24, W - 24, H - 24], outline="#F3D27A", width=3)
cands = ["/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc", "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
         "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
path = next((c for c in cands if os.path.exists(c)), None)
cjk = path and "CJK" in path
def F(s): return ImageFont.truetype(path, s) if path else ImageFont.load_default()
def c(text, font, y, fill):
    w = d.textlength(text, font=font); d.text(((W - w) / 2, y), text, font=font, fill=fill)
c("9999 10", F(190), 90, "#F3D27A")
c("久久久久 · 十全十美" if cjk else "Forever · Perfect", F(64), 330, "#FFFFFF")
c("Chinese Lucky Numbers · Dates · Zodiac · Tools", F(40), 440, "#FBE9D5")
c("999910.com", F(40), 510, "#F3D27A")
img.save(OUT, optimize=True)
print("og.png written")
