"""Open Graph 이미지(1200×630 PNG)를 만든다.
- Second Context: 각 페이지 머리글의 라벨(.label)과 h1을 읽어 브랜드 카드로 → assets/og/<이름>-<ko|en>.png
- 개인 포트폴리오(index.html): Hero의 알약 라벨·h1·이름을 읽어 스타일 C 카드로 → assets/og/portfolio.png
헤드리스 Chrome으로 캡처한다. 사용: python3 tools/build_en_pages.py . 다음에 python3 tools/make_og_images.py .
(페이지 문구를 바꾸면 다시 실행한다)"""
import html, os, re, subprocess, sys, tempfile

R = os.path.abspath(sys.argv[1])
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
# 이미지 이름 → 페이지. 이전 창업자 소개 주소(second-context-about.html)는 홈 이미지를 함께 쓴다
OG = {"home": "second-context.html", "approach": "second-context-approach.html",
      "work": "second-context-work.html", "contact": "second-context-contact.html"}

CARD = """<!doctype html><html lang="{lang}"><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;800&family=Noto+Sans+KR:wght@500;700&display=block">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1200px;height:630px;overflow:hidden;background:#FFFFFF}}
body{{font-family:'Manrope','Noto Sans KR',sans-serif;color:#30232E;padding:72px 80px 64px;display:flex;flex-direction:column;word-break:keep-all}}
.logo{{height:88px;width:auto;align-self:flex-start}}
.main{{flex:1;display:flex;flex-direction:column;justify-content:center}}
.label{{font-size:26px;font-weight:600;color:#A83E20;margin-bottom:20px}}
h1{{font-size:{size}px;font-weight:800;line-height:1.25;letter-spacing:-.01em;max-width:1000px;text-wrap:balance}}
.foot{{display:flex;align-items:center;gap:20px;font-size:22px;font-weight:500}}
.foot i{{display:block;width:56px;height:4px;background:#DA613E}}
</style>
<img class="logo" src="{logo}" alt="">
<div class="main"><p class="label">{label}</p><h1>{title}</h1></div>
<p class="foot"><i></i>rachelcho.github.io/my-portfolio</p>
</html>"""


# 개인 포트폴리오: design-style.md 스타일 C (배경·흰 카드 22px·그림자·알약 라벨, Pretendard)
PORTFOLIO = """<!doctype html><html lang="ko"><meta charset="utf-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1200px;height:630px;overflow:hidden;background:#f3f1ec}}
body{{font-family:'Pretendard',sans-serif;color:#161513;padding:40px;word-break:keep-all}}
.card{{height:100%;background:#ffffff;border-radius:22px;box-shadow:0 2px 10px rgba(22,21,19,.05);padding:56px 64px;display:flex;flex-direction:column}}
.pill{{align-self:flex-start;font-size:18px;font-weight:700;letter-spacing:.06em;background:#e9e5db;color:#6b675f;padding:10px 24px;border-radius:999px}}
h1{{flex:1;display:flex;align-items:center;font-size:52px;font-weight:800;line-height:1.3;letter-spacing:-.02em;text-wrap:balance}}
.foot{{display:flex;justify-content:space-between;align-items:center}}
.name{{font-size:28px;font-weight:800}}
.url{{font-size:20px;color:#6b675f;font-weight:500}}
</style>
<div class="card"><span class="pill">{pill}</span><h1>{title}</h1>
<div class="foot"><span class="name">{name}</span><span class="url">rachelcho.github.io/my-portfolio</span></div></div>
</html>"""


def header(s):
    """머리글(.page-header)의 라벨과 h1"""
    m = re.search(r'(?s)<p class="label">(.*?)</p>\s*<h1[^>]*>(.*?)</h1>', s)
    return [html.unescape(re.sub(r'<[^>]+>', '', g).strip()) for g in m.groups()]


def shoot(tmp, name, card):
    src = os.path.join(tmp, name + ".html")
    open(src, "w", encoding="utf-8").write(card)
    out = os.path.join(R, "assets", "og", name + ".png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--allow-file-access-from-files", "--virtual-time-budget=5000", "--window-size=1200,630",
                    f"--screenshot={out}", "file://" + src], check=True, capture_output=True)
    print("made assets/og/" + name + ".png")


with tempfile.TemporaryDirectory() as tmp:
    os.makedirs(os.path.join(R, "assets", "og"), exist_ok=True)
    for name, page in OG.items():
        for lang, path in (("ko", page), ("en", "en/" + page)):
            s = open(os.path.join(R, path), encoding="utf-8").read()
            label, title = header(s)
            shoot(tmp, f"{name}-{lang}", CARD.format(lang=lang, logo="file://" + os.path.join(R, "assets", "second-context-logo.png"),
                                                     label=html.escape(label), title=html.escape(title),
                                                     size=64 if len(title) <= 34 else 56))

    s = open(os.path.join(R, "index.html"), encoding="utf-8").read()
    pill, title, name = (html.unescape(re.search(p, s).group(1).strip()) for p in
                         (r'<span class="pill">(.*?)</span>', r'(?s)<h1>(.*?)</h1>', r'<div class="name">(.*?)</div>'))
    shoot(tmp, "portfolio", PORTFOLIO.format(pill=html.escape(pill), title=html.escape(title), name=html.escape(name)))
