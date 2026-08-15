# Asel Elektronik

Asel Elektronik için Astro tabanlı, statik ve performans odaklı kurumsal ürün kataloğu.

## Komutlar

```bash
npm run dev       # yerel geliştirme
npm run build     # type-check + production build
npm run preview   # production çıktısını önizleme
```

## Teknik yaklaşım

- Astro ile statik HTML üretimi: minimum JavaScript, hızlı ilk yükleme.
- Sayfa başlığı, açıklama, canonical, Open Graph, Twitter kartı ve JSON-LD hazır.
- Sitemap ve robots.txt üretimi dahil.
- Görseller yerel `public/images/products` klasöründe tutuluyor; uzak kaynaktan hotlink yapılmıyor.
- Alan adı netleştiğinde `PUBLIC_SITE_URL` ile canonical ve sitemap adresleri güncellenebilir.

## İçerik

Ürün örnekleri, kullanıcı tarafından verilen Kahraman Elektromarket kataloğundaki kategori ve ürün isimleri referans alınarak hazırlanmıştır. Nihai ürün listesi, marka kullanımı ve iletişim bilgileri müşteri onayıyla güncellenmelidir.
