# Second Context 화면 목록 (screens.md)

- 기준 버전: 2026-11-11, 커밋 `947f46e` (로컬 파일과 공개 사이트 https://rachelcho.github.io/my-portfolio/ 의 HTML·CSS·JS 해시가 같음을 확인)
- 대상: Second Context 사이트(B2B 프로덕트 디자인 컨설팅). 포트폴리오(index.html 등)는 이 문서에 넣지 않는다
- 영어 페이지는 `en/` 폴더에 같은 파일 이름으로 있고, 한국어 원본에서 `tools/build_en_pages.py`로 만든다(직접 고치지 않음)
- 공통 헤더·검색·푸터는 `tools/sc_chrome.py`가 다섯 페이지에 같은 구조로 넣는다

## 1. 독립 페이지

| ID | 화면 | 파일 (한국어 / 영어) | 역할 | 진입 경로 | 주요 행동 |
|---|---|---|---|---|---|
| S-01 | 홈 | `second-context.html` / `en/second-context.html` | 필요성 → 적합성 → 신뢰 → 문의를 한 페이지에서 | 직접 주소, 모든 페이지의 로고·헤더 메뉴·푸터 Company | 프로젝트 문의하기(#contact) · 사례 살펴보기(#work) · 상담 예약(Calendly) · 홈 안 문의 폼 전송 |
| S-02 | Approach (협업 방식) | `second-context-approach.html` | 6단계 진행 방식·산출물·기대 효과 확인 | 홈 #approach의 "진행 방식 자세히 보기", 검색 | 30분 상담 예약하기(→ S-04#booking) · 프로젝트 문의하기(→ S-01#contact) |
| S-03 | 사례 상세 (Work) | `second-context-work.html` | 세 사례의 문제·역할·설계 판단·결과와 단계형 데모 | 홈 #work 사례 카드 6개(사례당 2개), 검색 | 데모 단계 이동·재생·정지, 사례 02 탭 전환 |
| S-04 | Contact (문의 페이지) | `second-context-contact.html` | 홈과 같은 문의 폼 + 다른 연락 방법 | **Approach의 "30분 상담 예약하기" 버튼 두 곳(→ #booking)뿐**. 홈·헤더·푸터·검색(site.js INDEX)에는 이 페이지가 없음 | 문의 보내기 · 이메일 주소 복사 · 30분 상담 예약하기 |
| S-05 | About Second Context | `second-context-about.html` | 소개 세 문단 · 경력 수치 · 경력 목록 · 멘토링 | 홈 #founder의 "About Second Context" 버튼, 검색 | 수치 확인, 홈으로 이동 |

## 2. 홈 내부 영역 (S-01, 위에서 아래 순서)

| 번호 | 영역 | 앵커 | 바탕 | 내용 요약 |
|---|---|---|---|---|
| 1 | Header | (고정 헤더) | 검정 | 로고 · 메뉴 5 · 상담 캡슐 · 한국어/EN · 검색 |
| 2 | Hero | `#top` | 영상 | 배경 영상 + 제목·설명·버튼 2 |
| 3 | Why Us | `#why-us` | 검정 | 문제의식 · 사진 2 · 차별점 3 · About Second Context(`#founder`) · 경험한 제품과 맡은 역할(`#experience`) |
| 4 | Services | `#services` | 흰색 | 서비스 4 · 사진 2 |
| 5 | Selected Work | `#work` | 검정 | 사례 3(각 카드 2) · 예시 콘셉트 안내 |
| 6 | Approach | `#approach` | 흰색 | 사진 띠 · 4단계 · 자세히 보기 |
| 7 | Contact | `#contact` | 검정 | 문의 폼(`#inquiry`) · 다른 연락 방법(`#email-contact`, `#booking`) |
| 8 | Footer | — | 검정 | Let’s 회전 단어 · Company · Follow · Newsletter · 로고·언어·저작권 |

About Second Context·Founder는 독립 영역이 아니라 Why Us 안에 중첩되어 있다(`#why-us > .why-about#founder`).

## 3. 공통 오버레이

| ID | 화면 | 진입 | 행동 |
|---|---|---|---|
| O-01 | 사이트 검색 | 헤더 검색 버튼 | 검색어 입력 → 같은 언어의 페이지·사례 결과, Esc·닫기로 닫힘 |
| O-02 | 모바일 메뉴 패널 | 1200px 이하 "Menu" 버튼 | 메뉴 5 + 큰 상담 캡슐, Esc로 닫힘 |

## 4. 외부 서비스

| ID | 이름 | 사이트가 관여하는 범위 |
|---|---|---|
| X-01 | Calendly (https://calendly.com/yeagyeong/meeting-with-rachel-cho) | 새 탭으로 여는 링크까지. 예약 확정·안내 메일은 Calendly 설정 |
| X-02 | Formspree (https://formspree.io/f/mwllbenr) | 문의 전송 요청과 2xx 응답 처리까지. 메일 도착은 운영자가 확인 |
| X-03 | LinkedIn 회사 페이지 · GitHub | 푸터 Follow의 새 탭 링크 |
| X-04 | 뉴스레터 구독 서비스 | **연결 안 됨** (`form.newsletter`의 `data-endpoint` 비어 있음) |
