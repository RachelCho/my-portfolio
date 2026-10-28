/* Second Context 사례 인터랙션: 단계 버튼, 모션 재생·정지·다시 보기.
   - 사례마다 상태를 따로 가진다 (한 사례의 단계·재생이 다른 사례에 영향을 주지 않음)
   - 재생은 사용자가 눌렀을 때만 시작하고, 마지막 단계에서 한 번 멈춘다
   - 화면 요소: data-show="2 3"(그 단계에서만 보임), data-hl="1"(그 단계에서 강조), data-pick="2"(그 단계에서 선택됨)
   - 언어 전환 뒤 단계를 되살릴 때는 lang.js가 'sc:step' 이벤트를 보낸다 */
(function () {
  var STEP_MS = 2600;

  function has(attr, n) { return (' ' + (attr || '') + ' ').indexOf(' ' + n + ' ') !== -1; }

  Array.prototype.forEach.call(document.querySelectorAll('[data-demo]'), function (demo) {
    var steps = Array.prototype.slice.call(demo.querySelectorAll('.demo-step'));
    var total = steps.length;
    var play = demo.querySelector('[data-play]');
    var stop = demo.querySelector('[data-stop]');
    var replay = demo.querySelector('[data-replay]');
    var timer = null;

    function setStep(n) {
      n = Math.max(1, Math.min(total, n));
      demo.setAttribute('data-step', String(n));
      steps.forEach(function (b) {
        if (+b.getAttribute('data-go') === n) b.setAttribute('aria-current', 'step');
        else b.removeAttribute('aria-current');
      });
      Array.prototype.forEach.call(demo.querySelectorAll('[data-show]'), function (el) { el.hidden = !has(el.getAttribute('data-show'), n); });
      Array.prototype.forEach.call(demo.querySelectorAll('[data-hl]'), function (el) { el.classList.toggle('is-hl', has(el.getAttribute('data-hl'), n)); });
      Array.prototype.forEach.call(demo.querySelectorAll('[data-pick]'), function (el) { el.classList.toggle('is-pick', has(el.getAttribute('data-pick'), n)); });
      Array.prototype.forEach.call(demo.querySelectorAll('[data-rec]'), function (el) { el.classList.toggle('is-rec', has(el.getAttribute('data-rec'), n)); });
      Array.prototype.forEach.call(demo.querySelectorAll('[data-note]'), function (el) { el.hidden = +el.getAttribute('data-note') !== n; });
    }

    function current() { return +demo.getAttribute('data-step') || 1; }

    function halt() {
      if (timer) { clearTimeout(timer); timer = null; }
      demo.classList.remove('is-playing');
      play.disabled = false;
      stop.disabled = true;
    }

    function tick() {
      if (current() >= total) { halt(); return; }
      setStep(current() + 1);
      timer = setTimeout(tick, STEP_MS);
    }

    function start(from) {
      halt();
      if (from) setStep(from);
      else if (current() >= total) setStep(1);
      demo.classList.add('is-playing');
      play.disabled = true;
      stop.disabled = false;
      stop.focus();
      timer = setTimeout(tick, STEP_MS);
    }

    steps.forEach(function (b) {
      b.addEventListener('click', function () { halt(); setStep(+b.getAttribute('data-go')); });
    });
    // 단계 버튼은 좌우 화살표로도 이동한다
    demo.querySelector('.demo-steps').addEventListener('keydown', function (e) {
      if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
      var i = steps.indexOf(document.activeElement);
      if (i === -1) return;
      e.preventDefault();
      var next = steps[(i + (e.key === 'ArrowRight' ? 1 : total - 1)) % total];
      next.focus();
      next.click();
    });
    play.addEventListener('click', function () { start(); });
    stop.addEventListener('click', function () { halt(); play.focus(); });
    replay.addEventListener('click', function () { start(1); });
    demo.addEventListener('sc:step', function (e) { halt(); setStep(+e.detail || 1); });

    setStep(current());
  });
})();
