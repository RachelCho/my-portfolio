/* Second Context 문의 폼: 입력 검증, 오류 안내, 전송 상태 알림.
   전송 주소는 form의 data-endpoint에 넣는다. 비어 있으면 전송하지 않고 "연결 전" 안내만 보여 준다.
   비밀키는 이 파일이나 HTML에 넣지 않는다 (공개 저장소). */
(function () {
  var form = document.getElementById('inquiry');
  if (!form) return;

  var ko = document.documentElement.lang === 'ko';
  var EMAIL = 'rachel.cho5257@gmail.com';
  var T = ko ? {
    names: { name: '이름', email: '이메일', message: '문의 내용' },
    prefix: '오류: ',
    required: function (n) { return n + ' 항목을 입력해 주세요.'; },
    email: '이메일 형식이 올바르지 않습니다. name@company.com 형태로 입력해 주세요.',
    summary: function (c) { return '입력 내용을 확인해 주세요. 수정이 필요한 항목이 ' + c + '개 있습니다.'; },
    notConnected: '전송되지 않음: 온라인 문의 접수가 아직 연결되지 않았습니다. 작성하신 내용은 그대로 남아 있으니 ' + EMAIL + '으로 보내 주세요.',
    sending: '문의를 보내는 중입니다…',
    success: '전송 완료: 문의가 접수되었습니다. 감사합니다.',
    failure: '전송 실패: 문의를 보내지 못했습니다. 작성하신 내용은 그대로 남아 있습니다. 잠시 후 다시 시도하시거나 ' + EMAIL + '으로 보내 주세요.'
  } : {
    names: { name: 'your name', email: 'your email address', message: 'your message' },
    prefix: 'Error: ',
    required: function (n) { return 'Please fill in ' + n + '.'; },
    email: 'This email address isn’t valid. Please use a format like name@company.com.',
    summary: function (c) { return 'Please check the form. ' + c + (c === 1 ? ' field needs' : ' fields need') + ' your attention.'; },
    notConnected: 'Not sent: online inquiries aren’t connected yet. Your message is still in the form—please send it to ' + EMAIL + '.',
    sending: 'Sending your inquiry…',
    success: 'Sent: your inquiry has been received. Thank you.',
    failure: 'Not sent: something went wrong. Your message is still in the form. Please try again later or send it to ' + EMAIL + '.'
  };

  var status = form.querySelector('.form-status');
  var button = form.querySelector('button[type="submit"]');
  var fields = Array.prototype.slice.call(form.querySelectorAll('input, textarea'));
  var endpoint = (form.getAttribute('data-endpoint') || '').trim();
  var sending = false;

  var pending = form.querySelector('.form-pending');
  if (pending && endpoint) pending.hidden = true;

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
    if (el.required && !v) msg = T.required(T.names[el.name] || el.name);
    else if (el.type === 'email' && v && el.validity.typeMismatch) msg = T.email;
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

    sending = true;
    button.setAttribute('aria-disabled', 'true');
    setStatus(T.sending, 'sending');

    fetch(endpoint, {
      method: 'POST',
      body: new FormData(form),
      headers: { Accept: 'application/json' }
    }).then(function (res) {
      if (!res.ok) throw new Error('HTTP ' + res.status);
      form.reset();
      setStatus(T.success, 'success');
    }).catch(function () {
      setStatus(T.failure, 'error');
    }).then(function () {
      sending = false;
      button.removeAttribute('aria-disabled');
    });
  });
})();
