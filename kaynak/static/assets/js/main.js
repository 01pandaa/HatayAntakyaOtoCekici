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


  // ---------------- Dönüşüm takibi: arama & WhatsApp tıklamaları ----------------
  var T = window.TRACK || {};
  var AREAS = [['.mbar','mobil_alt_bar'],['.float','sabit_buton'],['.topbar','ust_serit'],['.header','menu'],
    ['.hero','ana_sayfa_ust'],['.page-hero','sayfa_ust'],['.sos','acil_serit'],['.price-band','uygun_fiyat'],
    ['.gallery','galeri'],['.aside','yan_kutu'],['.cta','alt_cagri'],['.contact','iletisim'],['.footer','alt_bilgi']];
  function area(el) {
    for (var i = 0; i < AREAS.length; i++) if (el.closest(AREAS[i][0])) return AREAS[i][1];
    return 'icerik';
  }
  var last = {};
  function track(kind, el) {
    var now = Date.now();
    if (last[kind] && now - last[kind] < 1500) return; // çift tıklamayı tek say
    last[kind] = now;
    var where = area(el), page = location.pathname;
    var ev = kind === 'call' ? 'arama_tiklama' : 'whatsapp_tiklama';
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ event: ev, buton_yeri: where, sayfa: page });
    if (typeof window.gtag === 'function') {
      if (T.ga4) gtag('event', kind === 'call' ? 'phone_call_click' : 'whatsapp_click', { button_location: where, page_path: page });
      var label = kind === 'call' ? T.ads_call_label : T.ads_wa_label;
      if (T.ads_id && label) gtag('event', 'conversion', { send_to: T.ads_id + '/' + label, value: 1.0, currency: 'TRY' });
    }
    if (T.meta && typeof window.fbq === 'function') fbq('track', 'Contact', { content_name: kind === 'call' ? 'Arama' : 'WhatsApp', content_category: where });
    if (/[?&]takip_test/.test(location.search)) console.log('[Dönüşüm]', ev, where, page);
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var h = a.getAttribute('href') || '';
    if (h.indexOf('tel:') === 0) track('call', a);
    else if (/wa\.me|api\.whatsapp\.com|whatsapp:\/\//.test(h)) track('wa', a);
  }, true);

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
        setTimeout(function () { window.location.href = 'https://wa.me/' + PHONE + '?text=' + encodeURIComponent(msg); }, 250);
      }, function () {
        window.location.href = fallback;
      }, { enableHighAccuracy: true, timeout: 10000 });
    });
  });
})();
