/* Second Context 예약·결제 설정 (2026-11-16, 로컬 초안). 예약 주소는 이 파일 한곳에서만 바꾼다.
   - freeConsultUrl: 무료 30분 상담(Calendly). 상담 언어(한국어/영어) 질문은 Calendly 이벤트 설정에서 추가해야 한다
   - paidReviewUrl: 유료 60분 집중 UX 리뷰(Calendly 유료 이벤트 + Stripe). 아직 없음 → 비워 둔다.
     비어 있으면 페이지는 '리뷰 신청 문의'(문의 폼, 리뷰 미리 선택)와 '온라인 결제 연결 준비 중' 안내를 보여 준다.
     주소를 넣으면 [data-paid-review-link] 버튼이 그 주소로 보이고, 준비 중 안내([data-paid-pending])는 숨는다.
   무료 상담 링크를 paidReviewUrl에 넣지 않는다. 가짜 결제 링크·결제 성공 상태를 만들지 않는다. */
window.SC_BOOKING = {
  freeConsultUrl: 'https://calendly.com/yeagyeong/meeting-with-rachel-cho',
  paidReviewUrl: ''
};

(function () {
  var url = (window.SC_BOOKING.paidReviewUrl || '').trim();
  // 무료 상담 주소가 잘못 들어가면 유료 버튼을 켜지 않는다
  if (!url || url === window.SC_BOOKING.freeConsultUrl) return;
  document.addEventListener('DOMContentLoaded', function () {
    Array.prototype.forEach.call(document.querySelectorAll('[data-paid-review-link]'), function (a) {
      a.href = url;
      a.hidden = false;
    });
    Array.prototype.forEach.call(document.querySelectorAll('[data-paid-pending]'), function (el) { el.hidden = true; });
    Array.prototype.forEach.call(document.querySelectorAll('[data-paid-ready]'), function (el) { el.hidden = false; });
  });
})();
