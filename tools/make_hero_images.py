"""홈 Hero 사진 만들기 (2026-11-05 교체)
대표 이미지: assets/Product designer leading a studio critique.png (1774×887)
— 복잡한 제품 화면(대형 화면·노트북의 대시보드)을 바탕으로 팀의 디자인 논의를 이끄는 Rachel.
Rachel은 오른쪽(얼굴 중심 가로 75%·세로 30%), 설명하는 손은 가로 66%·세로 68%.

- 데스크톱(901px~): home-hero-rachel-design-review-<폭>.jpg (원본 2:1 그대로 축소, 크롭·합성 없음)
  CSS object-position 75% 30%로 화면 비율이 바뀌어도 얼굴이 오른쪽 ¾ 지점에 머문다.
- 태블릿·모바일(~900px): home-hero-rachel-design-review-mobile-<폭>.jpg (4:3, 원본 오른쪽을 잘라 얼굴·손·노트북이 함께 보이게)
얼굴·피부·대시보드는 보정하지 않는다(밝기·채도·선명도 편집 없음). 원본보다 크게 늘리지 않는다.
한국어·영어 홈은 같은 파일을 쓴다.
실행: python3 tools/make_hero_images.py .

(이전 Hero home-hero-focus-*.jpg는 2026-11-04 원본 "Startup leaders align around operations.png"에서 만들었다. 파일은 남아 있지만 쓰지 않는다)
"""
import sys
from pathlib import Path
from PIL import Image

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
src = Image.open(root / "assets/Product designer leading a studio critique.png").convert("RGB")
out = root / "assets/images"
W, H = src.size
NAME = "home-hero-rachel-design-review"


def save(im, name, widths):
    for w in widths:
        w = min(w, im.width)
        h = round(im.height * w / im.width)
        # 4:4:4·품질 86: 얼굴 윤곽과 대시보드의 작은 글자·선이 번지지 않게
        im.resize((w, h), Image.LANCZOS).save(out / f"{name}-{w}.jpg", quality=86, subsampling=0, optimize=True, progressive=True)
        print(f"{name}-{w}.jpg {w}×{h}")


# 데스크톱: 원본 비율 그대로 (1774은 원본 폭)
save(src, NAME, (1280, 1774))

# 태블릿(601~900px): 4:3, 원본 높이 전체를 쓰고 오른쪽 끝에 맞춘다 → 얼굴 가로 약 62%, 손 약 48%, 앞쪽 동료 일부
cw = round(H * 4 / 3)
save(src.crop((W - cw, 0, W, H)), NAME + "-tablet", (768, 1152))

# 모바일(~600px): 4:3, Rachel 쪽으로 더 가깝게 → 얼굴 가로 55%·세로 28%, 손 38%·73%, 노트북 화면과 뒤 대시보드 포함
#   375px 화면에서 얼굴 폭이 약 50px → 60px로 커진다
top, bottom = 60, 800
mw = round((bottom - top) * 4 / 3)
save(src.crop((W - mw, top, W, bottom)), NAME + "-mobile", (640, mw))
