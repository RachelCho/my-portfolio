"""Second Context 파비콘·Open Graph 이미지(2026-11-10): 검정 바탕 + 흰 두 사각 프레임 심볼(워드마크 없음).
승인 로고 흰색판(assets/second-context-logo-white.png)에서 심볼만 잘라 쓴다.
사용: python3 tools/make_brand_icons.py .
 - favicon.ico(16·32·48) · assets/favicon-32.png
 - assets/og/<home|approach|work|contact>-<ko|en>.png (1200×630, 페이지 문구 없음)
포트폴리오(index.html)의 assets/og/portfolio.png는 건드리지 않는다. tools/make_og_images.py는 Second Context에 다시 쓰지 않는다."""
import os, sys
from PIL import Image

R = sys.argv[1]
logo = Image.open(os.path.join(R, 'assets/second-context-logo-white.png')).convert('RGBA')
sym = logo.crop((0, 0, 340, 326))  # 심볼과 워드마크 사이 빈 열(339~361px) 왼쪽
sym = sym.crop(sym.getchannel('A').getbbox())


def place(W, H, frac):
    c = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    w = round(W * frac); h = round(sym.height * w / sym.width)
    if h > H * frac:
        h = round(H * frac); w = round(sym.width * h / sym.height)
    c.alpha_composite(sym.resize((w, h), Image.LANCZOS), ((W - w) // 2, (H - h) // 2))
    return c.convert('RGB')


big = place(512, 512, .82)  # 작은 크기에서 선이 뭉개지지 않게 큰 판에서 줄인다
big.resize((32, 32), Image.LANCZOS).save(os.path.join(R, 'assets/favicon-32.png'))
big.save(os.path.join(R, 'favicon.ico'), sizes=[(16, 16), (32, 32), (48, 48)])
og = place(1200, 630, .30)
for n in ('home', 'approach', 'work', 'contact'):
    for l in ('ko', 'en'):
        og.save(os.path.join(R, f'assets/og/{n}-{l}.png'))
print('favicon + og done')
