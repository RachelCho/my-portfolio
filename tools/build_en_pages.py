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
    ('서로 다른 시장과 업무 환경에 맞는 제품 경험.', 'Product experiences that fit different markets and ways of working.'),
    ('홈 헬스케어 운영부터 산업용 IoT 모니터링, 글로벌 제품 현지화까지. 실제 프로젝트 경험을 바탕으로 Second Context가 함께 해결할 수 있는 상황을 소개합니다.',
     'From home healthcare operations to industrial IoT monitoring and global product localization. Drawing on real project experience, here are situations Second Context can help you work through.'),
    ('복잡한 방문 일정과 현장 업무를 연결합니다.', 'Connecting complex visit schedules with work in the field.'),
    ('재택 의료 서비스를 운영하는 팀은 환자의 서비스 자격, 방문 빈도와 의료진의 가용성을 함께 고려해 일정을 계획해야 합니다.',
     'Teams running home healthcare services have to plan schedules around patients’ service eligibility, visit frequency, and clinician availability all at once.'),
    ('예약 조건과 일정 상태가 명확하지 않으면, 운영자와 의료진은 추가 확인을 반복하며 업무를 진행하게 됩니다.',
     'When booking conditions and schedule status aren’t clear, coordinators and clinicians have to keep double-checking as they work.'),
    ('실제 일정 계획 과정을 살펴보고, 예약 가능 여부와 예외 상황을 이해하기 쉬운 정보와 업무 흐름으로 설계합니다.',
     'We look at how schedules are actually planned, and design information and workflows that make availability and exceptions easy to understand.'),
    ('명확한 일정 판단', 'Clearer scheduling decisions'),
    ('반복 확인 감소', 'Fewer repeated checks'),
    ('운영자와 현장 의료진의 정보 연결', 'Connected information between coordinators and field clinicians'),
    ('운영 데이터를 대응 우선순위로 연결합니다.', 'Turning operational data into response priorities.'),
    ('산업용 IoT와 모니터링 환경에서는 여러 시스템의 상태와 알림을 함께 살피며, 어떤 문제에 먼저 대응할지 판단해야 합니다.',
     'In industrial IoT and monitoring environments, teams watch the status and alerts of many systems at once and have to decide which problem to respond to first.'),
    ('정보가 여러 화면에 분산되어 있으면 문제의 심각도와 다른 시스템에 미치는 영향을 파악하는 데 시간이 걸립니다.',
     'When information is spread across many screens, it takes time to understand how severe a problem is and how it affects other systems.'),
    ('운영자의 조사·대응 흐름을 중심으로 정보 위계와 탐색 구조를 정리하고, 중요한 신호와 관련 맥락을 함께 확인할 수 있도록 설계합니다.',
     'We organize information hierarchy and navigation around how operators investigate and respond, so critical signals can be reviewed together with their context.'),
    ('빠른 문제 파악', 'Faster problem identification'),
    ('명확한 대응 우선순위', 'Clearer response priorities'),
    ('연결된 조사 흐름', 'A connected investigation flow'),
    ('글로벌 제품을 현지 사용자에게 자연스럽게 연결합니다.', 'Connecting global products naturally with local users.'),
    ('글로벌 제품을 한국 시장에 선보일 때는 브랜드의 일관성과 함께 한국어 표현, 날짜·시간 표기와 타이포그래피를 고려해야 합니다.',
     'Bringing a global product to the Korean market means considering Korean phrasing, date and time formats, and typography alongside brand consistency.'),
    ('원문의 의미가 전달되더라도 문구와 화면 구성이 현지 사용자의 기대와 어긋나면 제품을 이해하는 과정에 마찰이 생깁니다.',
     'Even when the original meaning comes across, copy and layouts that miss local users’ expectations create friction in understanding the product.'),
    ('글로벌·현지 팀의 관점을 연결하고, UX 문구와 정보 위계, 글자와 간격을 현지 사용 맥락에 맞춰 조정합니다.',
     'We bridge the perspectives of global and local teams, and adapt UX copy, information hierarchy, type, and spacing to the local context of use.'),
    ('자연스러운 제품 이해', 'Natural product understanding'),
    ('일관된 브랜드 표현', 'Consistent brand expression'),
    ('현지 맥락에 맞는 사용 경험', 'A user experience that fits the local context'),
    ('<dt>상황</dt>', '<dt>Situation</dt>'),
    ('<dt>해결할 간극</dt>', '<dt>The gap</dt>'),
    ('<dt>Second Context의 역할</dt>', '<dt>Second Context’s role</dt>'),
    ('<dt>기대 효과</dt>\n            <dd>\n', '<dt>Expected outcomes</dt>\n            <dd>\n'),
    ('비슷한 과제를 고민하고 계신가요?', 'Working through a similar challenge?'),
    ('제품과 현재 상황을 함께 살펴보겠습니다.', 'Let’s look at your product and where it stands today.'),
    ('협업 방식 보기', 'See how we work'),
    ('창업자 소개', 'About the founder'),
    ('Rachel Cho의 흑백 인물 사진', 'Black-and-white portrait of Rachel Cho'),
    ('새로운 세계에서 스스로 길을 찾아온 경험을, 사람과 제품의 다음 가능성으로 연결합니다.',
     'I connect my experience of finding my own way in new worlds to the next possibilities for people and products.'),
    ('경제적으로 넉넉하지 않았던 어린 시절, 해외 유학은 상상하기조차 어려운 일이었습니다. 그런 제가 직접 27개국을 여행하고 현지 사람들과 생활하며, 국경을 넘어 일하는 디지털 노매드가 되었습니다. 낯선 환경에 들어가 배우고 관계를 쌓으며, 제게 가능한 선택지를 하나씩 넓혀 왔습니다.',
     'Growing up without much money, I could hardly imagine studying abroad. Since then, I have traveled to 27 countries, lived alongside local people, and become a digital nomad working across borders. By stepping into unfamiliar places, learning, and building relationships, I have widened the choices open to me one step at a time.'),
    ('그 과정에서 12개 이상의 글로벌 기업을 위한 주요 프로젝트를 이끌고, 1,500만 달러의 투자를 유치한 Y Combinator 출신 스타트업에서 파운딩 디자이너로 일했습니다. 글로벌 기업의 복잡한 협업부터 초기 스타트업의 빠른 의사결정까지 경험하며, 서로 다른 환경에서 제품의 방향을 정하고 실행하는 일을 해왔습니다.',
     'Along the way, I have led key projects for more than 12 global companies and worked as the founding designer at a Y Combinator startup that raised $15 million. From complex collaboration at global enterprises to fast decision-making at early-stage startups, I have set product direction and carried it through in very different environments.'),
    ('이 여정은 현지화를 바라보는 제 관점을 만들었습니다. 같은 제품도 사용자의 문화, 업무 방식, 기대에 따라 다르게 받아들여집니다. 새로운 시장에서 제품의 가치를 전달하려면 사람들이 어떻게 판단하고, 무엇을 신뢰하며, 실제로 어떤 방식으로 일하는지 이해해야 합니다.',
     'This journey shaped how I see localization. The same product is received differently depending on users’ culture, ways of working, and expectations. To deliver a product’s value in a new market, you need to understand how people make decisions, what they trust, and how they actually work.'),
    ('Second Context는 이러한 이해를 한국 기업의 글로벌 확장에 연결하기 위해 시작하였습니다. 특히 미국 시장을 준비하는 B2B SaaS 팀을 대상으로 제품 UX 진단, 현지화 방향 검토, 개선 우선순위 수립과 실제 디자인을 지원합니다. 스타트업 전략 코치로서는 팀이 목표 사용자와 핵심 문제를 명확히 하고, 다음에 집중할 제품 과제를 구체화하도록 돕습니다.',
     'I started Second Context to bring this understanding to Korean companies expanding globally. In particular, I support B2B SaaS teams preparing for the U.S. market with product UX reviews, localization direction reviews, improvement priorities, and hands-on design. As a startup strategy coach, I help teams clarify their target users and core problems and define the product work to focus on next.'),
    ('사람들의 새로운 출발을 돕는 일도 이어가고 있습니다. 이민자와 유학 준비자들이 비자와 학교 선택, 해외 정착과 커리어의 연결을 고민할 때 제 경험을 나누고, 디자이너들에게는 전략적인 커리어 설계와 해외 취업을 위한 멘토링을 제공합니다. 또한 디자이너 소셜 모임을 기획하고 운영하며, 서로 다른 경험을 가진 사람들이 지식과 기회를 나누는 자리를 만들고 있습니다.',
     'I also continue to help people make new starts. When immigrants and prospective international students are thinking through visas, school choices, settling abroad, and how it all connects to their careers, I share my own experience. For designers, I offer mentoring on strategic career planning and finding work abroad. I also plan and host social gatherings for designers, creating spaces where people with different backgrounds share knowledge and opportunities.'),
    ('스스로의 가능성을 넓혀 온 경험을 바탕으로, 이제는 사람과 제품이 새로운 시장에서 자신만의 자리를 찾도록 돕고자 합니다.',
     'Drawing on the experience of widening my own possibilities, I now want to help people and products find their own place in new markets.'),
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
    ('<h1>프로젝트 이야기를 들려주세요.</h1>', '<h1>Tell us about your project.</h1>'),
    ('<p class="lead">제품과 목표 시장, 현재 고민하고 계신 과제를 알려 주세요.</p>',
     '<p class="lead">Tell us about your product, your target market, and the challenges you’re working through.</p>'),
    ('aria-label="프로젝트 문의"', 'aria-label="Project inquiry"'),
    ('</span> 필수 항목</p>', '</span> Required</p>'),
    ('<label for="f-name">이름 ', '<label for="f-name">Name '),
    ('<label for="f-org">회사·팀</label>', '<label for="f-org">Organisation</label>'),
    ('<label for="f-email">이메일 ', '<label for="f-email">Email '),
    ('<label for="f-phone">전화번호</label>', '<label for="f-phone">Phone number</label>'),
    ('<label for="f-message">문의 내용 ', '<label for="f-message">How can I help? '),
    ('제품, 목표 시장, 현재 과제와 희망 일정을 알려 주세요.', 'Tell us about your product, target market, current challenges, and preferred timeline.'),
    ('온라인 문의 전송이 아직 연결되지 않아 문의 보내기 버튼을 사용할 수 없습니다. Direct contact의 이메일(주소 복사·Gmail 작성)이나 30분 상담 예약을 이용해 주세요.',
     'Online inquiries aren’t connected yet, so the Send inquiry button is unavailable. Please use the email under Direct contact (copy the address or compose in Gmail) or book a 30-minute consultation.'),
    ('>이메일 주소 복사</button>', '>Copy email</button>'),
    ('Gmail에서 작성<span', 'Compose in Gmail<span'),
    ('이메일 주소 (선택해서 복사)', 'Email address (select to copy)'),
    ('>문의 보내기</button>', '>Send inquiry</button>'),
    ('aria-label="연락 안내"', 'aria-label="Contact details"'),
    ('<dt>이메일</dt>', '<dt>Email</dt>'),
    ('먼저 이야기 나누고 싶으신가요?', 'Would you like to talk first?'),
    ('30분 상담에서 제품과 현재 과제를 함께 살펴보겠습니다.', 'In a 30-minute consultation, we’ll look at your product and current challenges together.'),
    ('30분 상담 예약하기<span class="sr-only"> (새 탭에서 열림)</span></a>\n          </div>',
     'Book a 30-minute consultation<span class="sr-only"> (새 탭에서 열림)</span></a>\n          </div>'),
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
