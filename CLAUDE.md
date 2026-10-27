# 조예경 포트폴리오

## 프로젝트 개요
- 프로젝트명: 조예경 포트폴리오
- 목적: 디자인 작업물을 소개하는 개인 포트폴리오 사이트

## 핵심 기능
1. 자기소개: 포트폴리오 소유자의 소개를 제공한다.
2. 작업물 목록: 등록된 디자인 작업물을 목록으로 보여준다.
3. 작업물 상세: 선택한 작업물의 상세 내용을 보여준다.
4. 로그인: 사용자 인증 기능을 제공한다.
5. 작업물 관리: 작업물을 등록, 수정, 삭제할 수 있다.

## 프로젝트 작업 기준
- 앞으로 이 프로젝트를 작업할 때 이 문서의 목적과 핵심 기능을 참고한다.
- 기존 파일과 구현 상태를 먼저 확인한 뒤 필요한 부분을 수정한다.
- 기술 스택, 로그인 방식과 작업물 관리 권한은 아직 정해지지 않았다. 구현에 필요하면 사용자에게 확인한다.
- 작업 후 변경 사항과 실제로 확인한 결과를 설명한다.

## 디자인 방향
- 선택한 스타일: 스타일 C — 카드형 벤토 그리드
- 디자인 기준은 design-style.md를 따른다.
- 화면을 만들 때 style-c-grid.html도 직접 읽어 색상, 여백, 카드와 레이아웃을 참고한다.
- 이름: Rachel Cho | 조예경
- 소개 문구: Senior Product Designer specializing in B2B SaaS and enterprise products.

## 지켜야 할 것
- design-style.md의 "수정 시 지켜야 할 것" 항목을 그대로 따를 것

## 오늘 배운 것
- CLAUDE.md로 프로젝트 규칙 관리하기
- 스타일 문서와 HTML 예시를 함께 참고하기
- 선택한 스타일로 첫 화면 만들기
- 변경사항을 커밋하고 push하기

## 메모
- 이 스타일을 고른 이유: 디자이너 포트폴리오에 적합하고 정보 구조가 명확하여 선택했다. 케이스스터디를 중심으로 작업물을 보여주고, 별도의 About 페이지와 이력서 PDF 업로드 및 다운로드 기능을 제공한다.
- 내 소개 문구 방향: B2B SaaS와 엔터프라이즈 제품을 전문으로 하는 시니어 프로덕트 디자이너
- 이 스타일에서 바꾸고 싶은 부분: 별도의 Contact 페이지와 문의 폼 대신, 모든 페이지의 푸터에 이메일과 LinkedIn 링크를 배치한다.

## Second Context 브랜드 규칙 (필수)
- 적용 대상: second-context.html, plan-draft.html, plan-draft.md 등 Second Context 관련 화면과 문서
- 포트폴리오(index.html)의 스타일 C 기준과 별개로 적용한다.
- 아래 컬러 토큰과 WCAG 2.2 AA 색상 대비 조건은 필수 디자인 규칙이다. 화면을 바꿀 때마다 hover·active·focus를 포함해 대비를 다시 계산한다.

### 확정 컬러 토큰
| 토큰 | HEX | 역할 |
|---|---|---|
| Primary / Context Plum | #30232E | 제목, 본문, Primary 버튼 |
| Secondary / Accessible Orange | #A83E20 | 기능성 강조, Secondary 버튼, 강조 글자 |
| Background / Warm Cream | #F4F0E8 | 기본 배경, 어두운 배경 위 글자 |
| Surface / Soft Sage | #9DAE9A | 보조 배경, 정보 패널 |
| Decorative Accent / Signal Orange | #DA613E | 승인 로고, 순수 장식 선·그래픽 전용 |

### 접근성 필수 조건 (WCAG 2.2 AA 색상 대비)
- 일반 글자: 배경과 4.5:1 이상
- 큰 글자: 최소 3:1 이상, 브랜드 내부 목표는 가능하면 4.5:1 이상
- 식별에 필요한 아이콘·컨트롤 경계·상태 표시: 인접 색상과 3:1 이상
- 링크는 밑줄 등 색상 이외의 구분을 함께 제공
- 오류·성공·선택 상태는 문구나 아이콘을 함께 제공
- hover, active, focus 상태도 실제 배경과의 대비를 검증
- 키보드 포커스는 명확하게 보이고 다른 요소에 가려지지 않게 구현
- 색상 대비는 WCAG 기준의 일부입니다. 대비 검증만으로 사이트 전체가 WCAG를 충족한다고 표현하지 않습니다.

### 승인된 조합
| 글자 / 배경 | 대비 |
|---|---|
| 플럼 / 크림 | 13.15:1 |
| 크림 / 플럼 | 13.15:1 |
| 조정 오렌지 / 크림 | 5.48:1 |
| 크림 / 조정 오렌지 | 5.48:1 |
| 플럼 / 세이지 | 6.37:1 |
| 조정 오렌지 / 흰색 | 6.22:1 |

### 버튼
- Primary: 플럼 배경 + 크림 문구
- Secondary 채움: 조정 오렌지 배경 + 크림 문구
- Secondary 외곽선: 크림 배경 + 조정 오렌지 문구·테두리

### 사용 금지 조합
- 플럼 ↔ 조정 오렌지 (약 2.40:1): 서로를 글자·배경이나 기능 식별용 경계로 조합하지 않는다
- 세이지 / 크림 (약 2.06:1): 글자나 기능성 아이콘에 쓰지 않는다
- 장식 오렌지 #DA613E: 글자·버튼·기능 요소에 쓰지 않는다

### 창업자 소개 (Founder)
- 사진: ./rachel-portrait-bw.png (흑백 최종본). 얼굴·외모를 편집하지 않고, 원본 비율을 유지하며 얼굴과 머리를 자르지 않는다
- 사진 아래 3줄: Rachel Cho / Founder, Second Context / Product Designer · Startup Strategy Coach · Career Mentor
- 소개문은 사용자가 준 최종본을 그대로 쓰고 직접 작성하지 않는다
- 글로벌 기업 12곳 이상, 27개국 경험, 1,500만 달러를 투자 유치한 YC 스타트업의 창업 디자이너 경력을 서로 구분한다
- 투자 유치는 회사의 이력이며, 본인이 직접 투자를 유치했다는 의미로 바꾸지 않는다
- 멘토링은 본인 경험 기반의 비자·학교 선택·커리어 설계 도움이며, 이민 법률 자격이나 법률 서비스 제공을 주장하지 않는다

### 페이지 구조와 구현 규칙
- 정적 HTML, GitHub Pages(/my-portfolio/ 하위 경로). 링크·이미지는 상대 경로만 쓴다
- 페이지: second-context.html(홈), second-context-approach.html, second-context-contact.html. 기존 포트폴리오 contact.html과 이름이 겹치지 않게 second-context- 접두어를 쓴다
- 공통 스타일은 assets/second-context.css 하나로 관리하고, 헤더·푸터·본문 바로가기는 세 페이지에 같은 구조로 둔다
- 현재 페이지 메뉴에는 aria-current="page"를 넣고 밑줄·굵기로도 표시한다
- 새 탭 링크에는 "(새 탭에서 열림)"을 화면 밖 텍스트(sr-only)로 붙인다
- 버튼은 최소 44×44px, 모바일(900px 이하)에서도 메뉴 링크를 숨기지 않고 줄바꿈한다
- Calendly는 직접 링크를 항상 제공하고, 임베드는 title이 있는 iframe으로 추가한다
- 실제 전송 수단이 없는 문의 폼은 게시하지 않는다. 현재 문의는 이메일(mailto)로 받는다
- 성과 수치·고객 실적·매출 증가 등을 임의로 추가하거나 보장하지 않는다
- 파비콘: 승인 로고(Second context framed wordmark logo.png)의 두 열린 사각 프레임 심볼만 크림 배경 위에 사용한다. 워드마크·가운데 채움 네모는 넣지 않는다
  - 파일: favicon.ico(16·32·48px, 저장소 루트), assets/favicon-32.png(32×32)
  - 연결: Second Context 페이지마다 <title> 바로 아래에 상대 경로로 둔다
    `<link rel="icon" href="favicon.ico" sizes="any">`
    `<link rel="icon" href="assets/favicon-32.png" type="image/png" sizes="32x32">`
  - 새 Second Context 페이지를 만들면 같은 두 줄을 넣는다. 경로를 /로 시작하지 않는다(/my-portfolio/ 하위 경로 유지)

### 레이아웃 간격 규칙 (공통 컨테이너)
| 역할 | 변수 | 데스크톱 (901px~) | 태블릿 (601~900px) | 모바일 (~600px) |
|---|---|---|---|---|
| 콘텐츠 최대 폭 | --max | 1200px | 1200px | 1200px |
| 좌우 여백 (공통 기준선) | --gutter | 32 | 32 | 16 |
| 섹션 위아래 | --section-y | 96 | 64 | 64 |
| 라벨 → 제목 | --gap-label | 16 | 16 | 16 |
| 제목 → 설명 문단, 짧은 주석 | --gap-lead | 24 | 24 | 24 |
| 제목·설명 → 본문 블록(카드 목록·두 열·CTA 줄) | --gap-block | 48 | 48 | 48 |
| 문단 ↔ 문단 | --gap-para | 24 | 24 | 24 |
| 패널 제목 → 내용 | --gap-sub | 16 | 16 | 16 |
| 두 열(사진·본문, 소개·문의, 단계 제목·설명) 사이 | --gap-split | 64 | 세로 쌓임 | 세로 쌓임 |
| 두 열이 세로로 쌓일 때 | --gap-stack | — | 32 | 32 |
| 카드 목록 사이 | --gap-grid | 24 | 24 | 24 |
| 카드·패널 안쪽 | --card-pad | 32 | 32 | 24 |
| 라벨 ↔ 값, 목록 항목 (반 단계) | --gap-tight | 4 | 4 | 4 |

- 모든 Second Context 페이지(Home·Approach·Contact)는 헤더·각 섹션·푸터에 같은 `.wrap` 컨테이너 하나만 쓴다. `.wrap`을 중첩하거나 페이지별로 좌우 padding을 따로 주지 않는다
- 배경이 화면 전체를 채우는 섹션도 배경은 `section`에, 내용은 안쪽 `.wrap`에 두어 같은 기준선에 맞춘다
- 간격은 assets/second-context.css의 변수만 쓰고, 값은 8 / 16 / 24 / 32 / 48 / 64 / 96px 간격 체계에서 고른다 (예외: --gap-tight 4px)
- 버튼 안쪽 여백: 기본 16·24px, 헤더 버튼 8·16px, 최소 높이 44px
- 창업자 소개는 Home의 #founder 섹션이며 별도 About 페이지는 없다 (about.html은 포트폴리오 페이지)
- 창업자 소개 그리드: 사진 열 --founder-photo 340px(320~360 범위) + 열 사이 --gap-split 64px + 본문은 남은 너비(본문에 별도 max-width를 두지 않음). 위쪽 정렬, 사진은 원본 비율, 900px 이하에서 세로 배치(사진 최대 440px)
- 읽기 너비(--text 720px)는 컨테이너가 아니라 안쪽 요소(.lead, h2, 기획서의 .body > *)에만 건다. `.wrap`과 폭 제한 클래스를 같은 요소에 같이 쓰지 않는다 — 섹션 전체가 가운데로 밀린다
- overflow-x: hidden으로 넘침을 가리지 않는다. 고정 높이는 Calendly iframe, 헤더·버튼 최소 높이, 장식 선에만 쓴다
- 기획서(plan-draft.html)는 자체 CSS를 쓰되 같은 이름의 변수(--gutter·--section-y·--gap-*·--card-pad·--founder-photo)로 같은 규칙을 따른다. 기획서 섹션 위아래는 64px(모바일 48px)

### 다국어 (한국어·영어)
- 기본 언어는 한국어. 한국어 URL은 그대로 두고, 영어는 en/ 폴더에 같은 파일 이름으로 둔다 (en/second-context.html, en/second-context-approach.html, en/second-context-contact.html)
- 브라우저 언어·접속 국가에 따른 자동 이동을 하지 않는다. 실시간 번역 API를 쓰지 않는다
- 헤더 오른쪽에 언어 이름 링크 "한국어 | English"(국기·스위치 금지). `<nav class="lang">`, 현재 언어는 aria-current="true" + 굵기·밑줄, 각 링크에 lang·hreflang
- 언어 링크는 현재 페이지의 다른 언어 페이지로 연결하고, 각 언어의 내부 링크는 같은 언어 페이지로만 연결한다 (선택 언어 유지)
- 페이지마다 html lang, title, description, canonical(자기 언어 URL), hreflang ko·en·x-default(한국어)를 둔다
- 영어 페이지는 한국어 페이지에서 만든다: 한국어 문구를 고친 뒤 `python3 tools/build_en_pages.py .`를 실행하고, 새 문구는 스크립트의 번역 표에 추가한다. 표에 없는 한국어가 남으면 스크립트가 멈춘다
- 이름·브랜드명·숫자(27개국, 12개 이상, $15M)·서비스 범위를 그대로 유지한다. $15M은 회사(Y Combinator 스타트업)의 투자 유치 이력으로만 쓴다
- 헤더는 1100px 이하에서 두 줄(로고·언어 / 메뉴), 그 위에서는 한 줄. 영어 길이 때문에 버튼·메뉴를 고정 폭·고정 높이로 자르지 않는다
- Calendly 예약 화면의 언어는 Calendly 쪽 설정을 따르며 사이트 번역 범위가 아니다

### 공식 기준
- https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html
