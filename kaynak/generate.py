# -*- coding: utf-8 -*-
"""Ersan Oto Kurtarma statik site üreticisi.
Tüm sayfalar ./site klasörüne yazılır. Bilgileri değiştirmek için sadece CONFIG'i düzenleyin."""
import os, json, shutil, html
from urllib.parse import quote

CONFIG = {
    "name": "Ersan Oto Kurtarma",
    "short": "Ersan",
    "owner": "Tamer Ersan",
    "phone_display": "0552 080 34 50",
    "phone_tel": "+905520803450",
    "wa": "905520803450",
    "email": "info@ersanotokurtarma.com",
    "street": "Odabaşı Mah. Abdi İpekçi Cad. 66 Sok. No:3/1",
    "city": "Antakya",
    "region": "Hatay",
    "postal": "31030",
    "lat": 36.246482,
    "lng": 36.167135,
    "domain": "https://www.ersanotocekici.com",
    # GitHub Pages proje adresinde "/RepoAdi/", kendi alan adında "/" olmalı (404 sayfası için)
    "base_path": "/",
    "custom_domain": True,  # True yapılırsa CNAME dosyası oluşturulur
}
C = CONFIG
OUT = os.path.join(os.path.dirname(__file__), "site")
STATIC = os.path.join(os.path.dirname(__file__), "static")

def wa(msg="Merhaba, oto kurtarma hizmeti hakkında bilgi almak istiyorum."):
    return f"https://wa.me/{C['wa']}?text={quote(msg)}"

# ------------------------------------------------------------------ ikonlar
I = {
 "phone": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>',
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.14-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.22 3.08c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.69.63.71.22 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35zM12.05 21.8h-.01a9.8 9.8 0 0 1-5-1.37l-.36-.21-3.72.98 1-3.63-.24-.37A9.82 9.82 0 0 1 12.05 2.2a9.8 9.8 0 0 1 9.82 9.82 9.83 9.83 0 0 1-9.82 9.78zm8.36-18.16A11.75 11.75 0 0 0 12.05.2 11.8 11.8 0 0 0 1.83 17.9L.16 24l6.25-1.64a11.8 11.8 0 0 0 5.64 1.43h.01A11.8 11.8 0 0 0 23.86 12a11.7 11.7 0 0 0-3.45-8.36z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
 "truck": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M1 16V7h11v9M12 10h5l4 4v2h-9"/><circle cx="6" cy="17.5" r="2"/><circle cx="17" cy="17.5" r="2"/><path d="M3 7 9 3"/></svg>',
 "hook": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2v9"/><path d="M12 11a4 4 0 1 1-4 4"/><path d="M8 2h8"/></svg>',
 "tool": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.7 6.3a4 4 0 0 0 5 5L22 14l-8 8-2.3-2.3a4 4 0 0 0-5-5L2 10l8-8z"/></svg>',
 "road": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 22 9 2M20 22 15 2M12 4v2M12 10v3M12 17v3"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><path d="M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5z"/><path d="m9 12 2 2 4-4"/></svg>',
 "battery": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="7" width="18" height="12" rx="2"/><path d="M22 11v4M6 7V5M16 7V5M11 10l-2 3h4l-2 3"/></svg>',
 "moto": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="5" cy="17" r="3"/><circle cx="19" cy="17" r="3"/><path d="M5 17h6l3-6h3l2 6M14 11l-2-4H9"/></svg>',
 "crash": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 15h2l2-5h7l3 5h2a2 2 0 0 1 2 2v1H3v-1a2 2 0 0 1 0-2z"/><path d="M12 2v3M5 4l2 2M19 4l-2 2"/></svg>',
}

# Logo / favicon
LOGO = ('<svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="12" fill="#FFB400"/>'
        '<path d="M8 31V19h14v12M22 23h7l6 5v3H22" fill="none" stroke="#0E2A47" stroke-width="3" stroke-linejoin="round"/>'
        '<path d="M10 19 20 12" stroke="#0E2A47" stroke-width="3" stroke-linecap="round"/>'
        '<circle cx="14" cy="33" r="3.5" fill="#0E2A47"/><circle cx="30" cy="33" r="3.5" fill="#0E2A47"/></svg>')

TRUCK_ART = '''<svg viewBox="0 0 520 300" role="img" aria-label="Üzerinde otomobil taşıyan oto çekici illüstrasyonu">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1d4f82"/><stop offset="1" stop-color="#0E2A47"/></linearGradient></defs>
<rect width="520" height="300" rx="18" fill="url(#sky)"/>
<circle cx="430" cy="62" r="26" fill="#FFB400" opacity=".9"/>
<path d="M0 205 C90 170 160 190 250 175 S420 150 520 172 V300 H0Z" fill="#0a1f35" opacity=".6"/>
<rect x="0" y="240" width="520" height="60" fill="#071728"/>
<g fill="#FFB400"><rect x="20" y="266" width="44" height="6" rx="3"/><rect x="110" y="266" width="44" height="6" rx="3"/><rect x="200" y="266" width="44" height="6" rx="3"/><rect x="290" y="266" width="44" height="6" rx="3"/><rect x="380" y="266" width="44" height="6" rx="3"/><rect x="470" y="266" width="44" height="6" rx="3"/></g>
<!-- flatbed -->
<rect x="60" y="196" width="290" height="18" rx="3" fill="#FFB400"/>
<g fill="#0E2A47"><rect x="72" y="200" width="16" height="10"/><rect x="104" y="200" width="16" height="10"/><rect x="136" y="200" width="16" height="10"/><rect x="168" y="200" width="16" height="10"/><rect x="200" y="200" width="16" height="10"/><rect x="232" y="200" width="16" height="10"/><rect x="264" y="200" width="16" height="10"/><rect x="296" y="200" width="16" height="10"/></g>
<rect x="60" y="214" width="300" height="16" fill="#e8edf3"/>
<!-- cab -->
<path d="M350 230 V150 a10 10 0 0 1 10-10 h62 a12 12 0 0 1 10 5 l30 40 a12 12 0 0 1 3 8 V230Z" fill="#E63946"/>
<path d="M366 152 h52 l26 34 h-78Z" fill="#bfe0ff" opacity=".85"/>
<rect x="356" y="196" width="108" height="6" fill="#c92d39"/>
<rect x="455" y="208" width="14" height="10" rx="2" fill="#FFB400"/>
<rect x="378" y="128" width="40" height="12" rx="4" fill="#FFB400"/><rect x="382" y="131" width="10" height="6" rx="2" fill="#ff6b00"/><rect x="404" y="131" width="10" height="6" rx="2" fill="#ff6b00"/>
<!-- car on bed -->
<path d="M96 196 v-22 a8 8 0 0 1 6-8 l30-6 26-26 a14 14 0 0 1 10-4 h76 a14 14 0 0 1 11 5 l28 33 24 4 a8 8 0 0 1 7 8 v16Z" fill="#f4f7fb"/>
<path d="M166 160 l22-22 h38 v22Z M234 138 h8 a8 8 0 0 1 6 3 l17 19 h-31Z" fill="#7fb2e5"/>
<circle cx="140" cy="196" r="20" fill="#14202e"/><circle cx="140" cy="196" r="8" fill="#9aa8b8"/>
<circle cx="276" cy="196" r="20" fill="#14202e"/><circle cx="276" cy="196" r="8" fill="#9aa8b8"/>
<!-- wheels truck -->
<g><circle cx="110" cy="236" r="24" fill="#14202e"/><circle cx="110" cy="236" r="10" fill="#9aa8b8"/>
<circle cx="168" cy="236" r="24" fill="#14202e"/><circle cx="168" cy="236" r="10" fill="#9aa8b8"/>
<circle cx="410" cy="236" r="24" fill="#14202e"/><circle cx="410" cy="236" r="10" fill="#9aa8b8"/></g>
<text x="205" y="226" fill="#0E2A47" font-family="Arial,sans-serif" font-weight="800" font-size="13" text-anchor="middle">7/24 OTO KURTARMA</text>
</svg>'''

# ------------------------------------------------------------------ fotoğraflar
PHOTOS = {
 "kare1": ("cekici-724-otoyol.webp", 615, 679, "7/24 oto çekici: otoyolda araç yükleyen kayar kasalı çekici"),
 "kare2": ("yolda-mi-kaldiniz-yagmur.webp", 616, 679, "Yağmurlu gecede yolda kalan araca çekici yardımı"),
 "kare3": ("cekici-724-gunbatimi.webp", 618, 667, "Gün batımında aracı çekiciye yükleyen kurtarma personeli"),
 "kare4": ("yolda-mi-kaldiniz-gece.webp", 618, 667, "Gece yağmurda araç kurtarma operasyonu"),
 "genis1": ("oto-kurtarma-sehir.webp", 1254, 572, "Şehir içinde SUV taşıyan oto kurtarma çekicisi"),
 "genis2": ("oto-kurtarma-otoyol.webp", 1254, 562, "Otoyolda araç taşıyan beyaz oto kurtarma çekicisi"),
}
def img(depth, key, cls="photo", eager=False):
    f, w, h, alt = PHOTOS[key]
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return f'<img class="{cls}" src="{rel(depth, "assets/img/" + f)}" width="{w}" height="{h}" alt="{e(alt)}" {load}>'

def gallery(depth):
    sq = "".join(f'<a class="g-item" href="tel:{C["phone_tel"]}" aria-label="Hemen arayın">{img(depth, k)}</a>' for k in ("kare1","kare2","kare3","kare4"))
    wd = "".join(f'<a class="g-item" href="tel:{C["phone_tel"]}" aria-label="Hemen arayın">{img(depth, k)}</a>' for k in ("genis1","genis2"))
    return f'<div class="gallery g4">{sq}</div><div class="gallery g2" style="margin-top:18px">{wd}</div>'

# ------------------------------------------------------------------ veri
SERVICES = [
 dict(slug="arac-cekme", icon="truck", name="Araç Çekme", title="Araç Çekme Hizmeti",
  short="Arızalı, kazalı veya çalışmayan aracınızı kayar kasalı çekicimizle güvenle istediğiniz noktaya taşıyoruz.",
  intro="Aracınız çalışmıyor, arıza lambası yandı ya da kaza sonrası yürüyemez hale mi geldi? Kayar kasalı (platform) çekicilerimizle aracınızı tekerleklerine ve şanzımanına yük bindirmeden, sabitleme kayışlarıyla güvenle çekiyoruz.",
  points=["Kayar kasalı platform çekici ile hasarsız yükleme","Otomobil, SUV, hafif ticari, panelvan ve minibüs","Servise, sanayiye, eve veya otoparka teslim","Otomatik vites ve 4x4 araçlar için güvenli taşıma","Sigorta ve ekspertiz süreçlerinde yönlendirme"],
  steps=["Bizi arayın veya WhatsApp'tan konumunuzu gönderin","Araç tipi ve gideceği yere göre fiyatı telefonda netleştirelim","En yakın çekicimiz yola çıksın, aracınızı yükleyip teslim edelim"]),
 dict(slug="arac-kurtarma", icon="hook", name="Araç Kurtarma", title="Kaza ve Zor Durum Araç Kurtarma",
  short="Kaza, devrilme, şarampole veya çukura düşme gibi zor kurtarma operasyonlarında profesyonel müdahale.",
  intro="Şarampole yuvarlanan, çamura saplanan, kar ve buzda kayan ya da kaza sonrası yol dışına çıkan araçlar özel ekipman ve deneyim ister. Vinç ve vinçli halat donanımımızla aracınızı ek hasar oluşturmadan kurtarıyoruz.",
  points=["Şarampol, hendek ve çukurdan araç çıkarma","Çamura, kuma veya kara saplanan araç kurtarma","Kaza sonrası yol temizliği ve aracın güvenli taşınması","Dağ ve köy yollarında (Yayladağı, Hassa, Altınözü) kurtarma","Trafik güvenliği için ikaz ve işaretleme"],
  steps=["Güvenli bir noktaya geçin, gerekirse 112'yi arayın","Bizi arayıp konumu ve aracın durumunu anlatın","Kurtarma ekipmanlı ekibimiz bölgeye gelip operasyonu tamamlasın"]),
 dict(slug="yol-yardim", icon="battery", name="Yol Yardım", title="Yol Yardım: Akü Takviye, Lastik, Yakıt",
  short="Akü takviyesi, lastik değişimi, yakıt ikmali ve küçük arızalarda yerinde müdahale.",
  intro="Her arıza çekici gerektirmez. Aküsü biten, lastiği patlayan ya da yakıtı biten araçlara yerinde müdahale ederek sizi en kısa sürede yeniden yola çıkarıyoruz.",
  points=["Akü takviyesi (akü bitti, araç çalışmıyor)","Patlak lastik değişimi ve stepne takma","Yolda kalan araca yakıt ulaştırma","Kapıda kalan anahtar ve basit arıza yönlendirmesi","Yerinde çözülemezse aynı ekiple çekme"],
  steps=["Aracın belirtilerini telefonda anlatın","Yerinde çözülebilecekse yol yardım ekibi gelsin","Çözülemezse aracınızı istediğiniz servise çekelim"]),
 dict(slug="arac-tasima", icon="road", name="Araç Taşıma", title="Araç Taşıma Hizmeti",
  short="Galeri, servis, ekspertiz veya ev taşıma için binek ve hafif ticari araç taşıma.",
  intro="Yeni aldığınız aracı galeriden, ekspertizden ya da başka bir ilçeden evinize getirmek; klasik veya modifiyeli aracınızı kilometre yaptırmadan taşımak istiyorsanız planlı araç taşıma hizmetimizden yararlanabilirsiniz.",
  points=["Galeri ve ekspertiz arası araç taşıma","Klasik, modifiyeli ve alçak araçlar için uygun rampa","Motosiklet taşıma","Randevulu ve zamanında teslim","Taşıma öncesi fotoğraflı teslim tutanağı"],
  steps=["Alış ve teslim adreslerini bildirin","Tarih ve saati birlikte planlayalım","Aracınızı teslim alıp güvenle ulaştıralım"]),
 dict(slug="sehirlerarasi-oto-kurtarma", icon="shield", name="Şehirlerarası Oto Kurtarma", title="Şehirlerarası Oto Kurtarma ve Araç Taşıma",
  short="Hatay'dan Türkiye'nin her iline sigortalı, güvenli ve zamanında şehirlerarası araç taşıma.",
  intro="Hatay'dan Adana, Mersin, Gaziantep, Osmaniye, Kahramanmaraş, Ankara, İstanbul ve Türkiye'nin her iline aracınızı taşıyoruz. Uzun yolda arıza yapan araçları da bulunduğu yerden alıp memleketine ulaştırıyoruz.",
  points=["Türkiye'nin tüm illerine kapıdan kapıya taşıma","Sigortalı ve güvenli uzun yol taşıması","Yolculuk boyunca bilgi ve konum paylaşımı","Uzun yolda arızalanan araçları geri getirme","Mesafeye göre önceden netleşen fiyat"],
  steps=["Çıkış ve varış noktasını bildirin","Fiyat ve tarihi netleştirelim","Aracınız sigortalı olarak yola çıksın, teslimde haber verelim"]),
 dict(slug="7-24-oto-cekici", icon="clock", name="7/24 Oto Çekici", title="7/24 Acil Oto Çekici",
  short="Gece gündüz, hafta sonu ve resmi tatillerde bir telefon kadar yakınınızdayız.",
  intro="Yolda kalmak saat sormaz. Gece yarısı, bayram sabahı ya da yağmurlu bir pazar günü — Antakya ve tüm Hatay'da 7 gün 24 saat çekici hizmeti veriyoruz. Telefonunuzu her zaman bir yetkili açar.",
  points=["Gece, hafta sonu ve resmi tatillerde kesintisiz hizmet","Telefonu her zaman bir yetkili açar, çağrı merkezi yok","Antakya merkezde ortalama 15-20 dakikada varış","WhatsApp'tan konum göndererek hızlı çağrı","Gece de aynı şeffaf fiyat politikası"],
  steps=["0552 080 34 50'yi arayın","Konumunuzu paylaşın","En yakın çekicimiz hemen yola çıksın"]),
]

# Hatay'ın 15 ilçesi (mesafeler Antakya merkeze yaklaşık karayolu mesafesidir)
D = [
 dict(slug="antakya", name="Antakya", km="Merkez", eta="15-20 dk",
  intro="Hatay'ın merkez ilçesi Antakya, ekibimizin ve çekicilerimizin bulunduğu yer. Odabaşı'ndaki merkezimizden çıkan çekicilerimiz şehir içindeki her noktaya hızla ulaşıyor.",
  areas=["Odabaşı","Saraykent","Cumhuriyet","Akevler","Serinyol","Narlıca","Ekinci","Aksaray","Kuzeytepe","Sağlık","Haraparası","Esentepe"],
  routes=["Antakya–İskenderun yolu (D817)","Antakya–Reyhanlı yolu","Antakya–Samandağ yolu","Şehir içi ana caddeler ve çevre yolu"],
  note="Antakya merkezde aracınız kaldıysa ortalama 15-20 dakikada yanınızdayız. Serinyol, Narlıca ve Ekinci gibi bölgelerde de aynı hızla hizmet veriyoruz."),
 dict(slug="defne", name="Defne", km="~5 km", eta="15-25 dk",
  intro="Antakya'ya komşu Defne ilçesi, Harbiye'den Sümerler'e kadar en sık hizmet verdiğimiz bölgelerden biri.",
  areas=["Harbiye","Sümerler","Armutlu","Elektrik","Dursunlu","Çekmece","Güzelburç","Hatun","Avcılar"],
  routes=["Antakya–Harbiye yolu","Antakya–Samandağ yolu","Defne–Altınözü bağlantısı"],
  note="Harbiye şelaleleri yolunda ya da Defne şehir içinde kaldıysanız merkezimize yakınlığı sayesinde çok kısa sürede ulaşıyoruz."),
 dict(slug="iskenderun", name="İskenderun", km="~58 km", eta="35-50 dk",
  intro="Hatay'ın liman kenti İskenderun'da şehir içi, sanayi bölgesi ve sahil yolunda oto çekici ve yol yardım hizmeti veriyoruz.",
  areas=["Sakarya","Numune","Dumlupınar","Modernevler","Denizciler","Karaağaç","Çay","Barbaros","Sanayi Sitesi"],
  routes=["Antakya–İskenderun yolu (D817) ve Belen geçidi","İskenderun–Arsuz sahil yolu","Adana–İskenderun otoyolu bağlantısı"],
  note="Belen geçidi ve D817 üzerinde kalan araçlar için hızlı müdahale ediyor, aracınızı İskenderun sanayisine veya istediğiniz servise taşıyoruz."),
 dict(slug="arsuz", name="Arsuz", km="~85 km", eta="45-65 dk",
  intro="Sahil ilçesi Arsuz'da, özellikle yaz aylarında yoğunlaşan trafikte yolda kalan araçlara çekici ve yol yardım hizmeti sunuyoruz.",
  areas=["Arsuz merkez","Uluçınar","Gözcüler","Konacık","Madenli","Karaağaç","Kale"],
  routes=["İskenderun–Arsuz sahil yolu","Arsuz–Samandağ bağlantı yolu"],
  note="Yazlıkçı ve tatilciler için şehirlerarası taşıma da yapıyoruz; aracınızı Arsuz'dan memleketinize götürebiliriz."),
 dict(slug="belen", name="Belen", km="~40 km", eta="25-40 dk",
  intro="Antakya ile İskenderun arasındaki Belen, virajlı ve eğimli geçidiyle arıza ve kaza riskinin yüksek olduğu bir güzergâh. Belen'de çekici ve kurtarma hizmeti veriyoruz.",
  areas=["Belen merkez","Kıcı","Atik","Bakras","Müftüler","Sarımazı","Kömürçukuru"],
  routes=["Belen geçidi (D817)","Belen–Kırıkhan yolu","Bakras yolu"],
  note="Belen yokuşunda motoru hararet yapan, freni ısınan ya da kaza yapan araçlara özellikle hızlı ulaşmaya çalışıyoruz."),
 dict(slug="dortyol", name="Dörtyol", km="~90 km", eta="55-75 dk",
  intro="Hatay'ın kuzeyindeki Dörtyol'da, otoyol ve şehir içinde kalan araçlara 7/24 oto çekici hizmeti veriyoruz.",
  areas=["Dörtyol merkez","Kuzuculu","Yeşilköy","Karakese","Özerli","Kuzucu","Altınçağ"],
  routes=["Adana–İskenderun otoyolu (Dörtyol bağlantısı)","Dörtyol–Osmaniye yolu","Dörtyol–Payas sahil yolu"],
  note="Otoyolda kaldıysanız emniyet şeridine geçip ikaz üçgeninizi koyun, ardından bizi arayın; konumunuzu WhatsApp'tan gönderebilirsiniz."),
 dict(slug="payas", name="Payas", km="~75 km", eta="45-65 dk",
  intro="Sanayi ve liman tesisleriyle hareketli Payas'ta binek ve hafif ticari araçlar için çekici ve yol yardım hizmeti sunuyoruz.",
  areas=["Payas merkez","Yakacık","Kürtül","Ödemiş","Akarca","Karayılan"],
  routes=["Adana–İskenderun otoyolu","Payas–İskenderun D817","Yakacık yolu"],
  note="Payas sanayi bölgesindeki işletmeler için düzenli araç taşıma da planlayabiliriz."),
 dict(slug="erzin", name="Erzin", km="~100 km", eta="60-80 dk",
  intro="Hatay'ın Osmaniye sınırındaki ilçesi Erzin'de yolda kalan araçlar için oto kurtarma ve çekici hizmeti veriyoruz.",
  areas=["Erzin merkez","Yeşilkent","Başlamış","Turunçlu","Aşağıburnaz","Kuşçular"],
  routes=["Adana–İskenderun otoyolu (Erzin bağlantısı)","Erzin–Osmaniye yolu","Erzin–Dörtyol yolu"],
  note="Erzin–Osmaniye hattında arızalanan araçları Hatay'a ya da Osmaniye'ye taşıyabiliyoruz."),
 dict(slug="kirikhan", name="Kırıkhan", km="~50 km", eta="35-50 dk",
  intro="Amik Ovası'nın kuzeyindeki Kırıkhan'da şehir içi, sanayi ve tarım yollarında çekici hizmeti sunuyoruz.",
  areas=["Kırıkhan merkez","Ceylanlı","Kodallı","Torun","Kurtuluş","Alaybeyli","Muratpaşa"],
  routes=["Antakya–Kırıkhan yolu","Kırıkhan–Hassa–Gaziantep yolu","Kırıkhan–Belen yolu"],
  note="Kırıkhan üzerinden Gaziantep'e giden yolda kalan araçlara da hizmet veriyor, şehirlerarası taşıma yapabiliyoruz."),
 dict(slug="kumlu", name="Kumlu", km="~40 km", eta="30-45 dk",
  intro="Amik Ovası'nın ortasındaki Kumlu'da tarla ve köy yollarında kalan araçlara da ulaşan çekici hizmeti veriyoruz.",
  areas=["Kumlu merkez","Akkerpiç","Gökçeoğlu","Hamam","Kırcaoğlu","Yaziköy"],
  routes=["Antakya–Kumlu yolu","Kumlu–Reyhanlı yolu","Kumlu–Kırıkhan bağlantısı"],
  note="Çamurlu köy ve tarla yollarında saplanan araçlar için kurtarma ekipmanıyla geliyoruz."),
 dict(slug="reyhanli", name="Reyhanlı", km="~45 km", eta="30-45 dk",
  intro="Cilvegözü sınır kapısına yakın Reyhanlı'da yoğun trafiğe uygun hızlı oto çekici ve yol yardım hizmeti veriyoruz.",
  areas=["Reyhanlı merkez","Cilvegözü","Kuşaklı","Varışlı","Ziyaret","Bükülmez","Döğüştepe"],
  routes=["Antakya–Reyhanlı yolu","Reyhanlı–Cilvegözü yolu","Reyhanlı–Kumlu yolu"],
  note="Sınır kapısı güzergâhında kalan binek ve hafif ticari araçlara da destek veriyoruz."),
 dict(slug="hassa", name="Hassa", km="~85 km", eta="50-70 dk",
  intro="Amanos Dağları eteğindeki Hassa'da dağ yollarında ve Gaziantep istikametinde kalan araçlara kurtarma hizmeti sunuyoruz.",
  areas=["Hassa merkez","Aktepe","Akbez","Kuzuculu","Gazelli","Yolbaşı","Bintaş"],
  routes=["Kırıkhan–Hassa yolu","Hassa–Gaziantep (İslahiye) yolu","Aktepe yolu"],
  note="Kış aylarında karlı ve buzlu yollarda kayan araçlar için kurtarma ekipmanıyla destek veriyoruz."),
 dict(slug="samandag", name="Samandağ", km="~28 km", eta="25-35 dk",
  intro="Akdeniz kıyısındaki Samandağ'da sahil yolu, Çevlik ve Meydan bölgesinde oto çekici hizmeti veriyoruz.",
  areas=["Samandağ merkez","Çevlik","Meydan","Mağaracık","Tekebaşı","Yaylıca","Sutaşı","Vakıflı"],
  routes=["Antakya–Samandağ yolu","Samandağ sahil yolu","Samandağ–Arsuz bağlantısı","Samandağ–Yayladağı yolu"],
  note="Sahilde kuma saplanan araçlar için de kurtarma hizmeti veriyoruz."),
 dict(slug="yayladagi", name="Yayladağı", km="~50 km", eta="35-55 dk",
  intro="Dağlık ve virajlı yollarıyla bilinen Yayladağı'nda, zor arazide yolda kalan araçlara çekici ve kurtarma hizmeti sunuyoruz.",
  areas=["Yayladağı merkez","Yeditepe","Güveççi","Kışlak","Topraklı","Aknehir"],
  routes=["Antakya–Yayladağı yolu","Yayladağı–Samandağ yolu","Yayladağı sınır kapısı yolu"],
  note="Virajlı dağ yollarında kaza ve şarampole düşme durumlarında kurtarma ekipmanıyla geliyoruz."),
 dict(slug="altinozu", name="Altınözü", km="~25 km", eta="25-35 dk",
  intro="Antakya'ya yakın Altınözü'nde merkez ve köy yollarında oto çekici ve yol yardım hizmeti veriyoruz.",
  areas=["Altınözü merkez","Tokdemir","Babatorun","Boynuyoğun","Hacıpaşa","Yanıkpınar","Kamberli"],
  routes=["Antakya–Altınözü yolu","Altınözü–Hacıpaşa yolu","Defne–Altınözü bağlantısı"],
  note="Merkeze yakınlığı sayesinde Altınözü'ne genellikle yarım saat içinde ulaşıyoruz."),
]
# Serinyol Antakya içindedir; ilçe listesi alfabetik değil, öncelik sırasına göredir.
LOC = {"defne":("Defne'de","Defne'den"),"belen":("Belen'de","Belen'den"),"payas":("Payas'ta","Payas'tan"),
       "erzin":("Erzin'de","Erzin'den"),"yayladagi":("Yayladağı'nda","Yayladağı'ndan"),"altinozu":("Altınözü'nde","Altınözü'nden")}
for d in D:
    d["path"] = f"bolgeler/{d['slug']}-oto-cekici/"
    d["loc"], d["abl"] = LOC.get(d["slug"], (d["name"] + "'da", d["name"] + "'dan"))

NAV = [("", "Ana Sayfa"), ("hizmetler/", "Hizmetler"), ("bolgeler/", "Bölgeler"), ("hakkimizda/", "Hakkımızda"), ("sss/", "S.S.S"), ("iletisim/", "İletişim")]

# ------------------------------------------------------------------ yardımcılar
def e(s): return html.escape(s, quote=True)

def rel(depth, path):
    pre = "../" * depth
    return (pre + path) if (pre + path) else "./"

def biz_schema():
    return {
      "@context": "https://schema.org",
      "@type": ["AutoRepair", "LocalBusiness"],
      "@id": C["domain"] + "/#business",
      "name": C["name"],
      "description": "Antakya ve Hatay genelinde 7/24 oto çekici, araç kurtarma, yol yardım ve araç taşıma hizmeti.",
      "url": C["domain"] + "/",
      "telephone": C["phone_tel"],
      "email": C["email"],
      "image": C["domain"] + "/assets/img/og-image.jpg",
      "logo": C["domain"] + "/assets/img/logo.svg",
      "priceRange": "₺₺",
      "founder": {"@type": "Person", "name": C["owner"]},
      "address": {"@type": "PostalAddress", "streetAddress": C["street"], "addressLocality": C["city"], "addressRegion": C["region"], "postalCode": C["postal"], "addressCountry": "TR"},
      "geo": {"@type": "GeoCoordinates", "latitude": C["lat"], "longitude": C["lng"]},
      "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], "opens": "00:00", "closes": "23:59"}],
      "areaServed": [{"@type": "City", "name": d["name"]} for d in D] + [{"@type": "AdministrativeArea", "name": "Hatay"}],
    }

def crumbs_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i+1, "name": n, "item": C["domain"] + "/" + p} for i, (p, n) in enumerate(items)]}

def faq_schema(qas):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]}

def call_btn(cls="btn btn-call", text=None, sub=None):
    t = text or C["phone_display"]
    inner = f'<span class="stack">{e(t)}<span class="sub">{e(sub)}</span></span>' if sub else e(t)
    return f'<a class="{cls}" href="tel:{C["phone_tel"]}">{I["phone"]}{inner}</a>'

def wa_btn(cls="btn btn-wa", text="WhatsApp'tan Yaz", msg=None, sub=None):
    inner = f'<span class="stack">{e(text)}<span class="sub">{e(sub)}</span></span>' if sub else e(text)
    return f'<a class="{cls}" href="{e(wa(msg) if msg else wa())}" target="_blank" rel="noopener">{I["wa"]}{inner}</a>'

def loc_btn(cls="btn loc-btn"):
    return f'<a class="{cls}" href="{e(wa("Merhaba, yolda kaldım. Konumum: "))}" data-send-location>{I["pin"]}<span class="lbl">Konumumu WhatsApp ile Gönder</span></a>'

def header(depth, active):
    links = []
    for p, n in NAV:
        cur = ' aria-current="page"' if p == active else ""
        if p == "hizmetler/":
            sub = "".join(f'<a href="{rel(depth, "hizmetler/" + s["slug"] + "/")}">{e(s["name"])}</a>' for s in SERVICES)
            links.append(f'<div class="has-drop"><a href="{rel(depth,p)}"{cur}>{n} ▾</a><div class="drop">{sub}</div></div>')
        elif p == "bolgeler/":
            sub = "".join(f'<a href="{rel(depth, d["path"])}">{e(d["name"])} Oto Çekici</a>' for d in D)
            links.append(f'<div class="has-drop"><a href="{rel(depth,p)}"{cur}>{n} ▾</a><div class="drop cols">{sub}</div></div>')
        else:
            links.append(f'<a href="{rel(depth,p)}"{cur}>{n}</a>')
    return f'''<a class="skip" href="#main">İçeriğe atla</a>
<div class="topbar"><div class="container"><span class="live"><i></i> Şu an açık · 7/24 hizmetteyiz</span><span class="hide-s">Antakya merkez &amp; Hatay'ın tüm ilçeleri · <a href="tel:{C["phone_tel"]}">{C["phone_display"]}</a></span></div></div>
<header class="header"><div class="container">
<a class="brand" href="{rel(depth,"")}" aria-label="{e(C["name"])} ana sayfa">{LOGO}<span><b>{e(C["name"])}</b><small>7/24 Antakya &amp; Hatay Çekici</small></span></a>
<nav class="nav" aria-label="Ana menü">{"".join(links)}</nav>
<div class="head-cta">{call_btn("btn btn-call btn-sm")}{wa_btn("btn btn-wa btn-sm", "WhatsApp")}<button class="menu-btn" aria-label="Menüyü aç" aria-expanded="false">{I["menu"]}</button></div>
</div></header>'''

def footer(depth):
    svc = "".join(f'<li><a href="{rel(depth,"hizmetler/"+s["slug"]+"/")}">{e(s["name"])}</a></li>' for s in SERVICES)
    d1 = "".join(f'<li><a href="{rel(depth,d["path"])}">{e(d["name"])} Oto Çekici</a></li>' for d in D[:8])
    d2 = "".join(f'<li><a href="{rel(depth,d["path"])}">{e(d["name"])} Oto Çekici</a></li>' for d in D[8:])
    return f'''<footer class="footer"><div class="container">
<div class="cols">
<div><a class="brand" href="{rel(depth,"")}">{LOGO}<span><b>{e(C["name"])}</b><small>7/24 Antakya &amp; Hatay</small></span></a>
<p style="margin-top:14px">Antakya ve Hatay genelinde 7/24 güvenilir, hızlı ve profesyonel oto kurtarma, araç çekme ve yol yardım hizmeti.</p>
<ul style="margin-top:14px"><li><a href="tel:{C["phone_tel"]}">📞 {C["phone_display"]}</a></li><li><a href="{e(wa())}" target="_blank" rel="noopener">💬 WhatsApp</a></li><li><a href="mailto:{C["email"]}">✉ {C["email"]}</a></li><li>📍 {e(C["street"])}, {C["city"]} / {C["region"]}</li></ul></div>
<div><h4>Hizmetler</h4><ul>{svc}</ul></div>
<div><h4>Bölgeler</h4><ul>{d1}</ul></div>
<div><h4>&nbsp;</h4><ul>{d2}<li><a href="{rel(depth,"bolgeler/")}">Tüm bölgeler →</a></li></ul></div>
</div>
<div class="copy"><span>© <span data-year>2026</span> {e(C["name"])} · {e(C["owner"])}. Tüm hakları saklıdır.</span><span><a href="{rel(depth,"hakkimizda/")}">Hakkımızda</a> · <a href="{rel(depth,"sss/")}">S.S.S</a> · <a href="{rel(depth,"iletisim/")}">İletişim</a></span></div>
</div></footer>
<div class="float"><a class="f-wa" href="{e(wa("Merhaba, yardıma ihtiyacım var."))}" target="_blank" rel="noopener" aria-label="WhatsApp ile yazın">{I["wa"]}<span class="tip">WhatsApp'tan yaz</span></a><a class="f-call" href="tel:{C["phone_tel"]}" aria-label="Hemen arayın">{I["phone"]}<span class="tip">Hemen ara: {C["phone_display"]}</span></a></div>
<div class="mbar"><a class="m-call" href="tel:{C["phone_tel"]}">{I["phone"]} HEMEN ARA</a><a class="m-wa" href="{e(wa("Merhaba, yardıma ihtiyacım var."))}" target="_blank" rel="noopener">{I["wa"]} WHATSAPP</a></div>
<script src="{rel(depth,"assets/js/main.js")}" defer></script>'''

def page(path, title, desc, body, active="", schemas=(), keywords=""):
    depth = path.count("/")
    canonical = C["domain"] + "/" + path
    sch = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in [biz_schema(), *schemas])
    kw = f'<meta name="keywords" content="{e(keywords)}">' if keywords else ""
    doc = f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{kw}
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0E2A47">
<meta name="format-detection" content="telephone=yes">
<meta name="geo.region" content="TR-31"><meta name="geo.placename" content="Antakya, Hatay"><meta name="geo.position" content="{C["lat"]};{C["lng"]}"><meta name="ICBM" content="{C["lat"]}, {C["lng"]}">
<meta property="og:type" content="website"><meta property="og:locale" content="tr_TR"><meta property="og:site_name" content="{e(C["name"])}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canonical}">
<meta property="og:image" content="{C["domain"]}/assets/img/og-image.jpg"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{rel(depth,"assets/img/favicon.svg")}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel(depth,"assets/css/style.css")}">
{sch}
</head>
<body id="top">
{header(depth, active)}
<main id="main">
{body}
</main>
{footer(depth)}
</body>
</html>
'''
    target = os.path.join(OUT, path, "index.html") if path else os.path.join(OUT, "index.html")
    if path.endswith(".html"):
        target = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(doc)

def page_hero(depth, crumbs, h1, lead, extra=""):
    cr = ' <span>/</span> '.join([f'<a href="{rel(depth,p)}">{e(n)}</a>' for p, n in crumbs[:-1]] + [e(crumbs[-1][1])])
    return f'''<section class="page-hero"><div class="container">
<nav class="crumbs" aria-label="Sayfa yolu">{cr}</nav>
<h1>{h1}</h1><p>{lead}</p>
<div class="hero-cta">{call_btn("btn btn-call btn-lg", "Hemen Ara", C["phone_display"])}{wa_btn("btn btn-wa btn-lg", "WhatsApp'tan Yaz", sub="Hızlı mesaj gönder")}{extra}</div>
</div></section>'''

def sos(depth):
    return f'''<section class="sos"><div class="container">
<div><h2>Acil mi? Şimdi arayın.</h2><p>Antakya merkezde ortalama 15-20 dakikada yanınızdayız.</p></div>
<div class="acts">{call_btn("btn btn-call btn-lg")}{wa_btn("btn btn-wa btn-lg", "WhatsApp", msg="Merhaba, yardıma ihtiyacım var.")}</div>
</div></section>'''

def cta(depth, title="Yolda mı kaldınız?", text="Bir telefon kadar yakınız. Hemen arayın veya WhatsApp'tan konumunuzu gönderin, en yakın çekicimiz yola çıksın."):
    return f'''<section class="section" style="padding-top:20px"><div class="container"><div class="cta">
<div><h2>{e(title)}</h2><p>{e(text)}</p></div>
<div class="acts">{call_btn("btn btn-call btn-lg")}{wa_btn("btn btn-wa btn-lg", "WhatsApp")}</div>
</div></div></section>'''

def service_cards(depth):
    return "".join(f'''<a class="card-s" href="{rel(depth,"hizmetler/"+s["slug"]+"/")}"><div class="ico">{I[s["icon"]]}</div><h3>{e(s["name"])}</h3><p>{e(s["short"])}</p><span class="more">Detaylı bilgi</span></a>''' for s in SERVICES)

def district_grid(depth, exclude=None):
    out = []
    for d in D:
        if d["slug"] == exclude: continue
        main = " main" if d["slug"] == "antakya" else ""
        sub = "Merkez · 15-20 dk" if d["slug"] == "antakya" else f'{d["km"]} · {d["eta"]}'
        out.append(f'<a class="district{main}" href="{rel(depth,d["path"])}"><span>{e(d["name"])}<small>{sub}</small></span><span class="pin">{I["pin"]}</span></a>')
    return "".join(out)

WHY = [
 ("7/24 Açık", "Gece 03:00'te de, pazar sabahı da arayabilirsiniz. Telefonu her zaman bir yetkili açar."),
 ("Hızlı Varış", "Antakya merkez içinde ortalama 15-20 dakika, ilçelerde mesafeye göre 25-80 dakika."),
 ("Şeffaf Fiyat", "Fiyat yola çıkmadan telefonda netleşir. Sürpriz ek ücret yok."),
 ("Profesyonel Ekipman", "Kayar kasalı çekici, vinç ve kurtarma donanımıyla her duruma hazırız."),
 ("Tüm Hatay'da", "Antakya başta olmak üzere 15 ilçenin tamamında ve şehirlerarası güzergâhlarda."),
 ("Sigortalı Taşıma", "Şehirlerarası taşımalarda aracınız sigorta güvencesiyle yolculuk eder."),
]
def why_block():
    return "".join(f'<div class="why"><div class="n">{i+1}</div><div><h3>{e(t)}</h3><p>{e(p)}</p></div></div>' for i, (t, p) in enumerate(WHY))

FAQ = [
 ("7/24 hizmet veriyor musunuz?", "Evet, haftanın 7 günü 24 saat hizmetinizdeyiz. Gece, hafta sonu ve resmi tatiller dahil her an arayabilirsiniz."),
 ("Hangi bölgelere hizmet veriyorsunuz?", "Antakya merkez başta olmak üzere Hatay'ın 15 ilçesinin tamamına (Antakya, Defne, İskenderun, Arsuz, Belen, Dörtyol, Payas, Erzin, Kırıkhan, Kumlu, Reyhanlı, Hassa, Samandağ, Yayladağı, Altınözü) ve şehirlerarası tüm güzergâhlara hizmet veriyoruz."),
 ("Ortalama varış süreniz nedir?", "Antakya merkez içinde ortalama 15-20 dakika; ilçelerde mesafe, konum ve trafik yoğunluğuna göre 25-80 dakika içinde yanınızdayız."),
 ("Fiyat nasıl belirleniyor?", "Fiyat; mesafe, araç tipi ve hizmet türüne göre belirlenir ve yola çıkmadan önce telefonda netleştirilir. Sürpriz ek ücret yoktur."),
 ("Hangi araçları çekiyorsunuz?", "Otomobil, SUV, hafif ticari, panelvan, minibüs ve motosiklet dahil tüm binek araçları çekiyoruz. Ağır vasıta için ön görüşme yapılır."),
 ("Şehirlerarası araç taşıma yapıyor musunuz?", "Evet, Hatay'dan Türkiye'nin tüm illerine güvenli ve sigortalı araç taşıma hizmeti veriyoruz."),
 ("Konumumu nasıl gönderebilirim?", "Sitedeki \"Konumumu WhatsApp ile Gönder\" butonuna dokunun; telefonunuz konum izni isteyecek ve konumunuz hazır mesajla WhatsApp'a aktarılacak. Dilerseniz WhatsApp'tan canlı konum da paylaşabilirsiniz."),
 ("Ödeme nasıl yapılıyor?", "Nakit, banka havalesi/EFT ve mobil ödeme yöntemleriyle ödeme yapabilirsiniz."),
]
def faq_block(qas):
    return '<div class="faq">' + "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in qas) + '</div>'

def aside(depth, current_service=None, current_district=None):
    svc = "".join(f'<a href="{rel(depth,"hizmetler/"+s["slug"]+"/")}">{e(s["name"])}</a>' for s in SERVICES if s["slug"] != current_service)
    dis = "".join(f'<a href="{rel(depth,d["path"])}">{e(d["name"])} Oto Çekici</a>' for d in D if d["slug"] != current_district)
    return f'''<aside class="aside">
<div class="box"><h3>7/24 Acil Çekici</h3><p>Yolda kaldıysanız hemen arayın ya da konumunuzu WhatsApp'tan gönderin.</p>
{call_btn("btn btn-call", "Hemen Ara", C["phone_display"])}{wa_btn("btn btn-wa", "WhatsApp'tan Yaz")}{loc_btn("btn loc-btn")}</div>
<div class="box light"><h3>Hizmetlerimiz</h3>{svc}</div>
<div class="box light"><h3>Hizmet Bölgeleri</h3>{dis}</div>
</aside>'''

# ------------------------------------------------------------------ sayfalar
def build_home():
    body = f'''<section class="hero"><div class="container">
<div>
<span class="eyebrow">● 7/24 Antakya &amp; Hatay Oto Çekici</span>
<h1 style="margin-top:18px">Yolda Kalmayın, <span>Bize Ulaşın.</span></h1>
<p>Antakya ve Hatay genelinde <strong>7/24 güvenilir, hızlı ve profesyonel</strong> oto kurtarma, araç çekme, yol yardım ve araç taşıma hizmeti. {e(C["owner"])} ve deneyimli ekibiyle tek aramada yanınızdayız.</p>
<div class="hero-cta">{call_btn("btn btn-call btn-lg", "Hemen Ara", C["phone_display"])}{wa_btn("btn btn-wa btn-lg", "WhatsApp'tan Yaz", sub="Hızlı mesaj gönder")}</div>
<div class="hero-cta" style="margin-top:12px">{loc_btn("btn btn-ghost")}</div>
<div class="stats"><div><b>15 dk</b><span>Antakya ort. varış</span></div><div><b>7/24</b><span>Kesintisiz hizmet</span></div><div><b>15</b><span>Hatay ilçesi</span></div><div><b>81 il</b><span>Şehirlerarası taşıma</span></div></div>
</div>
<div class="hero-art"><span class="badge">Şu an açık</span><div class="card">{img(0, "kare1", eager=True)}</div></div>
</div></section>
{sos(0)}
<section class="section" id="hizmetler"><div class="container">
<div class="head center"><span class="kicker">Hizmetlerimiz</span><h2>Yolda kalmanıza çözüm olacak tüm hizmetler</h2><p>Araç çekmeden zor kurtarmaya, şehir içinden şehirlerarası taşımaya — tek elden profesyonel çözüm.</p></div>
<div class="grid g3">{service_cards(0)}</div>
</div></section>
<section class="section alt" id="galeri"><div class="container">
<div class="head center"><span class="kicker">Sahadan Kareler</span><h2>Yolda kaldığınız her an yanınızdayız</h2><p>Gece, yağmur, otoyol ya da şehir içi — Hatay'ın her köşesinde 7/24 çekici ve kurtarma.</p></div>
{gallery(0)}
<div class="hero-cta" style="justify-content:center;margin-top:28px">{call_btn("btn btn-call btn-lg", "Hemen Ara", C["phone_display"])}{wa_btn("btn btn-wa btn-lg", "WhatsApp'tan Yaz", sub="Hızlı mesaj gönder")}</div>
</div></section>
<section class="section dark"><div class="container">
<div class="head center"><span class="kicker">Neden Biz</span><h2>Hatay'da neden {e(C["name"])}?</h2><p>Sadece bir çekici değil, yolda kaldığınızda yanınızda duran bir çözüm ortağı.</p></div>
<div class="grid g3">{why_block()}</div>
</div></section>
<section class="section"><div class="container about">
<div class="art">{img(0, "genis1")}<span class="tag">Sigortalı &amp; Güvenilir</span></div>
<div><span class="kicker">Hakkımızda</span><h2>{e(C["owner"])} ile yolda güvendesiniz</h2>
<p style="margin-top:14px">{e(C["name"])}, Antakya'da {e(C["owner"])} tarafından kurulan, bölge halkının güvendiği yerel bir oto kurtarma ve yol yardım işletmesidir. Antakya'nın sokaklarını, Defne'den İskenderun'a, Reyhanlı'dan Arsuz'a kadar Hatay'ın tüm güzergâhlarını yakından tanıyoruz.</p>
<p>Amacımız yalnızca aracınızı çekmek değil; stresli bir anınızda yanınızda olmak ve sizi güvenle yola devam ettirmek. Bu yüzden <strong>şeffaf fiyat</strong>, <strong>deneyimli sürücüler</strong> ve <strong>bakımlı ekipman</strong> bizim için vazgeçilmez.</p>
<a class="btn btn-amber" href="hakkimizda/" style="margin-top:8px">Daha fazla bilgi</a>
<div class="owner"><div class="av">TE</div><div><b>{e(C["owner"])}</b><span>İşletme Sahibi · {e(C["name"])}</span></div></div>
</div></div></section>
<section class="section alt" id="bolgeler"><div class="container">
<div class="head center"><span class="kicker">Hizmet Bölgelerimiz</span><h2>Hatay'ın tüm ilçelerinde yanınızdayız</h2><p>İlçenizi seçin; o bölgeye özel varış süresi, güzergâhlar ve hizmet detaylarını görün.</p></div>
<div class="districts">{district_grid(0)}</div>
</div></section>
<section class="section" id="sss"><div class="container">
<div class="head center"><span class="kicker">Sıkça Sorulan Sorular</span><h2>Aklınızdaki sorular</h2></div>
{faq_block(FAQ[:6])}
<p style="text-align:center;margin-top:20px"><a class="more" href="sss/">Tüm soruları gör</a></p>
</div></section>
{cta(0)}'''
    page("", f"{C['name']} | 7/24 Antakya & Hatay Oto Çekici, Yol Yardım", 
         f"{C['name']} — Antakya ve Hatay'ın tüm ilçelerinde 7/24 oto çekici, araç kurtarma, yol yardım ve araç taşıma. Hemen arayın: {C['phone_display']}.",
         body, active="", schemas=[faq_schema(FAQ[:6])],
         keywords="oto çekici, oto kurtarma, Antakya çekici, Hatay çekici, Hatay oto kurtarma, yol yardım, araç taşıma, " + ", ".join(d["name"]+" çekici" for d in D))

def build_services():
    body = page_hero(1, [("", "Ana Sayfa"), ("hizmetler/", "Hizmetler")], "Oto Kurtarma <span style='color:var(--amber)'>Hizmetlerimiz</span>",
        "Antakya ve Hatay genelinde araç çekme, kaza kurtarma, yol yardım, araç taşıma ve şehirlerarası taşıma — 7 gün 24 saat.")
    body += f'''<section class="section"><div class="container"><div class="grid g3">{service_cards(1)}</div></div></section>
<section class="section dark"><div class="container"><div class="head center"><span class="kicker">Neden Biz</span><h2>Güvenle teslim, şeffaf fiyat</h2></div><div class="grid g3">{why_block()}</div></div></section>
{cta(1)}'''
    page("hizmetler/", f"Hizmetlerimiz | {C['name']} — Hatay Oto Çekici", 
         "Antakya ve Hatay'da araç çekme, araç kurtarma, yol yardım, araç taşıma ve şehirlerarası oto kurtarma hizmetleri. 7/24 " + C["phone_display"],
         body, active="hizmetler/", schemas=[crumbs_schema([("", "Ana Sayfa"), ("hizmetler/", "Hizmetler")])])

    for s in SERVICES:
        path = f"hizmetler/{s['slug']}/"
        cr = [("", "Ana Sayfa"), ("hizmetler/", "Hizmetler"), (path, s["name"])]
        pts = "".join(f"<li>{e(p)}</li>" for p in s["points"])
        steps = "".join(f'<div class="why" style="background:var(--bg-2);border-color:var(--line)"><div class="n">{i+1}</div><div><p style="color:var(--ink)">{e(t)}</p></div></div>' for i, t in enumerate(s["steps"]))
        dlinks = "".join(f'<a href="{rel(2,d["path"])}">{e(d["name"])}</a>' for d in D)
        qas = [(f"Antakya'da {s['name'].lower()} hizmeti ne kadar sürede gelir?", "Antakya merkez içinde ortalama 15-20 dakikada, ilçelerde ise mesafeye göre 25-80 dakika içinde bölgeye ulaşıyoruz."),
               (f"{s['name']} ücreti ne kadar?", "Ücret; mesafe, araç tipi ve aracın durumuna göre değişir. Bizi aradığınızda fiyatı yola çıkmadan önce netleştiriyoruz."),
               ("Gece ya da bayramda da hizmet veriyor musunuz?", "Evet, 7 gün 24 saat hizmet veriyoruz; gece ve resmi tatillerde de aynı şekilde ulaşabilirsiniz.")]
        body = page_hero(2, cr, f"{e(s['title'])} <span style='color:var(--amber)'>Antakya &amp; Hatay</span>", e(s["short"]))
        body += f'''<section class="section"><div class="container content">
<div class="prose">
<h2>{e(s["name"])} hizmeti</h2>
<p>{e(s["intro"])}</p>
<h3>Bu hizmet kapsamında</h3><ul>{pts}</ul>
<h3>Nasıl çalışıyoruz?</h3><div class="grid" style="gap:12px;margin-bottom:22px">{steps}</div>
<h2>Hatay'ın tüm ilçelerinde {e(s["name"].lower())}</h2>
<p>{e(s["name"])} hizmetimizi Antakya merkez başta olmak üzere Hatay'ın 15 ilçesinin tamamında veriyoruz. Bulunduğunuz ilçeye özel bilgi için seçin:</p>
<div class="chips">{dlinks.replace("<a ", "<span><a ").replace("</a>", "</a></span>")}</div>
<h2>Sıkça sorulanlar</h2>
{faq_block(qas)}
</div>
{aside(2, current_service=s["slug"])}
</div></section>
{cta(2)}'''
        page(path, f"{s['title']} | Antakya & Hatay 7/24 — {C['name']}",
             f"Antakya ve Hatay'da 7/24 {s['name'].lower()}: {s['short']} Hemen arayın: {C['phone_display']}.",
             body, active="hizmetler/", schemas=[crumbs_schema(cr), faq_schema(qas),
               {"@context": "https://schema.org", "@type": "Service", "name": s["title"], "serviceType": s["name"], "provider": {"@id": C["domain"] + "/#business"}, "areaServed": [d["name"] for d in D]}],
             keywords=f"{s['name']} Antakya, {s['name']} Hatay, " + ", ".join(f"{d['name']} {s['name'].lower()}" for d in D[:8]))

def build_districts():
    cr0 = [("", "Ana Sayfa"), ("bolgeler/", "Bölgeler")]
    body = page_hero(1, cr0, "Hatay'ın Tüm İlçelerinde <span style='color:var(--amber)'>Oto Çekici</span>",
        "Antakya merkez başta olmak üzere Hatay'ın 15 ilçesinin tamamında 7/24 oto çekici, kurtarma ve yol yardım. İlçenizi seçin.")
    body += f'''<section class="section"><div class="container"><div class="districts">{district_grid(1)}</div>
<p style="margin-top:22px;text-align:center">Mesafeler Antakya merkeze yaklaşık karayolu mesafesidir; varış süreleri trafik ve hava koşullarına göre değişebilir.</p></div></section>
{cta(1)}'''
    page("bolgeler/", f"Hizmet Bölgeleri | Hatay'ın 15 İlçesinde Oto Çekici — {C['name']}",
         "Antakya, Defne, İskenderun, Arsuz, Belen, Dörtyol, Payas, Erzin, Kırıkhan, Kumlu, Reyhanlı, Hassa, Samandağ, Yayladağı ve Altınözü'nde 7/24 oto çekici.",
         body, active="bolgeler/", schemas=[crumbs_schema(cr0)])

    for i, d in enumerate(D):
        n = d["name"]
        cr = cr0 + [(d["path"], f"{n} Oto Çekici")]
        areas = "".join(f"<span>{e(a)}</span>" for a in d["areas"])
        routes = "".join(f"<li>{e(r)}</li>" for r in d["routes"])
        svcs = "".join(f'<li><a href="{rel(2,"hizmetler/"+s["slug"]+"/")}"><b>{e(n)} {e(s["name"].lower())}</b></a> — {e(s["short"])}</li>' for s in SERVICES)
        dist_txt = "merkezimizin bulunduğu ilçe" if d["km"] == "Merkez" else f"Antakya merkeze yaklaşık {d['km'].replace('~','')} uzaklıkta"
        qas = [(f"{d['loc']} en yakın oto çekici ne kadar sürede gelir?", f"{n} için ortalama varış süremiz {d['eta']}'dır. Süre; bulunduğunuz nokta, trafik ve hava koşullarına göre değişebilir."),
               (f"{d['loc']} gece de çekici hizmeti var mı?", f"Evet. {n} ve çevresinde 7 gün 24 saat, gece ve resmi tatiller dahil hizmet veriyoruz."),
               (f"{d['abl']} başka ile araç taşıyor musunuz?", f"Evet. Aracınızı {d['abl']} Hatay'ın diğer ilçelerine veya Türkiye'nin herhangi bir iline sigortalı olarak taşıyabiliyoruz."),
               (f"{n} oto çekici fiyatı ne kadar?", "Fiyat; mesafe, araç tipi ve hizmet türüne göre belirlenir. Bizi aradığınızda fiyatı yola çıkmadan önce telefonda netleştiriyoruz.")]
        near = [D[j] for j in range(len(D)) if j != i][:0]
        body = page_hero(2, cr, f"{e(n)} Oto Çekici <span style='color:var(--amber)'>7/24</span>",
            f"{e(n)} ve çevresinde 7 gün 24 saat oto çekici, araç kurtarma, yol yardım ve araç taşıma. Ortalama varış: <strong style='color:#fff'>{d['eta']}</strong>.",
            extra=loc_btn("btn btn-ghost btn-lg"))
        body += f'''<section class="section"><div class="container content">
<div class="prose">
<div class="facts"><div><b>{e(d["eta"])}</b><span>Ortalama varış</span></div><div><b>{e(d["km"])}</b><span>Antakya merkeze uzaklık</span></div><div><b>7/24</b><span>Kesintisiz hizmet</span></div></div>
<h2>{e(d['loc'])} oto çekici ve yol yardım</h2>
<p>{e(d["intro"])}</p>
<p>{e(n)}, {dist_txt}. {e(d["note"])}</p>
<h3>{e(d['loc'])} hizmet verdiğimiz başlıca bölgeler</h3>
<div class="chips">{areas}<span>ve tüm mahalle/köyler</span></div>
<h3>Hizmet verdiğimiz güzergâhlar</h3><ul>{routes}</ul>
<h2>{e(d['loc'])} sunduğumuz hizmetler</h2>
<ul>{svcs}</ul>
<h2>{e(d['loc'])} yolda kaldıysanız ne yapmalısınız?</h2>
<ul><li>Aracınızı mümkünse yol kenarına veya emniyet şeridine alın, dörtlüleri yakın.</li><li>İkaz üçgenini aracın yaklaşık 30-50 metre arkasına koyun.</li><li>Bizi {C["phone_display"]} numarasından arayın veya konumunuzu WhatsApp'tan gönderin.</li><li>Kaza ve yaralanma varsa önce 112'yi arayın.</li></ul>
<h2>{e(n)} oto çekici — sıkça sorulanlar</h2>
{faq_block(qas)}
</div>
{aside(2, current_district=d["slug"])}
</div></section>
<section class="section alt"><div class="container"><div class="head center"><span class="kicker">Diğer Bölgeler</span><h2>Hatay'ın diğer ilçelerinde de yanınızdayız</h2></div><div class="districts">{district_grid(2, exclude=d["slug"])}</div></div></section>
{cta(2, title=f"{d['loc']} yolda mı kaldınız?")}'''
        page(d["path"], f"{n} Oto Çekici 7/24 | {n} Oto Kurtarma & Yol Yardım — {C['name']}",
             f"{n} oto çekici ve oto kurtarma: 7/24 araç çekme, kaza kurtarma, akü takviye ve araç taşıma. Ortalama varış {d['eta']}. Hemen arayın: {C['phone_display']}.",
             body, active="bolgeler/", schemas=[crumbs_schema(cr), faq_schema(qas),
               {"@context": "https://schema.org", "@type": "Service", "name": f"{n} Oto Çekici", "serviceType": "Oto çekici ve yol yardım", "provider": {"@id": C["domain"] + "/#business"}, "areaServed": {"@type": "City", "name": n, "containedInPlace": {"@type": "AdministrativeArea", "name": "Hatay"}}}],
             keywords=f"{n} oto çekici, {n} çekici, {n} oto kurtarma, {n} yol yardım, {n} araç taşıma, {n} en yakın çekici, " + ", ".join(d["areas"][:4]))

def build_about():
    cr = [("", "Ana Sayfa"), ("hakkimizda/", "Hakkımızda")]
    body = page_hero(1, cr, "Hakkımızda", f"{e(C['name'])} — Antakya merkezli, Hatay'ın tüm ilçelerine hizmet veren yerel oto kurtarma işletmesi.")
    body += f'''<section class="section"><div class="container about">
<div class="art">{img(1, "genis2")}<span class="tag">7/24 Hizmetteyiz</span></div>
<div class="prose"><span class="kicker">Biz Kimiz?</span><h2>{e(C["owner"])} ile yolda güvendesiniz</h2>
<p>{e(C["name"])}, Hatay'ın Antakya ilçesinde {e(C["owner"])} tarafından kurulmuştur. Bölgeyi yakından tanıyan ekibimizle Antakya merkezden Hatay'ın en uzak köyüne kadar yolda kalan sürücülere destek oluyoruz.</p>
<p>Yolda kalmanın ne kadar stresli olduğunu biliyoruz. Bu yüzden telefonu her zaman bir yetkili açar, fiyatı yola çıkmadan netleştirir ve aracınızı kendi aracımız gibi taşırız.</p>
<h3>Değerlerimiz</h3>
<ul><li>Hız: Antakya merkezde ortalama 15-20 dakikada varış</li><li>Şeffaflık: Önceden netleşen fiyat, sürpriz ücret yok</li><li>Güven: Sigortalı taşıma ve fotoğraflı teslim</li><li>Ulaşılabilirlik: 7 gün 24 saat, telefon ve WhatsApp</li></ul>
<div class="owner"><div class="av">TE</div><div><b>{e(C["owner"])}</b><span>İşletme Sahibi · {e(C["name"])}</span></div></div>
</div></div></section>
<section class="section dark"><div class="container"><div class="head center"><span class="kicker">Neden Biz</span><h2>Sizi neden yarı yolda bırakmayız</h2></div><div class="grid g3">{why_block()}</div></div></section>
{cta(1)}'''
    page("hakkimizda/", f"Hakkımızda | {C['name']} — {C['owner']}", f"{C['name']}, Antakya'da {C['owner']} tarafından kurulan, Hatay genelinde 7/24 hizmet veren oto kurtarma işletmesidir.",
         body, active="hakkimizda/", schemas=[crumbs_schema(cr)])

def build_faq():
    cr = [("", "Ana Sayfa"), ("sss/", "S.S.S")]
    body = page_hero(1, cr, "Sıkça Sorulan Sorular", "Oto çekici, kurtarma ve araç taşıma hakkında en çok merak edilenler.")
    body += f'''<section class="section"><div class="container">{faq_block(FAQ)}</div></section>{cta(1, "Sorunuzun cevabı burada yok mu?", "Bizi arayın veya WhatsApp'tan yazın, hemen yanıtlayalım.")}'''
    page("sss/", f"Sıkça Sorulan Sorular | {C['name']}", "Hatay oto çekici hizmeti hakkında sık sorulan sorular: varış süresi, fiyat, ödeme, hizmet bölgeleri.",
         body, active="sss/", schemas=[crumbs_schema(cr), faq_schema(FAQ)])

def build_contact():
    cr = [("", "Ana Sayfa"), ("iletisim/", "İletişim")]
    map_q = quote(f"{C['lat']},{C['lng']}")
    body = page_hero(1, cr, "İletişim", "Bir telefon kadar yakınız. Hemen arayın veya WhatsApp'tan yazın, en kısa sürede yola çıkalım.", extra=loc_btn("btn btn-ghost btn-lg"))
    body += f'''<section class="section"><div class="container">
<div class="contact">
<a class="c-item c-call" href="tel:{C["phone_tel"]}">{I["phone"]}<small>Telefon · 7/24</small><b>{C["phone_display"]}</b></a>
<a class="c-item c-wa" href="{e(wa())}" target="_blank" rel="noopener">{I["wa"]}<small>WhatsApp</small><b>Hızlı mesaj gönder</b></a>
<a class="c-item c-mail" href="mailto:{C["email"]}">{I["mail"]}<small>E-posta</small><b style="font-size:1rem">{C["email"]}</b></a>
<a class="c-item c-addr" href="https://www.google.com/maps/search/?api=1&amp;query={map_q}" target="_blank" rel="noopener">{I["pin"]}<small>Adres</small><b style="font-size:1rem">{e(C["street"])}<br>{C["city"]} / {C["region"]} · {C["postal"]}</b></a>
</div>
<div class="map"><iframe title="{e(C["name"])} konum haritası" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q={map_q}&amp;z=15&amp;output=embed"></iframe></div>
</div></section>
<section class="section alt"><div class="container"><div class="head center"><span class="kicker">Hizmet Bölgeleri</span><h2>Hatay'ın her yerine geliyoruz</h2></div><div class="districts">{district_grid(1)}</div></div></section>'''
    page("iletisim/", f"İletişim | {C['name']} — {C['phone_display']}", f"{C['name']} iletişim: 7/24 telefon {C['phone_display']}, WhatsApp, e-posta ve adres. {C['street']}, {C['city']}/{C['region']}.",
         body, active="iletisim/", schemas=[crumbs_schema(cr)])

def build_404():
    body = f'''<section class="page-hero"><div class="container" style="text-align:center;padding:80px 20px">
<h1>Sayfa bulunamadı</h1><p style="margin:14px auto 24px">Aradığınız sayfa taşınmış olabilir. Yolda kaldıysanız hemen arayın.</p>
<div class="hero-cta" style="justify-content:center">{call_btn("btn btn-call btn-lg")}{wa_btn("btn btn-wa btn-lg", "WhatsApp")}<a class="btn btn-amber btn-lg" href="/">Ana sayfa</a></div>
</div></section>'''
    # 404 sayfası her derinlikten açılabileceği için mutlak yollar kullanır
    page("404.html", f"Sayfa bulunamadı | {C['name']}", "Sayfa bulunamadı.", body)
    p = os.path.join(OUT, "404.html")
    s = open(p, encoding="utf-8").read()
    # 404 kök dizinde ama /olmayan/yol altında gösterilir → kökten mutlak yol
    B = C["base_path"]
    s = s.replace('href="assets/', f'href="{B}assets/').replace('src="assets/', f'src="{B}assets/')
    s = s.replace('href="./"', f'href="{B}"').replace('href="/"', f'href="{B}"')
    for pth in ["hizmetler/", "bolgeler/", "hakkimizda/", "sss/", "iletisim/"]:
        s = s.replace(f'href="{pth}', f'href="{B}{pth}')
    s = s.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
    open(p, "w", encoding="utf-8").write(s)

def build_misc():
    urls = [""] + ["hizmetler/", "bolgeler/", "hakkimizda/", "sss/", "iletisim/"] + [f"hizmetler/{s['slug']}/" for s in SERVICES] + [d["path"] for d in D]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        pr = "1.0" if u == "" else ("0.9" if u.startswith("bolgeler/") and u != "bolgeler/" else "0.8")
        sm += f"  <url><loc>{C['domain']}/{u}</loc><changefreq>weekly</changefreq><priority>{pr}</priority></url>\n"
    sm += "</urlset>\n"
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(sm)
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(f"User-agent: *\nAllow: /\n\nSitemap: {C['domain']}/sitemap.xml\n")
    if C.get("custom_domain"):
        open(os.path.join(OUT, "CNAME"), "w").write(C["domain"].replace("https://", "") + "\n")
    open(os.path.join(OUT, ".nojekyll"), "w").write("")
    os.makedirs(os.path.join(OUT, "assets/img"), exist_ok=True)
    open(os.path.join(OUT, "assets/img/logo.svg"), "w").write(LOGO.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'))
    open(os.path.join(OUT, "assets/img/favicon.svg"), "w").write(LOGO.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'))
    open(os.path.join(OUT, "assets/img/cekici.svg"), "w").write(TRUCK_ART.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" ', 1))
    return len(urls)

if __name__ == "__main__":
    if os.path.exists(OUT): shutil.rmtree(OUT)
    shutil.copytree(STATIC, OUT)
    build_home(); build_services(); build_districts(); build_about(); build_faq(); build_contact(); build_404()
    n = build_misc()
    print("OK", n, "sayfa")
