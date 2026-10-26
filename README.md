# Ersan Oto Kurtarma — Web Sitesi

7/24 Antakya & Hatay oto çekici sitesi. Saf HTML/CSS/JS — sunucu, veritabanı veya derleme gerekmez. GitHub Pages'te ücretsiz yayınlanır.

## İçerik (27 sayfa)

- Ana sayfa, Hizmetler, Bölgeler, Hakkımızda, S.S.S, İletişim, 404
- 6 hizmet sayfası: Araç Çekme, Araç Kurtarma, Yol Yardım, Araç Taşıma, Şehirlerarası Oto Kurtarma, 7/24 Oto Çekici
- 15 ilçe sayfası: Antakya, Defne, İskenderun, Arsuz, Belen, Dörtyol, Payas, Erzin, Kırıkhan, Kumlu, Reyhanlı, Hassa, Samandağ, Yayladağı, Altınözü
- Her sayfada: sabit **Ara** ve **WhatsApp** butonları (mobilde alt bar, masaüstünde sağ altta), "Konumumu WhatsApp ile Gönder" butonu
- SEO: her sayfaya özel başlık/açıklama, Schema.org (işletme, hizmet, SSS, breadcrumb), `sitemap.xml`, `robots.txt`

## GitHub Pages'te yayınlama

1. github.com'da **New repository** → isim ör. `ersanotokurtarma` → **Public** → Create.
2. Repo sayfasında **Add file → Upload files** → bu klasörün **içindeki** tüm dosya ve klasörleri sürükleyip bırakın (`index.html` repo kökünde olmalı) → **Commit changes**.
3. **Settings → Pages** → Source: **Deploy from a branch** → Branch: `main` / `/ (root)` → **Save**.
4. 1-2 dakika sonra site `https://KULLANICIADI.github.io/ersanotokurtarma/` adresinde açılır.

### Kendi alan adınızı bağlama (ersanotokurtarma.com)

Klasörde `CNAME` dosyası var ve içinde `ersanotokurtarma.com` yazıyor.
- Alan adı sağlayıcınızın DNS paneline şu kayıtları girin:
  - `A` kayıtları (@): `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
  - `CNAME` kaydı (www): `KULLANICIADI.github.io`
- GitHub → Settings → Pages → Custom domain alanında alan adını görün, **Enforce HTTPS** kutusunu işaretleyin.
- Alan adı kullanmayacaksanız `CNAME` dosyasını silin.

> Not: Alan adı şu an başka bir sitede yayındaysa, DNS'i değiştirdiğiniz anda yeni site yayına girer.

## Bilgileri değiştirme

Telefon, adres, e-posta, isim gibi bilgiler tüm sayfalarda tekrar ettiği için en kolay yol `generate.py` dosyasının başındaki `CONFIG` bölümünü düzenleyip `python3 generate.py` çalıştırmaktır; tüm sayfalar yeniden üretilir. (Kaynak dosyalar ayrı pakette: `kaynak/`.)

Küçük bir metin düzeltmesi için ilgili `index.html` dosyasını GitHub'da kalem ikonuyla doğrudan da düzenleyebilirsiniz.

## Gerçek fotoğraf ekleme

Şu an çekici görseli çizim (SVG). Kendi çekici fotoğraflarınızı `assets/img/` içine yükleyip `assets/img/og-image.png` dosyasını (1200×630) gerçek bir fotoğrafla değiştirmeniz paylaşımlarda ve Google'da daha iyi görünür.

## Yayından sonra

- Google Search Console'a siteyi ekleyip `sitemap.xml` gönderin.
- Google İşletme Profili'nde web sitesi olarak bu adresi girin.
