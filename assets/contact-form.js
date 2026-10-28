/* Second Context Contact: 문의 폼 검증·전송 상태, 이메일 주소 복사.
   전송 주소는 form의 data-endpoint에 넣는다. 비어 있으면 제출 버튼을 비활성화한 채로 두고 전송하지 않는다.
   비밀키는 이 파일이나 HTML에 넣지 않는다 (공개 저장소). */
(function () {
  var ko = document.documentElement.lang === 'ko';
  var EMAIL = 'rachel.cho5257@gmail.com';

  /* ---------- 이메일 주소 복사 ---------- */
  var copyBtn = document.querySelector('[data-copy-email]');
  if (copyBtn) {
    var copyStatus = document.getElementById('copy-status');
    var fallback = document.getElementById('copy-fallback');
    var manual = document.getElementById('email-manual');
    var C = ko ? {
      ok: '이메일 주소를 복사했습니다.',
      fail: '자동 복사를 사용할 수 없습니다. 아래 칸의 주소를 선택해 직접 복사해 주세요.'
    } : {
      ok: 'Email address copied.',
      fail: 'Couldn’t copy automatically. Please select and copy the address in the box below.'
    };
    var showFallback = function () {
      copyStatus.textContent = C.fail;
      fallback.hidden = false;
      manual.focus();
      manual.select();
    };
    copyBtn.addEventListener('click', function () {
      copyStatus.textContent = '';
      var address = copyBtn.getAttribute('data-copy-email');
      if (!navigator.clipboard || !window.isSecureContext) { showFallback(); return; }
      // 클립보드 쓰기가 실제로 성공했을 때만 완료 안내
      navigator.clipboard.writeText(address).then(function () {
        fallback.hidden = true;
        copyStatus.textContent = C.ok;
      }, showFallback);
    });
  }

  /* ---------- 문의 폼 ---------- */
  var form = document.getElementById('inquiry');
  if (!form) return;

  var T = ko ? {
    names: { name: '이름', email: '이메일', message: '문의 내용' },
    url: 'URL 형식이 올바르지 않습니다. example.com 형태로 입력해 주세요.',
    sendingLabel: '보내는 중…',
    prefix: '오류: ',
    required: function (n) { return n + ' 항목을 입력해 주세요.'; },
    email: '이메일 형식이 올바르지 않습니다. name@company.com 형태로 입력해 주세요.',
    summary: function (c) { return '입력 내용을 확인해 주세요. 수정이 필요한 항목이 ' + c + '개 있습니다.'; },
    notConnected: '전송되지 않음: 온라인 문의 접수가 아직 연결되지 않았습니다. 작성하신 내용은 그대로 남아 있으니 ' + EMAIL + '으로 보내 주세요.',
    sending: '문의를 보내는 중입니다…',
    success: '전송 완료: 문의가 접수되었습니다. 감사합니다.',
    failure: '전송 실패: 문의를 보내지 못했습니다. 작성하신 내용은 그대로 남아 있으니 문의 보내기를 다시 눌러 주세요. 계속 실패하면 ' + EMAIL + '으로 보내 주세요.'
  } : {
    names: { name: 'your name', email: 'your email address', message: 'your message' },
    url: 'This URL isn’t valid. Please use a format like example.com.',
    sendingLabel: 'Sending…',
    prefix: 'Error: ',
    required: function (n) { return 'Please fill in ' + n + '.'; },
    email: 'This email address isn’t valid. Please use a format like name@company.com.',
    summary: function (c) { return 'Please check the form. ' + c + (c === 1 ? ' field needs' : ' fields need') + ' your attention.'; },
    notConnected: 'Not sent: online inquiries aren’t connected yet. Your message is still in the form—please send it to ' + EMAIL + '.',
    sending: 'Sending your inquiry…',
    success: 'Sent: your inquiry has been received. Thank you.',
    failure: 'Not sent: something went wrong. Your message is still in the form—please select Send inquiry again. If it keeps failing, email ' + EMAIL + '.'
  };

  var status = form.querySelector('.form-status');
  var button = form.querySelector('button[type="submit"]');
  var fields = Array.prototype.slice.call(form.querySelectorAll('.field input, .field textarea'));
  var endpoint = (form.getAttribute('data-endpoint') || '').trim();
  var sending = false;

  // 전송 주소가 연결되면 비활성 안내를 숨기고 버튼을 켠다
  if (endpoint) {
    var pending = form.querySelector('.form-pending');
    if (pending) pending.hidden = true;
    button.disabled = false;
    button.removeAttribute('aria-describedby');
  }

  function setError(el, msg) {
    var err = document.getElementById(el.id + '-error');
    if (msg) {
      err.textContent = T.prefix + msg;
      err.hidden = false;
      el.setAttribute('aria-invalid', 'true');
    } else {
      err.textContent = '';
      err.hidden = true;
      el.removeAttribute('aria-invalid');
    }
  }

  function check(el) {
    var v = el.value.trim();
    var msg = '';
    // 제품 URL은 https:// 없이 적어도 받는다 (example.com → https://example.com)
    if (el.type === 'url' && v && !/^[a-z][a-z0-9+.-]*:\/\//i.test(v)) { el.value = 'https://' + v; }
    if (el.required && !v) msg = T.required(T.names[el.name] || el.name);
    else if (el.type === 'email' && v && el.validity.typeMismatch) msg = T.email;
    // 브라우저 검사는 공백 섞인 주소도 통과시키므로, 공백 없음과 도메인 점(.)을 함께 확인한다
    else if (el.type === 'url' && v && (el.validity.typeMismatch || !/^[a-z][a-z0-9+.-]*:\/\/[^\/\s.]+\.[^\/\s]+(\/\S*)?$/i.test(el.value.trim()))) msg = T.url;
    setError(el, msg);
    return !msg;
  }

  function setStatus(text, state) {
    status.textContent = text;
    status.setAttribute('data-state', state || '');
  }

  // 처음 제출한 뒤에는 항목을 벗어날 때마다 다시 확인한다
  fields.forEach(function (el) {
    el.addEventListener('blur', function () {
      if (el.hasAttribute('aria-invalid')) check(el);
    });
  });

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    if (sending) return;

    var invalid = fields.filter(function (el) { return !check(el); });
    if (invalid.length) {
      setStatus(T.summary(invalid.length), 'error');
      invalid[0].focus();
      return;
    }

    if (!endpoint) {
      setStatus(T.notConnected, 'error');
      return;
    }

    // 전송 중에는 다시 누를 수 없게 하고, 응답이 오면 버튼을 되돌린다
    sending = true;
    var label = button.textContent;
    button.setAttribute('aria-disabled', 'true');
    button.textContent = T.sendingLabel;
    setStatus(T.sending, 'sending');

    fetch(endpoint, {
      method: 'POST',
      body: new FormData(form),
      headers: { Accept: 'application/json' }
    }).then(function (res) {
      if (!res.ok) throw new Error('HTTP ' + res.status);
      // 서버가 성공(2xx)을 돌려준 뒤에만 입력을 비운다
      form.reset();
      fields.forEach(function (el) { setError(el, ''); });
      setStatus(T.success, 'success');
    }).catch(function () {
      setStatus(T.failure, 'error');
    }).then(function () {
      sending = false;
      button.textContent = label;
      button.removeAttribute('aria-disabled');
    });
  });
})();
