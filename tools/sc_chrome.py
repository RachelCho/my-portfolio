"""Second Context 다섯 페이지(한국어 원본)에 같은 헤더·검색 오버레이·푸터를 넣는다 (2026-11-10 다크 리디자인).
사용: python3 tools/sc_chrome.py . && python3 tools/build_en_pages.py .
언어 링크는 build_en_pages.py가 검색 버튼 바로 앞에 넣는다. 영어 문구는 build_en_pages.py의 COMMON 표에서 바꾼다."""
import os, re, sys

R = sys.argv[1]
PAGES = ["second-context.html", "second-context-approach.html", "second-context-contact.html", "second-context-about.html", "second-context-work.html"]
# 헤더·푸터 메뉴는 홈의 섹션으로 연결한다(2026-11-10 2차). 하위 페이지는 관련 섹션을 현재 위치로 표시
# 메뉴 이름은 두 언어 모두 영어로 고정(2026-11-10 사용자 요청). 헤더·푸터 공통
# 상담·문의 버튼은 2026-11-11 사용자 요청으로 한국어 페이지에서 "30분 상담 예약" · "프로젝트 문의하기"(영어는 build_en_pages.py 표)
SECTIONS = [("why-us", "Why Us"), ("services", "Services"), ("work", "Work"), ("approach", "Approach"), ("contact", "Contact")]
CURRENT = {"second-context-about.html": "why-us", "second-context-work.html": "work",
           "second-context-approach.html": "approach", "second-context-contact.html": "contact"}
CALENDLY = "https://calendly.com/yeagyeong/meeting-with-rachel-cho"
# 외부 링크: 주소가 비어 있으면 링크 없이 '준비 중'으로 표시한다
LINKEDIN = "https://www.linkedin.com/company/second-context/"
GITHUB = "https://github.com/RachelCho"
NEW_TAB = '<span class="sr-only"> (새 탭에서 열림)</span>'
# 로고: 두 사각 프레임 + 워드마크가 함께 있는 승인 로고의 흰색판(800×326, 안쪽 여백 포함). 헤더·푸터 공통
WORDMARK = '<img src="assets/second-context-logo-white.png" alt="second context" width="800" height="326"'


def home(page):
    return "" if page == PAGES[0] else "second-context.html"


def section_link(page, sid, name, cur_attr=True):
    cur = ' aria-current="true"' if cur_attr and CURRENT.get(page) == sid else ''
    return f'<a{cur} href="{home(page)}#{sid}" data-nav="{sid}">{name}</a>'


def follow(url, name, who):
    if not url:
        return f'<span class="fl-off">{name} <span class="fl-off-note">준비 중</span></span>'
    return f'<a href="{url}" target="_blank" rel="noopener">{name}<span class="sr-only"> — {who}</span>{NEW_TAB}</a>'


SEARCH_ICON = ('<svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
               'stroke-linecap="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5"/></svg>')
ARROW = ('<svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')


def header(page):
    links = "".join(f"      {section_link(page, sid, name)}\n" for sid, name in SECTIONS)
    return ('<header class="site-header">\n  <div class="wrap">\n'
            f'    <a href="second-context.html" class="logo" aria-label="Second Context 홈">{WORDMARK}></a>\n'
            '    <button type="button" class="menu-toggle" aria-expanded="false" aria-controls="main-nav"><span class="menu-icon" aria-hidden="true"><i></i><i></i></span><span class="menu-toggle-text">Menu</span></button>\n'
            '    <nav class="main-nav" id="main-nav" aria-label="주요 메뉴">\n'
            + links +
            f'      <a class="pill pill-light nav-cta" href="{CALENDLY}" target="_blank" rel="noopener"><span class="nav-cta-text">30분 상담 예약</span>{NEW_TAB}</a>\n'
            '    </nav>\n'
            f'    <button type="button" class="search-open" aria-haspopup="dialog" aria-controls="search" aria-expanded="false">{SEARCH_ICON}<span class="sr-only">사이트 검색</span></button>\n'
            '  </div>\n</header>\n\n'
            '<div class="search" id="search" role="dialog" aria-modal="true" aria-labelledby="search-title" hidden>\n'
            '  <div class="wrap">\n'
            '    <div class="search-top">\n'
            '      <p class="search-title" id="search-title">사이트 검색</p>\n'
            '      <button type="button" class="search-close"><span>닫기</span><svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg></button>\n'
            '    </div>\n'
            '    <form class="search-form" role="search" aria-label="사이트 검색">\n'
            '      <label class="sr-only" for="search-input">사이트 검색어</label>\n'
            '      <input id="search-input" type="search" autocomplete="off" placeholder="사례, 서비스, 페이지 검색">\n'
            f'      <button type="submit" class="circle-btn circle-btn--dark">{SEARCH_ICON}<span class="sr-only">검색</span></button>\n'
            '    </form>\n'
            '    <p class="search-status" role="status" aria-live="polite"></p>\n'
            '    <ul class="search-results"></ul>\n'
            '  </div>\n</div>\n')


def footer(page):
    company = "".join(f"          <li>{section_link(page, sid, name, False)}</li>\n" for sid, name in SECTIONS)
    return ('<footer class="site-footer">\n  <div class="wrap">\n'
          '    <div class="lets" data-rotator data-words="Understand|Design|Build|Collaborate" data-interval="2400">\n'
          '      <p class="lets-title" aria-hidden="true"><span><span class="lets-lead">Let’s</span><span class="lets-word is-in">Understand</span></span></p>\n'
          '      <p class="lets-sentence">Let’s understand, design, build, and collaborate.</p>\n'
          '      <div class="lets-actions">\n'
          f'        <a class="lets-cta" href="{home(page)}#contact"><span class="pill pill-light">프로젝트 문의하기</span><span class="circle-btn circle-btn--light">{ARROW}</span></a>\n'
          '        <button type="button" class="lets-toggle" aria-pressed="false" hidden><span class="lets-toggle-text">일시정지</span><span class="sr-only"> 움직이는 문구</span></button>\n'
          '      </div>\n'
          '    </div>\n'
          '    <div class="footer-links">\n'
          '      <nav class="fl-col" aria-labelledby="fl-company">\n'
          '        <p class="fl-title" id="fl-company">Company</p>\n'
          '        <ul>\n' + company +
          '        </ul>\n'
          '      </nav>\n'
          '      <nav class="fl-col" aria-labelledby="fl-follow">\n'
          '        <p class="fl-title" id="fl-follow">Follow</p>\n'
          '        <ul>\n'
          f'          <li>{follow(LINKEDIN, "LinkedIn", "Second Context 회사 페이지")}</li>\n'
          f'          <li>{follow(GITHUB, "GitHub", "Rachel Cho")}</li>\n'
          '        </ul>\n'
          '      </nav>\n'
          '      <form class="newsletter" data-endpoint="" novalidate aria-labelledby="nl-title">\n'
          '        <p class="fl-title" id="nl-title">Newsletter <span class="nl-badge">준비 중</span></p>\n'
          '        <label class="newsletter-label" for="nl-email">뉴스레터 구독 이메일</label>\n'
          '        <div class="newsletter-field">\n'
          '          <input id="nl-email" type="email" name="email" autocomplete="email" inputmode="email" placeholder="name@company.com" aria-describedby="nl-status">\n'
          f'          <button type="submit" class="circle-btn circle-btn--dark">{ARROW}<span class="sr-only">뉴스레터 구독 신청</span></button>\n'
          '        </div>\n'
          '        <p class="newsletter-status" id="nl-status" role="status" aria-live="polite"></p>\n'
          '      </form>\n'
          '    </div>\n'
          '    <div class="footer-bottom">\n'
          f'      <a href="second-context.html" class="footer-logo" aria-label="Second Context 홈">{WORDMARK} loading="lazy"></a>\n'
          '      <p class="footer-copy">© Second Context <span data-year>2026</span></p>\n'
          '    </div>\n'
          '  </div>\n</footer>\n')


for page in PAGES:
    p = os.path.join(R, page)
    s = open(p, encoding="utf-8").read()
    # 헤더(+이전 검색 오버레이)를 새로 쓴다
    s, n = re.subn(r'<header[^>]*>.*?</header>\n(\n<div class="search".*?\n</div>\n)?', lambda m: header(page), s, count=1, flags=re.S)
    assert n == 1, page
    s, n = re.subn(r'<footer[^>]*>.*?</footer>\n', lambda m: footer(page), s, count=1, flags=re.S)
    assert n == 1, page
    if '<script src="assets/site.js" defer></script>' not in s:
        s = s.replace('</body>', '<script src="assets/site.js" defer></script>\n</body>', 1)
    open(p, "w", encoding="utf-8").write(s)
    print("chrome", page)
