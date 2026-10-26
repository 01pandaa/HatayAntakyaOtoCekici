// Ersan Oto Kurtarma — main.js
(function () {
  var header = document.querySelector('.header');
  var btn = document.querySelector('.menu-btn');
  if (btn && header) {
    btn.addEventListener('click', function () {
      var open = header.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  // Mobilde açılır menüler
  document.querySelectorAll('.has-drop > a').forEach(function (a) {
    a.addEventListener('click', function (e) {
      if (window.innerWidth <= 1240) {
        var li = a.parentElement;
        if (!li.classList.contains('open')) { e.preventDefault(); li.classList.add('open'); }
      }
    });
  });
  // Yıl
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // Konumu WhatsApp ile gönder
  var PHONE = '905520803450';
  document.querySelectorAll('[data-send-location]').forEach(function (b) {
    b.addEventListener('click', function (e) {
      e.preventDefault();
      var fallback = 'https://wa.me/' + PHONE + '?text=' + encodeURIComponent('Merhaba, yolda kaldım. Çekici hizmetine ihtiyacım var. Konumum: ');
      if (!navigator.geolocation) { window.location.href = fallback; return; }
      var label = b.querySelector('.lbl');
      if (label) label.textContent = 'Konum alınıyor...';
      navigator.geolocation.getCurrentPosition(function (pos) {
        var url = 'https://maps.google.com/?q=' + pos.coords.latitude.toFixed(6) + ',' + pos.coords.longitude.toFixed(6);
        var msg = 'Merhaba, yolda kaldım. Çekici hizmetine ihtiyacım var. Konumum: ' + url;
        window.location.href = 'https://wa.me/' + PHONE + '?text=' + encodeURIComponent(msg);
      }, function () {
        window.location.href = fallback;
      }, { enableHighAccuracy: true, timeout: 10000 });
    });
  });
})();
