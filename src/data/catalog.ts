export type Category = {
  slug: string;
  title: string;
  description: string;
  intro: string;
  eyebrow: string;
};

export const categories: Category[] = [
  {
    slug: "aydinlatma",
    title: "Aydınlatma",
    description: "LED, dekoratif, dış mekân ve endüstriyel aydınlatma.",
    intro: "İç ve dış mekânlar için verimli, güvenli ve amaca uygun aydınlatma çözümleri.",
    eyebrow: "Işığı doğru kullan",
  },
  {
    slug: "anahtar-priz",
    title: "Anahtar & priz",
    description: "Modern mekanlar için modüler anahtar, priz ve aksesuarlar.",
    intro: "Günlük yaşamın her anında güven veren, sade ve uyumlu elektrik aksesuarları.",
    eyebrow: "Kontrol sende",
  },
  {
    slug: "kablolama",
    title: "Kablolama",
    description: "Enerji, zayıf akım, data ve solar kablo çözümleri.",
    intro: "Enerjiyi ve veriyi güvenle taşıyan doğru kablo seçimiyle sağlam altyapılar.",
    eyebrow: "Altyapını güçlendir",
  },
  {
    slug: "diafon-guvenlik",
    title: "Diafon & güvenlik",
    description: "Kamera, yangın, görüntülü ve sesli diafon sistemleri.",
    intro: "Konut, ofis ve işletmeler için erişim, iletişim ve güvenlik çözümleri.",
    eyebrow: "Güvenli alanlar",
  },
  {
    slug: "otomasyon-salt",
    title: "Otomasyon & şalt",
    description: "Sigorta, kontaktör, röle ve pano ekipmanları.",
    intro: "Elektrik sistemlerini korumak, kontrol etmek ve daha verimli yönetmek için ekipmanlar.",
    eyebrow: "Sistemi yönet",
  },
  {
    slug: "isitma-sogutma",
    title: "Isıtma & soğutma",
    description: "Fan, ısıtıcı ve havalandırma ürünleri.",
    intro: "Yaşam ve çalışma alanlarında konforu destekleyen ısıtma, soğutma ve hava çözümleri.",
    eyebrow: "Konforu ayarla",
  },
  {
    slug: "guc-urunleri",
    title: "Güç ürünleri",
    description: "Şarj istasyonu, UPS ve güç kaynağı seçenekleri.",
    intro: "Enerji sürekliliği ve yeni nesil mobilite için güvenilir güç çözümleri.",
    eyebrow: "Enerjiyi koru",
  },
  {
    slug: "teklif-proje",
    title: "Teklif & proje",
    description: "İhtiyaca göre ürün seçimi ve proje bazlı tedarik.",
    intro: "İhtiyacını birlikte analiz edip doğru ürün ve tedarik planını oluşturalım.",
    eyebrow: "Birlikte planla",
  },
];

export function getCategory(slug: string) {
  return categories.find((category) => category.slug === slug);
}
