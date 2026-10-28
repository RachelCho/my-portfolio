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
| Background / White | #FFFFFF | 기본 배경 (2026-10-28 크림에서 변경) |
| Neutral Surface | #F6F6F4 | 옅은 중립 면. 문의 폼처럼 꼭 필요한 영역에만 |
| Brand Cream | #F4F0E8 | 작은 브랜드 요소 전용: 플럼·오렌지 버튼 위 글자, 파비콘 바탕 |
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
| 플럼 / 화이트 | 14.94:1 |
| 조정 오렌지 / 화이트 | 6.22:1 |
| 플럼 / 중립 면(#F6F6F4) | 13.81:1 |
| 조정 오렌지 / 중립 면(#F6F6F4) | 5.75:1 |
| 플럼 / 크림 | 13.15:1 |
| 크림 / 플럼 | 13.15:1 |
| 조정 오렌지 / 크림 | 5.48:1 |
| 크림 / 조정 오렌지 | 5.48:1 |
| 플럼 / 세이지 | 6.37:1 |
| 조정 오렌지 / 흰색 | 6.22:1 |

### 버튼
- Primary: 플럼 배경 + 크림 문구
- Secondary 채움: 조정 오렌지 배경 + 크림 문구
- Secondary 외곽선: 화이트 배경 + 조정 오렌지 문구·테두리

### 사용 금지 조합
- 플럼 ↔ 조정 오렌지 (약 2.40:1): 서로를 글자·배경이나 기능 식별용 경계로 조합하지 않는다
- 세이지 / 크림 (약 2.06:1): 글자나 기능성 아이콘에 쓰지 않는다
- 장식 오렌지 #DA613E: 글자·버튼·기능 요소에 쓰지 않는다

### 창업자 소개 (Founder)
- 사진: assets/rachel-portrait-bw.png (흑백 최종본). 얼굴·외모를 편집하지 않고, 원본 비율을 유지하며 얼굴과 머리를 자르지 않는다
- 사진 아래 3줄: Rachel Cho / Founder & Product UX Consultant / Product Designer · Startup Strategy Coach · Career Mentor
- 구성(2026-10-28 갱신): 제목 "낯선 맥락을 이해하고, 다음 방향을 함께 찾습니다." / "Understanding new contexts. Finding a way forward, together." 창업자 소개 페이지는 사용자가 준 3문단(전문성 / 직접 학비·이민자 커리어·디지털 노매드 / 컨설팅·멘토링)을 그대로 쓰고, 홈 #founder도 같은 3문단 + 경력 수치(창업자 소개 페이지 링크 없음, 2026-10-28 사용자 요청). 메뉴에는 About을 따로 두지 않는다
- 1인칭(나/저)으로 쓰고, '자수성가'·'역경 극복'·'글로벌 리더' 같은 수식어 대신 구체적 경험(직접 학비 마련, 이민자로 쌓은 커리어, 27개국 디지털 노매드)으로 보여준다. 확인되지 않은 어려움·감정·가족사·재정 상황은 덧붙이지 않는다
- 경력 수치(Rachel 제공): 40+ 완료한 프로젝트 / Projects completed · 12+ 함께 일한 글로벌·다국적 기업 / Global & multinational companies worked with · 27 여행한 국가 / Countries visited. 12+를 "약 12개"로 바꾸지 않고, 27은 여행한 국가 수로만 쓴다(일한 국가·시장 수 아님). 투자금은 개인 수치에 넣지 않는다
- 카운트업(assets/count-up.js): HTML에는 최종 값, 화면 60% 진입 시 세 숫자를 동시에 0→최종 값 900ms(ease-out), 방문당 한 번, 언어 전환으로 들어온 페이지에서는 다시 재생하지 않음(lang.js가 sc:counted 전달). 움직임 줄이기·IntersectionObserver 미지원이면 최종 값 그대로. 보이는 숫자는 aria-hidden, sr-only로 최종 값만 읽음, aria-live 없음. tabular-nums + 최종 자릿수만큼 폭 확보
- 회사명은 쓰지 않는다("Y Combinator W21 출신의 미국 헬스케어 스타트업"). 투자금은 회사의 이력이며 개인 성과로 쓰지 않고, 금액은 자료끼리 다르므로($15M / $14.2M) 확인 전까지 넣지 않는다
- 기업 경험은 실제 참여 형태를 존중하고, 27개국은 개인 배경으로만 쓴다(27개 시장 업무·리서치로 바꾸지 않는다)
- 경력 수치는 창업자 소개에만, 프로젝트 개선 수치는 해당 사례(#work)에만 둔다. 프로젝트 성과를 Rachel 개인의 단독 성과로 쓰지 않는다
- 투자 유치를 다시 언급할 때는 회사의 이력으로만 쓴다. 멘토링을 언급할 때는 이민 법률 자격이나 법률 서비스 제공을 주장하지 않는다

### 페이지 구조와 구현 규칙
- 정적 HTML, GitHub Pages(/my-portfolio/ 하위 경로). 링크·이미지는 상대 경로만 쓴다
- 페이지: second-context.html(홈), second-context-approach.html, second-context-contact.html, second-context-about.html(창업자 소개). 기존 포트폴리오 contact.html과 이름이 겹치지 않게 second-context- 접두어를 쓴다
- 공통 스타일은 assets/second-context.css 하나로 관리하고, 헤더·푸터·본문 바로가기는 세 페이지에 같은 구조로 둔다
- 현재 페이지 메뉴에는 aria-current="page"를 넣고 밑줄·굵기로도 표시한다
- 새 탭 링크에는 "(새 탭에서 열림)"을 화면 밖 텍스트(sr-only)로 붙인다
- 버튼은 최소 44×44px, 모바일(900px 이하)에서도 메뉴 링크를 숨기지 않고 줄바꿈한다
- Calendly는 새 탭으로 여는 직접 링크로만 연결한다 (Contact 페이지 일정표 임베드는 2026-10-28에 제거)
- Contact 페이지(2026-10-28 2차 개편, 간결형): 짧은 머리글(라벨 Contact, 제목 40px "제품의 어떤 부분을 개선하고 싶으신가요?", 설명 18px 한 줄) → 데스크톱 폼(최대 640px) | 다른 연락 방법(280px, 이메일+복사, 30분 상담 Calendly). 900px 이하는 폼 → 다른 연락 방법. 같은 안내를 양쪽에 반복하지 않는다. 달력 임베드·사업장 주소·"무료"·"24시간 내 답변" 같은 확인되지 않은 약속 없음
- 문의 폼: 옅은 중립 면(--surface) 하나로 묶고, 입력은 흰 바탕 + 1px 테두리(--field-border, 화이트 대비 3.58:1)·높이 46px. 라벨→입력 8px, 필드 사이 20px, 문의 내용 160px. 데스크톱은 이름|이메일, 회사·제품명|제품 URL 두 열, 600px 이하 한 열
- 항목: 이름*(예: 홍길동)·이메일*(name@company.com)·회사 또는 제품명(회사명 또는 제품명)·제품 URL(https://yourproduct.com)·문의 내용*(제품 소개, 현재 어려운 점, 필요한 도움을 간단히 알려주세요.). 라벨은 항상 보이고, placeholder는 입력 예시로만 연한 회색(--placeholder #7A737C, 화이트 4.59:1). 날짜 항목은 없음
- 폼 동작은 assets/contact-form.js: 필수·이메일·URL 형식 검증, 오류를 aria-invalid·aria-describedby로 연결, 상태는 role=status, 전송 중 버튼 "전송 중… / Sending…"·중복 제출 방지, 실패 시 입력 유지·재시도, 서버 2xx 뒤에만 성공 표시와 초기화
- 문의 수신 주소: rachel.cho5257@gmail.com (2026-10-28 사용자 확인)
- Formspree 폼 주소: https://formspree.io/f/mwllbenr (공개용 주소, 비밀키 아님). second-context-contact.html의 data-endpoint에 넣고 빌드 스크립트로 영어 페이지에 복사된다
- 전송 서비스: Formspree. form의 data-endpoint에 https://formspree.io/f/<폼ID>를 넣으면 버튼이 켜진다. 보내는 항목 이름: name, email(Formspree가 Reply-To로 사용), company, product_url, message, _subject(메일 제목), language(어느 언어 페이지인지), _gotcha(스팸 방지 숨김 칸)
- 이메일: 주소는 mailto 링크(보조 수단) + "이메일 주소 복사 / Copy email" 버튼(클립보드 쓰기가 실제 성공했을 때만 완료 안내, 실패 시 선택 가능한 주소 칸 표시)
- 방문자 화면에는 연결 상태·개발 설정 안내를 쓰지 않는다. 버튼은 항상 플럼 단색 채움, 포커스 외곽선 유지. 기본 상태에서는 오류·상태 문구를 숨기고, 제출할 때만 보내는 중·성공·실패를 role=status로 알린다
- 문구: 보내는 중… / Sending… · 성공 "문의가 접수되었습니다. 남겨주신 이메일로 답변드리겠습니다." / "Thank you. Your inquiry has been received. I’ll reply to the email address you provided." · 실패 "전송하지 못했습니다. 작성하신 내용은 이 화면에 그대로 남아 있습니다. 다시 시도해 주세요." / "Your message couldn’t be sent. What you entered is still on this page. Please try again." (영구 저장을 암시하지 않음)
- 전송 주소는 form의 data-endpoint에만 넣는다. 비어 있으면 보내지 않고 실패 문구만 보인다(성공 표시 금지). data-endpoint가 비어 있는 상태로 배포하지 않는다. 비밀키를 HTML·JS·Git에 넣지 않는다. mailto로 폼 제출을 대신하지 않는다
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
- 머리글(.page-header): 라벨 + 제목(h1/h2) + 첫 소개 문단(.lead)을 하나로 묶는다. Home Hero·Why Us·Use Cases·Contact 안내, Approach·Contact 페이지 도입에 공통 적용 (한국어·영어 동일)
- 첫 소개 문단(.lead): 글자 20px(모바일 600px 이하 18px, --lead-size), 줄 높이 1.7, 굵기 400, 자간 0, 최대 너비 720px, 제목 → 문단 24px(--gap-lead), padding 0. 문단 기본 margin은 지우고 이 규칙으로만 간격을 준다
- 소개 문단 → 다음 콘텐츠: 64px(모바일 40px, --gap-after-lead). `.page-header + [class]` 규칙이 개별 블록의 margin-top보다 우선한다. 본문 중간 문단·카드 설명은 .lead를 쓰지 않는다
- Home Hero: 2열(.hero-grid) 텍스트 55% · 이미지 45%, 사이 64px, 세로 중앙 정렬. 이미지 assets/images/consulting-hero.jpg(1122×1402, 원본 PNG를 크기 그대로 JPEG 품질 90·4:4:4로 압축)를 4:5로 표시하고 object-position 50% 40%, 테두리·그림자·둥근 모서리 없음, 오른쪽 끝은 공통 컨테이너 오른쪽 끝. alt "동료들과 제품 전략을 논의하는 Rachel Cho" / "Rachel Cho discussing product strategy with colleagues". 900px 이하는 텍스트 → 이미지(사이 32px, 이미지 최대 560px)
- 창업자 소개 그리드: 사진 열 --founder-photo 340px(320~360 범위) + 열 사이 --gap-split 64px + 본문은 남은 너비(본문에 별도 max-width를 두지 않음). 위쪽 정렬, 사진은 원본 비율, 900px 이하에서 세로 배치(사진 최대 440px)
- 읽기 너비(--text 720px)는 컨테이너가 아니라 안쪽 요소(.lead, h2, 기획서의 .body > *)에만 건다. `.wrap`과 폭 제한 클래스를 같은 요소에 같이 쓰지 않는다 — 섹션 전체가 가운데로 밀린다
- overflow-x: hidden으로 넘침을 가리지 않는다. 고정 높이는 헤더·버튼 최소 높이, 장식 선에만 쓴다
- 기획서(plan-draft.html)는 자체 CSS를 쓰되 같은 이름의 변수(--gutter·--section-y·--gap-*·--card-pad·--founder-photo)로 같은 규칙을 따른다. 기획서 섹션 위아래는 64px(모바일 48px)

### Selected Work (홈 #work, 메뉴 이름 Work)
- 세 사례는 Rachel의 이전 경력 프로젝트로 소개한다. Second Context가 수주한 고객 프로젝트처럼 쓰지 않는다 (소개 문단: "Second Context를 시작하기 전, Rachel Cho가 이전 경력에서 수행한 세 프로젝트입니다. 고객사 이름은 밝히지 않습니다.")
- 공개 페이지에는 회사·협업사·제품 이름(고객사, 에이전시, 협업 IT 기업, 제품명)과 로고를 넣지 않는다. 제목은 01 미국 홈헬스케어 SaaS의 일정 관리 UX · 02 글로벌 제약사의 운영 모니터링·인시던트 관리 UX · 03 글로벌 테크 기업의 한국어 제품 현지화
- 홈 사례 구조: 왼쪽 번호·분야·연도·제목(h3)·강점 한 줄 | 오른쪽 핵심 설계 판단 → 대표 수치(.metrics) → "사례 자세히 보기" 링크(second-context-work.html#case-…)
- 사례 페이지 second-context-work.html: 사례마다 문제 / 내 역할 / 핵심 설계 판단 / 바뀐 화면과 흐름 / 확인된 결과 | 재구성 화면 + 3단계 인터랙션(assets/case-demo.js). 데스크톱(1101px~)은 화면이 따라 내려오고, 900px 이하는 화면을 먼저 보여 준다
- 재구성 화면: "설계 설명을 위한 재구성 · 예시 데이터"를 작게 표시하고, 예시 데이터는 "예시 환자 A·예시 인시던트 A"처럼 실제 데이터로 보이지 않게 쓴다. 자료에 있는 설계 판단만 보여 주고 새 기능·결과를 만들지 않는다
- 인터랙션: 단계 버튼(aria-current="step", 좌우 화살표), 모션 재생·정지·다시 보기(사용자가 시작, 마지막 단계에서 한 번 멈춤), 사례끼리 상태 공유 없음, 움직임 줄이기 설정에서는 전환 효과 없이 단계 이동만. 언어를 바꾸면 lang.js가 각 사례의 단계를 넘겨 준다
- 사례 02(운영 모니터링)는 데모 두 개를 위아래로 둔다(2026-10-29, 근거: Toptal-2CS-Axle-Pfizer-60min.pdf). A "먼저 대응할 문제를, 먼저 보이게." — 여러 알림 → 기술 신호(이상 점수)+업무 영향(막힌 팀·담당자)으로 P1을 맨 위로(순서 이동은 시연, 실제 화면은 처음부터 이 순서) → 항목 클릭 시 영향받는 팀·관련 신호·담당자·기록. B "과거의 기록에서, 다음에 주의할 신호를." — 프로젝트에서 연결한 관련 기록 수집 → 반복 패턴 → 목록 위 AI 요약(관찰 / 예측 / 근거, '관련 기록 보기'로 근거 펼침). 예측은 가능성으로만 쓰고, 정확도·신뢰도 %·데이터 규모·예측 시간·자동 대응을 만들지 않으며, 성과 수치를 데모 하나의 결과로 연결하지 않는다
- 한 데모를 재생하면 다른 데모의 재생은 멈춘다. 언어 전환 시 lang.js가 데모별 단계·선택 항목(data-sel)·펼침 상태를 넘긴다
- 현지화 비교 화면은 <!--i18n:keep--> 안에 두어 두 언어 페이지에서 원문·한국어를 그대로 유지한다. 실제 프로젝트 화면이 아닌 예시 문구임을 표시한다
- 대표 수치는 숫자 바로 옆에 지표 종류(사용자 평가·업무 성과·도입 범위·리서치 범위·프로젝트 기간)와 어떤 변화의 결과인지를 함께 쓴다. 숫자만 나열하지 않는다
- 기존 수치와 단위를 그대로 유지한다. 요약하면서 지우거나 "효율 개선"처럼 모호하게 바꾸지 않고, 서로 다른 지표를 합치지 않으며, 새 수치나 근거 없는 인과관계를 넣지 않는다
- 수치 출처는 공개 자료만: 이전 사이트 사례(4d60b08), 웹사이트용 이력서 PDF, yeagyeong.com 홈 카드. 자료끼리 값이 충돌하면 둘 다 보존하고 사용자에게 검토 항목으로 알린다
- 세 사례 아래 공통 마무리: "비슷한 과제를 고민하고 계신가요?" + [30분 상담 예약하기](Calendly) [협업 방식 보기](Approach)
### 다국어 (한국어·영어)
- 기본 언어는 한국어. 한국어 URL은 그대로 두고, 영어는 en/ 폴더에 같은 파일 이름으로 둔다 (en/second-context.html, en/second-context-approach.html, en/second-context-contact.html)
- 첫 방문은 한국어. 브라우저 언어·접속 국가에 따른 자동 이동을 하지 않는다. 실시간 번역 API를 쓰지 않는다
- assets/lang.js(모든 페이지 head, 빌드 스크립트가 넣음): 언어 링크를 누르면 선택을 localStorage에 기억하고, 영어를 고른 뒤 한국어(기본) 주소로 다시 오면 같은 페이지의 영어판으로 이어 준다. 전환할 때 보던 영역(섹션·사례 id 기준), 펼친 사례(details id), 작성 중인 문의 입력을 sessionStorage로 넘겨 복원한다. 저장이 막혀도 페이지는 그대로 동작한다
- 사례·펼침 id는 언어와 무관하게 고정: case-healthcare · case-monitoring · case-localization (+ -detail)
- 헤더 오른쪽에 언어 링크 "한국어 / EN"(국기·스위치 금지, EN은 화면 밖 텍스트 English로 읽힘). `<nav class="lang">`, 현재 언어는 aria-current="true" + 굵기·밑줄, 각 링크에 lang·hreflang, 누르는 영역 44×44px 이상. 1100px 이하에서도 첫 줄(로고 옆)에 둔다
- 언어 링크는 현재 페이지의 다른 언어 페이지로 연결하고, 각 언어의 내부 링크는 같은 언어 페이지로만 연결한다 (선택 언어 유지)
- 페이지마다 html lang, title, description, canonical(자기 언어 URL), hreflang ko·en·x-default(한국어)를 둔다. 한국어 title은 한국어(Second Context — 시장을 넘나드는 제품 디자인 / 협업 방식 / 문의)
- 번역 관리: 화면 문구는 한국어 HTML(원본)과 tools/build_en_pages.py의 번역 표 한 곳에서만 관리하고, 폼·복사 안내 메시지는 assets/contact-form.js 안의 ko/en 묶음에서 관리한다. en/*.html을 직접 고치지 않는다
- 실제 제품 스크린샷을 넣을 때는 화면 속 문구를 번역용으로 바꾸지 않고, 주석·설계 포인트·해설만 HTML 텍스트로 두어 번역 표로 전환한다
- 영어 페이지는 한국어 페이지에서 만든다: 한국어 문구를 고친 뒤 `python3 tools/build_en_pages.py .`를 실행하고, 새 문구는 스크립트의 번역 표에 추가한다. 표에 없는 한국어가 남으면 스크립트가 멈춘다
- 이름·브랜드명·숫자(40+, 12+, 27, 사례별 수치와 단위)·서비스 범위를 그대로 유지한다
- 메뉴 표기: Why Us · Services · Work · Approach · Contact (두 언어 공통, 대문자 강제 변환 없음)
- 헤더는 1100px 이하에서 두 줄(로고·언어 / 메뉴), 그 위에서는 한 줄. 영어 길이 때문에 버튼·메뉴를 고정 폭·고정 높이로 자르지 않는다
- Calendly 예약 화면의 언어는 Calendly 쪽 설정을 따르며 사이트 번역 범위가 아니다

### 공식 기준
- https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html
