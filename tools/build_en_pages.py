"""Second Context 한국어 페이지에 언어 전환·hreflang을 넣고, 번역 표로 en/ 영어 페이지를 만든다.
사용: python3 tools/build_en_pages.py .   (여러 번 실행해도 결과가 같다)"""
import os, re, sys

R = sys.argv[1]
BASE = "https://rachelcho.github.io/my-portfolio/"
PAGES = ["second-context.html", "second-context-approach.html", "second-context-contact.html"]


def head_links(page):
    ko, en = BASE + page, BASE + "en/" + page
    return (f'<link rel="alternate" hreflang="ko" href="{ko}">\n'
            f'<link rel="alternate" hreflang="en" href="{en}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{ko}">\n')


def lang_nav(page, cur):
    if cur == "ko":
        return ('    <nav class="lang" aria-label="언어 선택">\n'
                f'      <a href="{page}" lang="ko" hreflang="ko" aria-current="true">한국어</a>\n'
                '      <span aria-hidden="true">|</span>\n'
                f'      <a href="en/{page}" lang="en" hreflang="en">English</a>\n'
                '    </nav>\n')
    return ('    <nav class="lang" aria-label="Language">\n'
            f'      <a href="../{page}" lang="ko" hreflang="ko">한국어</a>\n'
            '      <span aria-hidden="true">|</span>\n'
            f'      <a href="{page}" lang="en" hreflang="en" aria-current="true">English</a>\n'
            '    </nav>\n')


def prep_korean(page):
    """한국어 원본에 canonical·hreflang·언어 전환만 추가한다. 본문은 건드리지 않는다."""
    p = os.path.join(R, page)
    s = open(p, encoding="utf-8").read()
    s = re.sub(r'<link rel="canonical"[^>]*>\n(<link rel="alternate"[^>]*>\n)*', "", s)
    s = re.sub(r'    <nav class="lang".*?    </nav>\n', "", s, flags=re.S)
    anchor = '<link rel="icon" href="assets/favicon-32.png" type="image/png" sizes="32x32">\n'
    assert s.count(anchor) == 1
    s = s.replace(anchor, anchor + f'<link rel="canonical" href="{BASE + page}">\n' + head_links(page))
    end = "    </nav>\n  </div>\n</header>"
    assert s.count(end) == 1
    s = s.replace(end, "    </nav>\n" + lang_nav(page, "ko") + "  </div>\n</header>")
    open(p, "w", encoding="utf-8").write(s)
    return s


COMMON = [
    ('<html lang="ko">', '<html lang="en">'),
    ('본문 바로가기', 'Skip to main content'),
    ('aria-label="Second Context 홈"', 'aria-label="Second Context home"'),
    ('aria-label="주요 메뉴"', 'aria-label="Main menu"'),
    ('(새 탭에서 열림)', '(opens in a new tab)'),
    ('30분 상담 예약하기', 'Book a 30-minute call'),
    ('30분 상담 예약', 'Book a 30-min call'),
    ('프로젝트 문의하기', 'Send a project inquiry'),
    ('30분 상담으로 시작합니다.', 'Start with a 30-minute call.'),
]

HOME = [
    ('미국 시장을 준비하는 한국 B2B SaaS 팀을 위한 제품 UX 진단과 디자인.',
     'Product UX reviews and design for Korean B2B SaaS teams preparing for the U.S. market.'),
    ('새로운 시장,<br>새로운 사용 맥락.', 'New markets,<br>new contexts of use.'),
    ('미국 시장을 준비하는 한국 B2B SaaS 팀을 위해 제품 UX 진단부터 실제 디자인까지 함께합니다.',
     'We work with Korean B2B SaaS teams preparing for the U.S. market, from product UX reviews to hands-on design.'),
    ('헬스케어 · 엔터프라이즈 · 복잡한 운영 워크플로', 'Healthcare · Enterprise · Complex operational workflows'),
    ('관련 사례 보기', 'See related work'),
    ('동료들과 제품 전략을 논의하는 Rachel Cho', 'Rachel Cho discussing product strategy with colleagues'),
    ('번역만으로는 제품이 현지에서 쓰이지 않습니다.', 'Translation alone won’t get your product used in a new market.'),
    ('같은 제품도 시장과 사용자가 달라지면 다른 맥락에서 사용됩니다. 사용자가 일하는 방식, 제품을 이해하는 방식, 신뢰를 판단하는 기준이 함께 달라지고, 한국 시장에 맞춰 제품을 만들어 온 팀은 이 차이를 내부에서 발견하기 어렵습니다.',
     'When the market and users change, the same product is used in a different context. How people work, how they make sense of a product, and how they judge trust all shift with it—and teams that built for the Korean market often find these differences hard to see from the inside.'),
    ('번역 중심 현지화', 'Translation-first localization'),
    ('화면 문구는 영어로 바꿨지만 온보딩이 국내 사용자를 전제로 설계되어, 첫 사용자가 제품의 가치를 이해하지 못합니다.',
     'The UI copy is now in English, but onboarding still assumes a Korean user, so first-time users don’t grasp the product’s value.'),
    ('처음 방문한 사용자가 가치를 이해하고 시작할 수 있는가?', 'Can a first-time user understand the value and get started?'),
    ('업무 방식 차이', 'Different ways of working'),
    ('핵심 워크플로가 현지 팀의 역할 분담과 승인 방식에 맞지 않아, 실제 업무에 쓰이지 않습니다.',
     'Core workflows don’t fit how local teams divide roles and handle approvals, so the product isn’t used in day-to-day work.'),
    ('핵심 업무 흐름이 목표 사용자의 실제 업무 방식에 맞는가?', 'Do core workflows match how target users actually work?'),
    ('<h3>구조와 문구</h3>', '<h3>Structure and wording</h3>'),
    ('메뉴 구조와 버튼 문구가 다음 행동을 분명하게 안내하지 못합니다.',
     'Menu structure and button labels don’t make the next step clear.'),
    ('화면의 구조와 문구가 다음 행동을 명확하게 안내하는가?', 'Do the screen structure and wording clearly guide the next action?'),
    ('우선순위 부재', 'No clear priorities'),
    ('고칠 것이 많아 보이지만, 출시 전에 무엇부터 해야 할지 정하지 못합니다.',
     'There seems to be a lot to fix, but the team can’t decide what to tackle first before launch.'),
    ('출시 전에 어떤 UX 문제부터 개선해야 하는가?', 'Which UX problems should be fixed first before launch?'),
    ('위 내용은 자주 나타나는 시행착오 유형을 설명하기 위한 예시입니다.',
     'The examples above illustrate common types of trial and error; they are not specific client cases.'),
    ('팀에 필요한 범위로 함께합니다.', 'We work at the scope your team needs.'),
    ('<span class="k">검토 범위</span>', '<span class="k">Scope</span>'),
    ('<span class="k">결과물</span>', '<span class="k">Deliverable</span>'),
    ('온보딩·핵심 작업·정보 구조·화면 문구', 'Onboarding, core tasks, information architecture, UI copy'),
    ('우선순위를 포함한 UX 진단 보고서', 'UX review report with priorities'),
    ('목표 사용자·업무 방식·현지화 가정', 'Target users, ways of working, localization assumptions'),
    ('상담 및 핵심 권고 요약', 'Consultation and a summary of key recommendations'),
    ('합의한 문제의 설계·프로토타입·개발 협업', 'Design, prototyping, and development collaboration on agreed problems'),
    ('범위에 맞춘 제품 디자인 결과물', 'Product design deliverables matched to the agreed scope'),
    ('복잡한 업무와 새로운 사용 맥락을, 명확한 제품 경험으로.', 'Turning complex work and new contexts of use into clear product experiences.'),
    ('Second Context를 시작하기 전, Rachel Cho가 이전 경력에서 수행한 세 프로젝트입니다. 고객사 이름은 밝히지 않습니다.',
     'Three projects Rachel Cho delivered in previous roles, before starting Second Context. Client names are not disclosed.'),
    # 01 홈헬스케어
    ('미국 홈헬스케어 SaaS의 일정 관리 UX', 'Scheduling UX for a U.S. home healthcare SaaS'),
    ('복잡한 자격 조건·일정 규칙·예외를 사용자가 이해하고 바로 행동할 수 있게 설계했습니다.',
     'Designed complex eligibility conditions, scheduling rules, and exceptions so users could understand them and act right away.'),
    ('내부 규칙과 코드를 그대로 보여주는 대신, 예약 가능한 날짜를 보여주는 달력과 명확한 상태 표시로 다음 행동을 판단할 수 있게 했습니다.',
     'Instead of exposing internal rules and codes, a calendar of bookable dates and clear status indicators let users decide their next step.'),
    ('5.8 <span aria-hidden="true">→</span><span class="sr-only">에서</span> 8.2', '5.8 <span aria-hidden="true">→</span><span class="sr-only"> to </span> 8.2'),
    ('파일럿에서 측정한 일정 계획 자신감', 'Confidence in planning schedules, measured in the pilot'),
    ('180초 <span aria-hidden="true">→</span><span class="sr-only">에서</span> 60초', '180 sec <span aria-hidden="true">→</span><span class="sr-only"> to </span> 60 sec'),
    ('여러 개선이 함께 적용된 후의 작업 시간', 'Task time after several improvements were applied together'),
    ('<p class="metric-value">3,000명 이상</p>', '<p class="metric-value">3,000+</p>'),
    ('AI 일정 추천 경험을 사용하는 임상의', 'Clinicians using the AI scheduling recommendation experience'),
    ('미국 홈헬스케어 운영팀이 임상의 방문 일정을 조정하는 AI 일정 관리 플랫폼입니다. 일정 담당자는 환자 자격·방문 빈도·인력 가용성을 함께 고려해야 했고, 이 과정에서 반복 문의와 혼란이 발생했습니다.',
     'An AI scheduling platform that U.S. home healthcare operations teams use to coordinate clinician visits. Schedulers had to weigh patient eligibility, visit frequency, and staff availability together, which led to repeated questions and confusion.'),
    ('파운딩 디자이너(Senior Product Designer)로 참여했습니다.', 'Joined as the founding designer (Senior Product Designer).'),
    ('CEO와 함께 핵심 AI 일정 플랫폼의 제품 디자인 비전과 전략을 정의하고, 비즈니스 목표를 0→1 단계의 엔드투엔드 디자인 방향으로 옮겼습니다.',
     'Defined the product design vision and strategy for the core AI scheduling platform with the CEO, translating business goals into end-to-end design direction from 0 to 1.'),
    ('CTO, 프런트엔드 엔지니어 6명과 함께 회사의 첫 Figma 디자인 시스템을 만들었습니다.',
     'Built the company’s first Figma design system with the CTO and 6 front-end engineers.'),
    ('디자인·제품·엔지니어링이 함께 쓰는 회사의 첫 엔드투엔드 디자인 프로세스를 만들었습니다.',
     'Established the company’s first end-to-end design process shared by design, product, and engineering.'),
    ('자격·방문 빈도·인력 가용성 규칙이 겹쳐 반복 문의와 혼란이 생겼기 때문에, 규칙을 설명하는 대신 예약 가능한 날짜와 상태를 먼저 보여주도록 했습니다.',
     'Because overlapping eligibility, visit-frequency, and availability rules caused repeated questions and confusion, the design shows bookable dates and status first instead of explaining the rules.'),
    ('내부 코드는 사용자가 이해할 수 있는 문구로 바꿨습니다.', 'Replaced internal codes with wording users could understand.'),
    ('의사결정 속도와 확신을 함께 높이기 위해, AI가 만든 일정 추천을 어떻게 보여주고 검증하고 조정할지 정의했습니다.',
     'To improve both decision speed and confidence, defined how AI-generated schedule recommendations are surfaced, validated, and adjusted.'),
    ('예약 가능한 날짜를 보여주는 달력과 일정 상태 표시', 'A calendar of bookable dates and schedule status indicators'),
    ('내부 코드를 대신하는 화면 문구', 'UI wording that replaces internal codes'),
    ('AI 일정 추천을 확인·검증·조정하는 흐름', 'A flow for reviewing, validating, and adjusting AI schedule recommendations'),
    ('파일럿에서 일정 계획 자신감 5.8 → 8.2', 'Schedule-planning confidence 5.8 → 8.2 in the pilot'),
    ('여러 개선이 함께 적용된 후 작업 시간 180초 → 60초', 'Task time 180 sec → 60 sec after several improvements were applied together'),
    ('AI 보조 일정 워크플로에서 수동 검증 35% 감소', 'Manual validation reduced by 35% in the AI-assisted scheduling workflow'),
    ('임상의 3,000명 이상이 사용하는 일정 추천 경험', 'Scheduling recommendation experience used by 3,000+ clinicians'),
    ('디자인 시스템을 개발자 23명 전원이 조직 표준으로 채택', 'Design system adopted by all 23 developers as the org-wide standard'),
    ('디자인 시스템 도입 후 릴리스 주기 50% 이상 단축', 'Release cycles accelerated by 50%+ after the design system was adopted'),
    # 02 운영 모니터링
    ('글로벌 제약사의 운영 모니터링·인시던트 관리 UX', 'Operations monitoring and incident management UX for a global pharmaceutical company'),
    ('많은 정보 속에서 심각도·영향 범위·조사 우선순위를 연결했습니다.',
     'Connected severity, scope of impact, and investigation priority across a large volume of information.'),
    ('8개 대시보드에 흩어진 정보를 심각도와 후속 영향 중심으로 다시 구조화해, 무엇부터 조사할지 먼저 판단할 수 있게 했습니다.',
     'Restructured information scattered across 8 dashboards around severity and downstream impact, so teams could first decide what to investigate.'),
    ('30분 <span aria-hidden="true">→</span><span class="sr-only">에서</span> 3분', '30 min <span aria-hidden="true">→</span><span class="sr-only"> to </span> 3 min'),
    ('<p class="metric-value">80% 단축</p>', '<p class="metric-value">80% faster</p>'),
    ('의사결정 지원 흐름과 신호 표시를 다시 설계한 뒤의 인시던트 분류(triage) 시간',
     'Incident triage time after redesigning decision-support workflows and signal display'),
    ('<p class="metric-value">40% 단축</p>', '<p class="metric-value">40% faster</p>'),
    ('개발자 내부 도구의 티켓 처리 시간 40% 단축', 'Developer internal-tool ticket processing time reduced by 40%'),
    ('개발자 내부 도구의 티켓 처리 시간', 'Ticket processing time in developers’ internal tools'),
    ('백신 운영을 지원하는 엔터프라이즈 모니터링 플랫폼으로, 제약사 엔지니어링팀이 사용했습니다. 운영 담당자는 인시던트를 조사하기 위해 8개 대시보드를 오가며 심각도와 영향을 파악해야 했습니다.',
     'An enterprise monitoring platform supporting vaccine operations, used by the company’s engineering teams. To investigate an incident, operators had to move between 8 dashboards to work out severity and impact.'),
    ('UX 디자인 에이전시를 통해 계약 Senior Product Designer로 참여했습니다.', 'Joined as a contract Senior Product Designer through a UX design agency.'),
    ('글로벌 IT 기업의 AI/ML 팀과 협업해 생성형 AI 기반 인시던트 관리 시스템을 설계하고, 모델 출력을 엔터프라이즈 사용자가 행동할 수 있는 신호로 바꿨습니다.',
     'Designed a generative-AI incident management system with a global IT company’s AI/ML teams, translating model outputs into actionable signals for enterprise users.'),
    ('이해관계자 인터뷰 15회를 진행해 위험 예측·알림·신뢰도 같은 AI 인사이트를 어떻게 보여주고 우선순위를 정할지 정의했습니다.',
     'Conducted 15 stakeholder interviews to define how AI insights such as risk predictions, alerts, and confidence levels are surfaced and prioritized.'),
    ('담당자가 8개 대시보드를 오가며 심각도와 영향을 직접 맞춰 봐야 했기 때문에, 정보 구조를 심각도와 후속 영향 중심으로 다시 설계했습니다.',
     'Because operators had to piece together severity and impact across 8 dashboards themselves, the information architecture was redesigned around severity and downstream impact.'),
    ('위험 예측·알림·신뢰도를 같은 무게로 나열하지 않고, 조사 우선순위에 따라 보여주는 기준을 정했습니다.',
     'Rather than listing risk predictions, alerts, and confidence levels with equal weight, set criteria for showing them by investigation priority.'),
    ('엔지니어링팀과 성능을 고려한 목록 탐색 방식을 조율했습니다.', 'Aligned with engineering on a list-browsing approach that accounts for performance.'),
    ('심각도와 후속 영향을 중심으로 한 인시던트 조사 흐름', 'An incident investigation flow centered on severity and downstream impact'),
    ('AI 인사이트를 우선순위에 따라 보여주는 의사결정 지원 화면', 'Decision-support screens that surface AI insights by priority'),
    ('성능을 고려한 인시던트 목록 탐색', 'Performance-aware incident list browsing'),
    ('프로젝트에서 보고된 인시던트 조사 시간 30분 → 3분', 'Incident investigation time 30 min → 3 min, as reported in the project'),
    ('프로젝트에서 보고된 인시던트 조사 시간', 'Incident investigation time reported in the project'),
    ('의사결정 지원 흐름 재설계와 신호 명확화 후 인시던트 분류(triage) 시간 80% 단축',
     'Incident triage time reduced by 80% after redesigning decision-support workflows and clarifying signals'),
    ('이해관계자 인터뷰 15회', '15 stakeholder interviews'),
    # 03 한국어 현지화
    ('글로벌 테크 기업의 한국어 제품 현지화', 'Korean product localization for a global tech company'),
    ('언어와 사용 맥락에 맞춰 제품 경험을 조정했습니다.', 'Adapted the product experience to the language and its context of use.'),
    ('번역된 문구에서 멈추지 않고, 이름·날짜·시간 표기와 타이포그래피·간격까지 한국어 사용 맥락에 맞춰 조정했습니다.',
     'Went beyond translated copy, adapting name, date, and time formats as well as typography and spacing to the Korean context of use.'),
    ('<p class="metric-value">6주</p>', '<p class="metric-value">6 weeks</p>'),
    ('2019년, 제작 에이전시와 고객사의 한국·미국 팀이 함께한 현지화 기간',
     'Localization period in 2019, with a production agency and the client’s Korea and U.S. teams'),
    ('5K 디스플레이 데스크톱 제품 관련 콘텐츠를 한국 시장에 맞추는 프로젝트였습니다. 글로벌 브랜드의 표현과 한국어의 자연스러운 문구·레이아웃을 함께 유지해야 했습니다.',
     'A project adapting content for a 5K-display desktop product to the Korean market, keeping the global brand’s expression while making Korean copy and layout read naturally.'),
    ('2019년 6주 동안 영국의 글로벌 제작 에이전시, 고객사의 한국 팀·미국 팀과 협업하며 UX 문구와 디자인 자산을 현지화하고 팀 간 소통을 지원했습니다.',
     'Over 6 weeks in 2019, worked with a global production agency in the U.K. and the client’s Korea and U.S. teams to localize UX copy and design assets and support communication between teams.'),
    ('글로벌 브랜드의 표현과 한국어의 자연스러움을 함께 지켜야 했기 때문에, 문구만 옮기지 않고 이름·날짜·시간 표기 방식까지 한국어 관례에 맞췄습니다.',
     'Because both the global brand’s expression and natural Korean had to be preserved, name, date, and time formats were matched to Korean conventions, not just the copy.'),
    ('같은 이유로 타이포그래피와 간격을 한국어 문장에 맞춰 조정했습니다.', 'For the same reason, typography and spacing were adjusted for Korean text.'),
    ('영국·한국·미국 팀의 관점이 어긋나지 않도록 팀 간 소통을 지원했습니다.', 'Supported communication so the U.K., Korea, and U.S. teams stayed aligned.'),
    ('한국어 UX 문구', 'Korean UX copy'),
    ('이름·날짜·시간 표기', 'Name, date, and time formats'),
    ('한국어 타이포그래피와 간격을 반영한 현지화 레이아웃', 'Localized layouts reflecting Korean typography and spacing'),
    ('한국 시장에 맞춘 UX 문구와 디자인 자산', 'UX copy and design assets tailored to the Korean market'),
    ('<li>현지화 레이아웃</li>', '<li>Localized layouts</li>'),
    # 공통 라벨
    ('<strong>핵심 설계 판단</strong>', '<strong>Key design decision</strong>'),
    ('<summary>사례 자세히 보기</summary>', '<summary>Read the full case</summary>'),
    ('<dt>프로젝트 맥락과 문제</dt>', '<dt>Project context and problem</dt>'),
    ('<dt>Rachel의 역할과 책임</dt>', '<dt>Rachel’s role and responsibilities</dt>'),
    ('<dt>핵심 설계 판단과 이유</dt>', '<dt>Key design decisions and why</dt>'),
    ('<dt>바뀐 화면과 업무 흐름</dt>', '<dt>Screens and workflows changed</dt>'),
    ('<dt>결과</dt>', '<dt>Results</dt>'),
    ('<dt>산출물</dt>', '<dt>Deliverables</dt>'),
    ('<span class="metric-kind">사용자 평가</span>', '<span class="metric-kind">User rating</span>'),
    ('<span class="metric-kind">업무 성과</span>', '<span class="metric-kind">Work outcome</span>'),
    ('<span class="metric-kind">도입 범위</span>', '<span class="metric-kind">Adoption scope</span>'),
    ('<span class="metric-kind">리서치 범위</span>', '<span class="metric-kind">Research scope</span>'),
    ('<span class="metric-kind">프로젝트 기간</span>', '<span class="metric-kind">Project length</span>'),
    ('수치는 각 프로젝트에서 측정·보고된 값이며, 측정 방식은 프로젝트마다 다릅니다.',
     'Figures are as measured and reported in each project; measurement methods differ by project.'),
    ('비슷한 과제를 고민하고 계신가요?', 'Working through a similar challenge?'),
    ('제품과 현재 상황을 함께 살펴보겠습니다.', 'Let’s look at your product and where it stands today.'),
    ('협업 방식 보기', 'See how we work'),
    ('창업자 소개', 'About the founder'),
    ('Rachel Cho의 흑백 인물 사진', 'Black-and-white portrait of Rachel Cho'),
    ('Rachel Cho는 복잡한 B2B 업무의 규칙과 예외를 명확한 제품 경험으로 설계하는 프로덕트 디자이너입니다. 정규직, 계약, 프로젝트 협업 등 여러 형태로 약 12개 글로벌·다국적 기업과 일하며 40개 이상의 프로젝트를 완료했습니다.',
     'Rachel Cho is a product designer who turns the rules and exceptions of complex B2B work into clear product experiences. Working with about 12 global and multinational companies in full-time, contract, and project-based roles, Rachel has completed 40+ projects.'),
    ('헬스케어 SaaS, 엔터프라이즈 운영 시스템, 글로벌 제품 현지화 경험을 바탕으로, Second Context에서는 문제 정의부터 UX 설계와 개발 협업까지 직접 참여합니다.',
     'Drawing on experience in healthcare SaaS, enterprise operations systems, and global product localization, Rachel works hands-on at Second Context, from problem definition through UX design and collaboration with development.'),
    ('aria-label="경력 요약"', 'aria-label="Career summary"'),
    ('<span class="stat-label">완료 프로젝트</span>', '<span class="stat-label">Completed projects</span>'),
    ('<span class="stat-value">약 12개</span><span class="stat-label">글로벌·다국적 기업</span>',
     '<span class="stat-value">About 12</span><span class="stat-label">Global and multinational companies</span>'),
    ('<span class="stat-value">27개국</span><span class="stat-label">여행 · 디지털 노매드 경험</span>',
     '<span class="stat-value">27 countries</span><span class="stat-label">Traveled · Digital nomad experience</span>'),
    ('<p class="metric-value">35% 감소</p>', '<p class="metric-value">35% less</p>'),
    ('AI 보조 일정 워크플로에서의 수동 검증', 'Manual validation in the AI-assisted scheduling workflow'),
    ('제품과 목표 시장, 현재 고민하고 계신 과제를 알려 주세요. 협업할 범위를 함께 살펴보겠습니다.',
     'Tell us about your product, your target market, and the challenges you’re working through. We’ll explore the right scope of collaboration together.'),
]

STEPS = [
    ('시장과 사용 맥락 이해하기', 'Understand the market and context of use'),
    ('제품 경험과 현지화 가정 점검하기', 'Review the product experience and localization assumptions'),
    ('개선 방향과 우선순위 합의하기', 'Agree on direction and priorities'),
    ('현지 맥락에 맞는 경험 설계하기', 'Design for the local context'),
    ('실행 계획과 개발 연결하기', 'Plan execution and connect to development'),
    ('검증하고 다음 개선으로 이어가기', 'Validate and carry into the next iteration'),
]
APPROACH = [
    ('Second Context의 6단계 접근: 시장과 사용 맥락 이해부터 설계, 개발 연결, 검증까지.',
     'Second Context’s six-step approach: from understanding the market and context of use to design, development handoff, and validation.'),
    ('새로운 시장을 이해하고, 제품이 실행할 다음 단계를 설계합니다.',
     'We understand new markets and design the next steps your product will take.'),
    ('모든 협업은 제품의 목표 시장과 사용자, 그리고 현재 팀이 해결해야 할 문제를 이해하는 데서 시작합니다. 현지 사용자의 업무 방식과 기대를 살펴보고, 발견한 차이를 개선 우선순위와 구체적인 디자인으로 연결합니다.',
     'Every engagement starts with understanding your product’s target market and users, and the problems your team needs to solve now. We look at how local users work and what they expect, then turn the gaps we find into improvement priorities and concrete design.'),
    ('Second Context의 6단계 접근은 시장에 대한 가정을 확인하고, 팀이 실행할 수 있는 결과물로 구체화합니다.',
     'Second Context’s six-step approach tests assumptions about the market and turns them into outcomes your team can act on.'),
    ('단계별 설명, 산출물과 기대 효과', 'Step-by-step description, deliverables, and expected outcomes'),
    ('6단계 접근', 'Six-step approach'),
] + STEPS + [(f'{i}단계: ', f'Step {i}: ') for i in range(1, 7)] + [
    ('목표 시장, 핵심 사용자, 업무 환경과 사업 목표를 함께 정리합니다.',
     'Together we define the target market, core users, work environment, and business goals.'),
    ('온보딩, 핵심 업무 흐름, 탐색 구조와 화면 문구를 검토하고 현지 사용자 관점에서 확인할 가정을 찾습니다.',
     'We review onboarding, core workflows, navigation, and UI copy, and identify the assumptions to test from a local user’s perspective.'),
    ('사용자 영향, 사업 중요도, 구현 난이도를 기준으로 먼저 해결할 문제와 목표를 정합니다.',
     'We decide which problems and goals to tackle first, based on user impact, business importance, and implementation effort.'),
    ('합의한 핵심 문제를 중심으로 사용자 흐름, 정보 구조, 화면과 문구를 설계합니다.',
     'Focusing on the agreed core problems, we design user flows, information architecture, screens, and copy.'),
    ('디자인 의도, 요구사항, 고려할 예외 상황과 다음 작업을 정리해 개발 협업으로 연결합니다.',
     'We document design intent, requirements, edge cases to consider, and next tasks, and carry them into development.'),
    ('합의된 범위에서 사용자 피드백이나 사용 데이터를 검토하고 후속 개선 과제를 정리합니다.',
     'Within the agreed scope, we review user feedback or usage data and define follow-up improvements.'),
    ('<dt>산출물</dt>', '<dt>Deliverable</dt>'),
    ('<dt>기대 효과</dt>', '<dt>Expected outcome</dt>'),
    ('시장·사용 맥락 브리프', 'Market and context-of-use brief'),
    ('검토할 문제와 협업 범위 명확화', 'Clarity on the problems to review and the scope of collaboration'),
    ('UX 진단 및 현지화 가정 목록', 'UX review and list of localization assumptions'),
    ('제품 경험의 마찰과 검증 과제 파악', 'Friction in the product experience and items to validate, identified'),
    ('우선순위 매트릭스 및 디자인 방향', 'Priority matrix and design direction'),
    ('팀의 시간과 자원을 집중할 기준 마련', 'Clear criteria for where to focus your team’s time and resources'),
    ('개선 사용자 흐름 및 합의 범위의 디자인·프로토타입', 'Improved user flows, plus designs and prototypes within the agreed scope'),
    ('제품 방향을 구체적인 경험으로 확인', 'Product direction confirmed as a concrete experience'),
    ('디자인 전달 자료 및 실행 계획', 'Design handoff materials and an execution plan'),
    ('구현 과정의 불확실성과 해석 차이 감소', 'Less uncertainty and fewer misinterpretations during implementation'),
    ('검증 결과 및 후속 개선 백로그', 'Validation results and a follow-up improvement backlog'),
    ('근거를 바탕으로 한 다음 제품 의사결정 지원', 'Evidence-based support for your next product decisions'),
    ('전체 과정과 제공물은 협업 범위에 따라 달라집니다. 짧은 상담이나 UX 진단은 필요한 단계에 집중하며, 사용자 리서치·프로토타입·개발 지원·후속 검증은 별도 합의된 범위에서 진행합니다.',
     'The overall process and deliverables depend on the scope of the engagement. Short consultations and UX reviews focus on the steps you need; user research, prototyping, development support, and follow-up validation are carried out within a separately agreed scope.'),
    ('팀의 판단과 실행을 돕는 제품 디자인.', 'Product design that supports your team’s decisions and execution.'),
    ('명확한 개선 우선순위', 'Clear improvement priorities'),
    ('먼저 해결할 문제와 그 이유를 정리합니다.', 'We define which problems to solve first, and why.'),
    ('현지 사용자에 대한 이해', 'Understanding of local users'),
    ('사용자의 기대와 실제 업무 맥락을 제품 판단에 반영합니다.', 'We bring users’ expectations and real work context into product decisions.'),
    ('원활한 디자인·개발 협업', 'Smooth design and development collaboration'),
    ('합의한 방향을 구현 가능한 요구사항과 디자인으로 연결합니다.', 'We turn the agreed direction into buildable requirements and designs.'),
    ('검증을 통한 지속적인 개선', 'Continuous improvement through validation'),
    ('피드백과 사용 근거를 다음 개선 과제로 이어갑니다.', 'We carry feedback and usage evidence into the next round of improvements.'),
]

CONTACT = [
    ('Second Context에 프로젝트를 문의하거나 30분 상담을 예약하세요.',
     'Send Second Context a project inquiry or book a 30-minute consultation.'),
    ('<h1>제품의 어떤 부분을 개선하고 싶으신가요?</h1>', '<h1>What would you like to improve in your product?</h1>'),
    ('<p class="lead">제품과 현재 고민을 간단히 알려주세요. 프로젝트 범위가 아직 정해지지 않았어도 괜찮습니다.</p>',
     '<p class="lead">Tell us briefly about your product and what you’re working through. It’s fine if the project scope isn’t defined yet.</p>'),
    ('<h2 class="label">이메일로 문의하기</h2>', '<h2 class="label">Email</h2>'),
    ('>이메일 주소 복사</button>', '>Copy email</button>'),
    ('이메일 주소 (선택해서 복사)', 'Email address (select to copy)'),
    ('<h2 class="label">30분 상담 예약</h2>', '<h2 class="label">30-minute consultation</h2>'),
    ('글보다 대화가 편하시다면 30분 상담에서 제품과 현재 과제를 함께 살펴보겠습니다.',
     'If you’d rather talk than write, we can look at your product and current challenges together in a 30-minute consultation.'),
    ('30분 상담 예약하기<span class="sr-only"> (새 탭에서 열림)</span></a>\n            </div>',
     'Book a 30-minute consultation<span class="sr-only"> (새 탭에서 열림)</span></a>\n            </div>'),
    ('<h2 class="label" id="inquiry-title">문의 남기기</h2>', '<h2 class="label" id="inquiry-title">Send an inquiry</h2>'),
    ('</span> 필수 항목</p>', '</span> Required</p>'),
    ('<label for="f-name">이름 ', '<label for="f-name">Name '),
    ('<label for="f-email">이메일 ', '<label for="f-email">Email '),
    ('<label for="f-company">회사 또는 제품명</label>', '<label for="f-company">Company or product name</label>'),
    ('<label for="f-url">제품 URL</label>', '<label for="f-url">Product URL</label>'),
    ('<label for="f-message">문의 내용 ', '<label for="f-message">Message '),
    ('어떤 제품인지, 현재 어려운 점과 필요한 도움을 알려주세요. 희망 일정이 있다면 함께 적어주세요.',
     'Tell us what the product is, what’s difficult right now, and what help you need. If you have a preferred timeline, include it too.'),
    ('온라인 문의 전송이 아직 연결되지 않아 문의 보내기 버튼을 사용할 수 없습니다. 이메일이나 30분 상담 예약을 이용해 주세요.',
     'Online inquiries aren’t connected yet, so the Send inquiry button is unavailable. Please use email or book a 30-minute consultation.'),
    ('>문의 보내기</button>', '>Send inquiry</button>'),
]

PATHS = [
    ('href="favicon.ico"', 'href="../favicon.ico"'),
    ('href="assets/', 'href="../assets/'),
    ('src="assets/', 'src="../assets/'),
    ('src="./rachel-portrait-bw.png"', 'src="../rachel-portrait-bw.png"'),
]

TABLE = {PAGES[0]: HOME, PAGES[1]: APPROACH, PAGES[2]: CONTACT}

for page in PAGES:
    s = prep_korean(page)
    e = s.replace(f'<link rel="canonical" href="{BASE + page}">', f'<link rel="canonical" href="{BASE}en/{page}">')
    e = e.replace(lang_nav(page, "ko"), lang_nav(page, "en"))
    # 페이지 표 먼저(긴 문장), 그다음 공통 문구
    for ko, en in TABLE[page] + COMMON + PATHS:
        if page == PAGES[2] and ko == 'Rachel과 Book a 30-minute call':
            continue
        # 페이지별 표의 문구는 반드시 있어야 한다. 공통 문구·경로는 페이지에 있을 때만 바꾼다
        assert ko not in dict(TABLE[page]) or e.count(ko) >= 1, (page, ko[:50])
        e = e.replace(ko, en)
    if page == PAGES[2]:
        e = e.replace('Rachel과 Book a 30-minute call', 'Book a 30-minute call with Rachel')
    # 한국어 작업 메모 주석은 영어 페이지에 옮기지 않는다 (화면에 보이지 않음)
    e = re.sub(r'[ \t]*<!--[^>]*[가-힣][^>]*-->\n', '', e)
    left = [m for m in re.findall(r'[^<>"]*[가-힣][^<>"]*', e) if m.strip() != '한국어']
    assert not left, (page, left)
    os.makedirs(os.path.join(R, 'en'), exist_ok=True)
    open(os.path.join(R, 'en', page), 'w', encoding='utf-8').write(e)
    print('built en/' + page)
