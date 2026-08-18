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
    slug: "kablo-koruma",
    title: "Kablo koruma",
    description: "Spiral boru, metal spiral ve kablo koruma aksesuarları.",
    intro: "Kabloları mekanik etkilerden korumaya ve tesisat güzergâhını düzenlemeye yardımcı ürün grupları.",
    eyebrow: "Altyapıyı koru",
  },
  {
    slug: "kablo-rakor",
    title: "Kablo rakorları",
    description: "Polyamid, metal, EMC ve Ex uyumlu kablo rakorları.",
    intro: "Pano, makine ve elektrik tesisatlarında kablo girişlerini düzenlemek için farklı diş ve gövde seçenekleri.",
    eyebrow: "Bağlantıyı tamamla",
  },
  {
    slug: "elektrik-boru",
    title: "Elektrik boruları",
    description: "PVC, PE, PP, EMT, IMC ve metal boru çözümleri.",
    intro: "Kablo güzergâhlarını korumak ve tesisat uygulamalarını düzenlemek için düz, spiral ve metal boru seçenekleri.",
    eyebrow: "Güzergâhı düzenle",
  },
  {
    slug: "kablo-kanali",
    title: "Kablo kanalları",
    description: "Hafif, orta, ağır ve sliding seri kablo taşıyıcıları.",
    intro: "Endüstriyel kablo yönetimi için açık, kapalı ve hareketli kablo kanalı çözümleri.",
    eyebrow: "Kabloları yönet",
  },
  {
    slug: "buat-aksesuar",
    title: "Buat & tesisat aksesuarları",
    description: "Buat, kroşe, kelepçe, bushing ve bağlantı aksesuarları.",
    intro: "Elektrik tesisatının montaj ve bağlantı adımlarını tamamlayan yardımcı ürünler.",
    eyebrow: "Montajı tamamla",
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
