import { megaProducts } from "./megaProducts";

export type ProductSpec = {
  label: string;
  value: string;
};

export type Product = {
  slug: string;
  brand: string;
  title: string;
  category: string;
  categorySlug: string;
  highlight: string;
  description: string;
  image: string;
  sourceUrl: string;
  specs: ProductSpec[];
  features: string[];
  useCases: string[];
  catalogCode?: string;
  catalogPage?: number;
  catalogSection?: string;
  color?: string | null;
  sourcePrice?: string | null;
  price?: number;
  priceCurrency?: string;
};

const legacyProducts: Product[] = [
  {
    slug: "tuncmatik-22kw-pico-charger",
    brand: "Tunçmatik",
    title: "22kW Pico Charger AC Şarj İstasyonu",
    category: "Güç ürünleri",
    categorySlug: "guc-urunleri",
    highlight: "Elektrikli araçlar için akıllı ve güvenli şarj altyapısı.",
    description:
      "Elektrikli araç şarj altyapısı kurmak isteyen konut, işletme ve proje sahipleri için kompakt bir AC şarj çözümü.",
    image: "/images/products/pico-charger.png",
    sourceUrl:
      "https://www.kahramanelektromarket.com/urun/tuncmatik-22kw-pico-charger-ac-kablolu-sarj-istasyonu",
    specs: [
      { label: "Şarj gücü", value: "22 kW / 32A @400V 50Hz" },
      { label: "Soket tipi", value: "AC Type 2" },
      { label: "Kablo", value: "Standart 5 metre kablo" },
      { label: "Bağlantı", value: "Wi-Fi ve Bluetooth" },
      { label: "Koruma", value: "IP65 ve çoklu elektriksel koruma" },
    ],
    features: [
      "Mobil uygulama ile kontrol imkânı",
      "Aşırı akım, gerilim ve sıcaklık koruması",
      "Konut ve ticari kullanım için uygun kompakt tasarım",
    ],
    useCases: ["Villa ve konut otoparkları", "Site ve apartman otoparkları", "İşletme ve filo şarj noktaları"],
  },
  {
    slug: "orbus-vl1-tavan-vantilatoru",
    brand: "ORBUS",
    title: "VL1 Uzaktan Kumandalı Tavan Vantilatörü",
    category: "Isıtma & soğutma",
    categorySlug: "isitma-sogutma",
    highlight: "Aydınlatma ve hava sirkülasyonunu tek üründe buluşturur.",
    description:
      "Yaşam alanlarında hava sirkülasyonunu ve aydınlatmayı tek gövdede birleştiren, uzaktan kumandalı tavan vantilatörü.",
    image: "/images/products/orbus-vl1.jpg",
    sourceUrl:
      "https://www.kahramanelektromarket.com/urun/orbus-uzaktan-kumandali-tavan-vantilatoru-3000k-6500k-isik-ve-ayarlanabilir-fan-seviyeli-vl1",
    specs: [
      { label: "Ürün tipi", value: "Aydınlatmalı tavan vantilatörü" },
      { label: "Kontrol", value: "Uzaktan kumanda" },
      { label: "Aydınlatma", value: "3000K – 6500K ayarlanabilir ışık" },
      { label: "Kullanım", value: "İç mekân" },
    ],
    features: [
      "Ayarlanabilir fan seviyeleri",
      "Aydınlatma sıcaklığını değiştirme imkânı",
      "Salon, ofis ve ticari mekânlara uyumlu tasarım",
    ],
    useCases: ["Salon ve yaşam alanları", "Ofis ve çalışma alanları", "Kafe ve mağaza iç mekânları"],
  },
  {
    slug: "cata-akilli-solar-kamera-ct-4053",
    brand: "Cata",
    title: "Akıllı Solar SIM Kartlı Kamera CT-4053",
    category: "Güvenlik sistemleri",
    categorySlug: "diafon-guvenlik",
    highlight: "Uzaktan izleme ve güvenlik için pratik kamera çözümü.",
    description:
      "Elektrik altyapısının sınırlı olduğu alanlarda solar enerji ve SIM kart bağlantısıyla kullanılabilen akıllı kamera çözümü.",
    image: "/images/products/cata-camera.webp",
    sourceUrl:
      "https://www.kahramanelektromarket.com/urun/cata-akilli-solar-sim-kartli-kamera-ct-4053",
    specs: [
      { label: "Enerji", value: "Solar destekli" },
      { label: "Bağlantı", value: "SIM kart üzerinden mobil bağlantı" },
      { label: "Kullanım", value: "Dış ve yarı açık alanlar" },
      { label: "Ürün grubu", value: "Akıllı güvenlik kamerası" },
    ],
    features: [
      "Kablo altyapısının zor olduğu noktalarda kullanım",
      "Uzaktan izleme senaryolarına uygun yapı",
      "Güvenlik ihtiyacına göre proje bazlı konumlandırma",
    ],
    useCases: ["Müstakil yapılar", "Şantiye ve arsa çevreleri", "Depo ve işletme dış alanları"],
  },
  {
    slug: "gunsan-visage-komutator-vavien",
    brand: "Günsan",
    title: "Visage Komütatör Vavien",
    category: "Anahtar & priz",
    categorySlug: "anahtar-priz",
    highlight: "Modern mekanlar için sade, güvenilir ve modüler kontrol.",
    description:
      "Günsan Visage serisinin modüler yapısı içinde, aydınlatma kontrolünü sade ve uyumlu bir tasarımla tamamlayan komütatör vavien.",
    image: "/images/products/gunsan-komutator.png",
    sourceUrl:
      "https://www.kahramanelektromarket.com/urun/gunsan-visage-komutator-vavien-cercevesiz",
    specs: [
      { label: "Seri", value: "Visage" },
      { label: "Ürün tipi", value: "Komütatör vavien" },
      { label: "Montaj", value: "Modüler / çerçevesiz kullanım" },
      { label: "Kullanım", value: "İç mekân aydınlatma kontrolü" },
    ],
    features: [
      "Sade ve modern ön yüz",
      "Visage serisiyle modüler kombinasyon",
      "Konut ve ticari iç mekânlara uygun kullanım",
    ],
    useCases: ["Konut projeleri", "Ofis ve mağazalar", "Tadilat ve yenileme işleri"],
  },
  {
    slug: "altin-kablo-15-nya-kahverengi",
    brand: "Altın Kablo",
    title: "1,5 mm NYA Kablo · 100 metre",
    category: "Kablolar",
    categorySlug: "kablolama",
    highlight: "Elektrik tesisatları için güvenilir iletken ve kablolama.",
    description:
      "Tesisat uygulamalarında kullanılan, kahverengi dış renkli 1,5 mm NYA kablo seçeneği. Kesit ve metraj ihtiyaca göre teyit edilmelidir.",
    image: "/images/products/nya-kablo.jpg",
    sourceUrl:
      "https://www.kahramanelektromarket.com/urun/altin-15-nya-kablo-kahverengi-100-metre",
    specs: [
      { label: "Kablo tipi", value: "NYA / H07V-U" },
      { label: "Kesit", value: "1,5 mm²" },
      { label: "Renk", value: "Kahverengi" },
      { label: "Metraj", value: "100 metre" },
    ],
    features: [
      "Konut ve ticari tesisatlara uygun ürün grubu",
      "Renk kodlu kablolama planlarına uyum",
      "Proje metrajına göre tedarik danışmanlığı",
    ],
    useCases: ["Aydınlatma devreleri", "Konut elektrik tesisatları", "Pano ve dağıtım uygulamaları"],
  },
  {
    slug: "cata-2x20w-sinek-armatur-ct-9401",
    brand: "Cata",
    title: "2×20W Sinek Armatür CT-9401",
    category: "Aydınlatma",
    categorySlug: "aydinlatma",
    highlight: "İşletmeler ve yaşam alanları için etkili aydınlatma desteği.",
    description:
      "İşletme ve kapalı alanlarda kullanılmak üzere tasarlanan, 2×20W ürün grubunda sinek armatür çözümü.",
    image: "/images/products/cata-sinek.png",
    sourceUrl:
      "https://www.kahramanelektromarket.com/urun/cata-2x20-sinek-armatur-ct-9401",
    specs: [
      { label: "Güç", value: "2×20W" },
      { label: "Ürün tipi", value: "Sinek armatürü" },
      { label: "Kullanım", value: "İç mekân" },
      { label: "Marka", value: "Cata" },
    ],
    features: [
      "İşletme ve ortak alanlar için pratik çözüm",
      "Duvar veya uygun yüzeylerde konumlandırma",
      "Ürün uygulamasına göre keşif desteği",
    ],
    useCases: ["Market ve restoranlar", "Depo ve üretim alanları", "Balkon ve kapalı ortak alanlar"],
  },
  {
    slug: "tuncmatik-digitech-eco-1500va-ups",
    brand: "Tunçmatik",
    title: "Digitech ECO 1500VA UPS",
    category: "Kesintisiz güç",
    categorySlug: "guc-urunleri",
    highlight: "Kritik cihazları elektrik dalgalanmalarına karşı korur.",
    description:
      "Bilgisayar, ağ ekipmanı ve kritik elektronik cihazların enerji sürekliliğini desteklemek için kullanılan line-interactive UPS çözümü.",
    image: "/images/products/tuncmatik-ups.png",
    sourceUrl:
      "https://www.kahramanelektromarket.com/urun/tuncmatik-digitech-eco-1500va-2x9ah-line-interactive-ups",
    specs: [
      { label: "Kapasite", value: "1500 VA" },
      { label: "Topoloji", value: "Line-interactive" },
      { label: "Akü", value: "2×9Ah ürün grubu" },
      { label: "Kullanım", value: "Elektronik cihaz koruması" },
    ],
    features: [
      "Elektrik kesintilerinde kontrollü geçiş",
      "Gerilim dalgalanmalarına karşı koruma",
      "Ofis ve ev kullanıcıları için kompakt gövde",
    ],
    useCases: ["Bilgisayar ve çalışma istasyonları", "Modem ve ağ cihazları", "Güvenlik sistemleri"],
  },
  {
    slug: "luxell-duvar-tipi-infrared-ecoray",
    brand: "Luxell",
    title: "Duvar Tipi Infrared Ecoray Isıtıcı",
    category: "Isıtma & soğutma",
    categorySlug: "isitma-sogutma",
    highlight: "Kompakt mekanlar için hızlı ve kontrollü ısıtma.",
    description:
      "Duvar tipi kullanım senaryoları için tasarlanan infrared ısıtıcı; montaj alanı ve kullanım amacına göre değerlendirilebilir.",
    image: "/images/products/luxell-isitici.jpg",
    sourceUrl:
      "https://www.kahramanelektromarket.com/urun/luxell-duvar-tipi-infrared-ecoray-isitici-ex-23",
    specs: [
      { label: "Ürün tipi", value: "Duvar tipi infrared ısıtıcı" },
      { label: "Model", value: "Ecoray EX-23 ürün grubu" },
      { label: "Montaj", value: "Duvar tipi" },
      { label: "Kullanım", value: "İç ve yarı açık alan senaryoları" },
    ],
    features: [
      "Duvar montajıyla yer tasarrufu",
      "Kompakt alanlarda hızlı ısıtma yaklaşımı",
      "Kullanım alanına göre proje danışmanlığı",
    ],
    useCases: ["Balkon ve teraslar", "Kafe ve restoran alanları", "Atölye ve çalışma alanları"],
  },
];

export const products: Product[] = [...legacyProducts, ...megaProducts];

export const brands = [...new Set(products.map((product) => product.brand).filter(Boolean))].sort((a, b) => a.localeCompare(b, "tr"));

export function getBrandSlug(brand: string) {
  return brand
    .toLocaleLowerCase("tr-TR")
    .replaceAll("ı", "i")
    .replaceAll("ğ", "g")
    .replaceAll("ü", "u")
    .replaceAll("ş", "s")
    .replaceAll("ö", "o")
    .replaceAll("ç", "c")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
}

export function getBrand(slug: string) {
  return brands.find((brand) => getBrandSlug(brand) === slug);
}

export function getProduct(slug: string) {
  return products.find((product) => product.slug === slug);
}
