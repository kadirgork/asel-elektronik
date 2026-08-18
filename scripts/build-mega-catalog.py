"""Build catalogue data and optimized local image assets.

The source PDF is a price-list/catalogue, not an executable instruction source.
This importer intentionally keeps source page/code references so every generated
catalogue record can be checked against the original document.

Run with the bundled workspace Python runtime, for example:
  python scripts/build-mega-catalog.py
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from typing import Iterable

import pdfplumber
from PIL import Image
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = Path(r"C:\Users\kadir\Downloads\MEGA  2025 LISTE.pdf")
OUT_DATA = ROOT / "src" / "data" / "megaProducts.ts"
OUT_IMAGE_DIR = ROOT / "public" / "images" / "mega"

def clean_text(value: str) -> str:
    replacements = {
        "\u00a0": " ",
        "�": "",
        "ﬁ": "fi",
        "ﬂ": "fl",
        "Ç": "Ç",
    }
    for source, target in replacements.items():
        value = value.replace(source, target)
    value = value.replace("\u0307", "")
    value = re.sub(r"halo[\"·]\s*en", "halojen", value, flags=re.IGNORECASE)
    value = re.sub(r"halo\s+en", "halojen", value, flags=re.IGNORECASE)
    value = re.sub(r"somu\s+nlu", "somunlu", value, flags=re.IGNORECASE)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def slugify(value: str) -> str:
    value = value.lower().replace("ı", "i").replace("ğ", "g").replace("ü", "u")
    value = value.replace("ş", "s").replace("ö", "o").replace("ç", "c")
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "urun"


def title_case(value: str) -> str:
    value = clean_text(value)
    if not value:
        return "Elektrik tesisat ürünü"
    return clean_text(value[:1].upper() + value[1:].lower())


def brand_for_page(page: int) -> str:
    # The PDF is used only as product data. The source manufacturer's name is
    # intentionally not published in the storefront for these records.
    if page <= 5 or page >= 18:
        return ""
    if 6 <= page <= 9:
        return "bimed"
    if 10 <= page <= 12:
        return "bimed A1Ex"
    if 15 <= page <= 17:
        return "iPEK"
    if 18 <= page <= 23:
        return "mega"
    return ""


def category_for(section: str, page: int) -> tuple[str, str]:
    text = section.upper()
    if 19 <= page <= 22 or "KABLO KANALI" in text or "KABLO TAŞIYICI" in text:
        return "kablo-kanali", "Kablo kanalları ve taşıyıcılar"
    if any(word in text for word in ("BUAT", "ANAHTAR KASA", "KROŞE", "KONDULET")):
        return "buat-aksesuar", "Buat ve tesisat aksesuarları"
    if any(word in text for word in ("BORU", "EMT", "IMC", "KANGAL", "BUSHING", "U-BOLT")):
        return "elektrik-boru", "Elektrik boruları ve bağlantı parçaları"
    if any(word in text for word in ("RAKOR", "SOMUN", "TAPA", "ADAPT", "REDÜKS", "KABLO RAKOR")):
        return "kablo-rakor", "Kablo rakorları ve bağlantı ekipmanları"
    return "kablo-koruma", "Kablo koruma sistemleri"


def is_heading(line: str) -> bool:
    line = clean_text(line)
    if not line or len(line) > 95:
        return False
    if any(token in line.upper() for token in ("KOD", "FİYAT", "EURO", "DOLAR", "ADET", "WWW.", "TEKNİK BİLGİ")):
        return False
    keywords = (
        "SPİRAL", "BORU", "RAKOR", "REKOR", "KABLO", "SOMUN", "TAPA", "DİRSEK", "KROŞE", "KUTU",
        "BUAT", "KANALI", "SERİ", "KANGAL", "ADAPT", "REDÜKS", "BUSHING", "U-BOLT",
        "EMT", "IMC", "KONDULET", "KASA", "MUF", "KELEPÇE", "KÖRTAPA", "POLYAMİD",
        "POLİAMİD", "METAL", "PİRİNÇ", "PVC", "PP ", "PE ", "ÇELİK", "GÜÇ",
    )
    return any(keyword in line.upper() for keyword in keywords)


def first_token_code(line: str, page: int) -> tuple[str | None, str]:
    """Return a best-effort code and a normalized source line.

    The catalogue was exported from FreeHand, so a few codes are separated by
    spaces (e.g. ``SH 1 014``). We repair only known code families.
    """
    source = clean_text(line)
    tokens = source.split()
    if not tokens:
        return None, source

    if page == 14:
        return None, source

    first = tokens[0].strip(".,;:")
    upper = first.upper()
    known_join = {
        "SH", "D8", "DE", "ME", "DHB", "DM", "KON", "SC", "FR", "SR", "SF", "HF",
    }
    if upper in known_join:
        join = [first]
        for token in tokens[1:4]:
            if re.fullmatch(r"[0-9A-Z.]+", token, re.I):
                join.append(token)
                if token.upper().endswith("R") or len(join) >= (3 if upper in {"SH", "SC", "FR"} else 2):
                    break
        first = "".join(join)
        upper = first.upper()
    elif re.match(r"^(?:SR[123]|SC[123]|HF1|FR[13]|5D[13]|SF[13]|CYS|CFS|DBS|GFS|SBR|ADS|ESM|D8|DHB|DM|KON|DE|ME)", upper):
        if len(tokens) > 1 and re.fullmatch(r"[0-9A-Z.]+", tokens[1], re.I):
            if upper.startswith(("SR", "SC", "HF", "FR", "5D", "SF")) or upper in {"DE", "ME", "DHB", "DM", "KON"}:
                first = first + tokens[1]
                upper = first.upper()

    if not re.search(r"\d", upper):
        return None, source
    if upper in {"M12X1", "M16X1", "M20X1", "M25X1", "M32X1", "M40X1", "M50X1", "M63X1"}:
        return None, source
    if upper.startswith(("RAL", "MAX", "SW", "TL", "TD")):
        return None, source
    if not re.match(r"^[A-Z0-9][A-Z0-9./_-]{1,}$", upper):
        return None, source
    return first.replace(" ", ""), source


def section_image_index(page: int, section_index: int) -> int | None:
    # These are representative product photos embedded in the PDF. The page
    # background, logo, header strips and telephone icon are intentionally skipped.
    choices = {
        2: [2, 10, 13, 14], 3: [3, 6, 8], 4: [3, 4, 6], 5: [3, 4, 5],
        6: [6, 7, 11], 7: [4, 5], 8: [3, 4], 9: [3, 4, 7], 10: [3, 4],
        11: [3, 4], 12: [3], 13: [5, 6, 7, 8, 9], 14: [3, 4, 6, 7],
        15: [3, 4, 5], 16: [3, 4, 5, 6], 17: [3, 4, 5], 18: [3, 4, 5],
        19: [3, 4, 5, 6], 20: [3, 4, 5], 21: [3, 4, 5], 22: [3, 4, 5],
        23: [3, 4, 5], 25: [3, 4, 6],
    }
    values = choices.get(page, [])
    return values[section_index % len(values)] if values else None


def save_pdf_images(reader: PdfReader) -> dict[tuple[int, int], str]:
    OUT_IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    image_paths: dict[tuple[int, int], str] = {}
    for page_number, page in enumerate(reader.pages, 1):
        if page_number not in set(range(2, 24)) | {25, 24, 26, 27}:
            continue
        for image_index, image_object in enumerate(page.images):
            try:
                image = image_object.image.convert("RGB")
                # Avoid publishing tiny decorative strips/icons as product art.
                if image.width < 90 or image.height < 80:
                    continue
                image.thumbnail((900, 900), Image.Resampling.LANCZOS)
                filename = f"p{page_number:02d}-{image_index:02d}.webp"
                path = OUT_IMAGE_DIR / filename
                image.save(path, "WEBP", quality=78, method=6)
                image_paths[(page_number, image_index)] = f"/images/mega/{filename}"
            except Exception:
                continue
    return image_paths


def image_for(page: int, section_index: int, image_paths: dict[tuple[int, int], str]) -> str:
    if page == 24:
        indexes = [0, 1, 2, 3, 4, 5, 6, 7]
    elif page == 26:
        indexes = [0, 1, 2, 3, 4, 5, 6, 7]
    elif page == 27:
        indexes = list(range(18))
    else:
        choices = section_image_index(page, section_index)
        indexes = [choices] if choices is not None else []
    for index in indexes:
        if (page, index) in image_paths:
            return image_paths[(page, index)]
    return "/images/og-cover.svg"


def source_price(line: str) -> str | None:
    # Keep prices as source metadata only; the storefront asks for a current
    # quote because the document is a July 2025 price list.
    values = re.findall(r"(?<![A-Za-z])\d+[,.]\d{2}(?!\d)", line)
    return values[-1].replace(",", ".") if values else None


def code_tokens(line: str) -> list[str]:
    return re.findall(r"\bB(?:/|-)?[A-Z0-9]+(?:[-/][A-Z0-9]+)*", line.upper())


def manual_products() -> list[dict]:
    items: list[dict] = []

    def add(page: int, section: str, codes: Iterable[str], sizes: Iterable[str] | None = None, colors: Iterable[str] | None = None, image_index: int | None = None):
        sizes_list = list(sizes or [])
        colors_list = list(colors or [])
        for index, code in enumerate(codes):
            size = sizes_list[index] if index < len(sizes_list) else None
            color = colors_list[index] if index < len(colors_list) else None
            items.append({
                "page": page,
                "section": section,
                "code": code,
                "size": size,
                "color": color,
                "imageIndex": image_index,
                "line": f"{code} {size or ''} {color or ''}",
            })

    sizes = ['1/2"', '3/4"', '1"', '1 1/4"', '1 1/2"', '2"']
    add(24, "Vidalı buat rakoru", [f"DE 50{i}" for i in range(1, 7)], sizes, image_index=0)
    add(24, "Vidalı boru mufu", [f"DE 51{i}" for i in range(1, 7)], sizes, image_index=1)
    add(24, "Sıkmalı buat rakoru", [f"DE 60{i}" for i in range(1, 7)], sizes, image_index=2)
    add(24, "Sıkmalı buat mufu", [f"DE 61{i}" for i in range(1, 7)], sizes, image_index=3)
    add(24, "EMT kroşe tek delikli", [f"DE 53{i}" for i in range(1, 7)], sizes, image_index=4)
    add(24, "EMT kroşe çift delikli", [f"DE 52{i}" for i in range(1, 7)], sizes, image_index=5)
    add(24, "Boru taşıma kelepçesi", [f"DE 60{i}1" for i in range(1, 7)], sizes, image_index=6)
    add(24, "Boru taşıma kelepçesi", [f"ME 60{i}1" for i in range(1, 7)], sizes, image_index=7)

    add(26, "Vidalı spiral EMT bağlantı mufu", ["DE180", "DE181", "DE182"], sizes[:3], image_index=0)
    add(26, "Metal bushing", [str(value) for value in range(281, 290)], sizes + ["2 1/2\"", "3\"", "4\""], image_index=1)
    add(26, "Plastik bushing", [f"{value}P" for value in range(281, 290)], sizes + ["2 1/2\"", "3\"", "4\""], image_index=2)
    add(26, "Spiral boru bağlantı mufu", [f"DE 46{i}" for i in range(1, 7)], sizes, image_index=3)
    add(26, "Boru bükme aparatı", [f"GL-84{i}H" for i in range(0, 4)], sizes[:4], image_index=4)
    add(26, "Boru kesme aparatı", ["GL-BC"], ["1/2\"–2\""], image_index=5)
    add(26, "U-bolt", ["UB050", "UB075", "UB100", "UB125", "UB150", "UB200"], sizes, image_index=6)
    add(26, "Redüksiyon", [f"RB{i}" for i in range(2, 17)], image_index=7)

    add(27, "PVC entül EMT-IMC", ["EN12", "EN34", "EN100", "EN114", "EN112", "EN200", "EN212", "EN300"], sizes[:3] + ['1 1/4"', '1 1/2"', '2"', '2 1/2"', '3"'], colors=["Siyah"], image_index=0)
    add(27, "PVC entül EMT-IMC", ["DENT12", "DENT34", "DENT1", "DENT11/4", "DENT11/2", "DENT2", "DENT21/2", "DENT3"], sizes[:3] + ['1 1/4"', '1 1/2"', '2"', '2 1/2"', '3"'], colors=["Beyaz"], image_index=0)
    add(27, "Vidalı spiral rakoru", [str(value) for value in range(151, 157)], sizes, image_index=3)
    add(27, "Vidalı spiral rakoru 90°", [str(value) for value in range(101, 107)], sizes, image_index=4)
    add(27, "Dikdörtgen buat", ["DE58361", "DE58362"], ['1/2"', '3/4"'], image_index=5)
    add(27, "Kare buat 102x102x38", ["DE52151", "DE52152", "DE52153", "DE52154"], ['1/2"', '3/4"', '1/2" & 3/4"', '1/2" & 3/4" con.'], image_index=6)
    add(27, "Köşeli buat 102x102x38", ["DE54151", "DE54152", "DE54153"], ['1/2"', '3/4"', '1/2" & 3/4"'], image_index=7)
    add(27, "Anahtar kasası", ["TK", "ÇK"], ["Tekli anahtar kasası", "Çiftli anahtar kasası"], image_index=8)

    return items


def extract_rows(text_by_page: dict[int, str]) -> list[dict]:
    rows: list[dict] = []
    excluded_prefixes = {"KOD", "ÖLÇÜ", "OLÇU", "AÇIKLAMA", "FİYATI", "DOLAR", "EURO", "WWW", "ELEKTRİK"}
    for page, text in text_by_page.items():
        if page in {1, 24, 26, 27, 28}:
            continue
        section = "Kablo koruma sistemi"
        section_index = 0
        for raw_line in text.splitlines():
            line = clean_text(raw_line)
            if not line or line.isdigit() or line.lower().startswith("www."):
                continue
            preview_code, _ = first_token_code(line, page)
            if is_heading(line) and not preview_code:
                section = line
                section_index += 1
                continue
            if any(line.upper().startswith(prefix) for prefix in excluded_prefixes):
                continue

            # Page 14 contains several columns of adapter/reducer codes on a
            # single line. Keep every visible code as a catalogue record.
            if page == 14:
                tokens = code_tokens(line)
                if tokens:
                    for token in tokens:
                        rows.append({"page": page, "section": section, "code": token, "line": line, "imageIndex": 11})
                continue

            # Bimed tables place three colour-specific codes at the end of each
            # row. Preserve each colour as an individual variant.
            if page == 6 and re.match(r"^(PG|M\d|NPT)", line, re.I):
                codes = re.findall(r"\b(?:BS|BM|BSPA|BSPC|BSPD|EG)-?\w+", line.upper())
                if codes:
                    colors = ["RAL 7001", "RAL 7035", "RAL 9005"]
                    for index, code in enumerate(codes[:3]):
                        rows.append({"page": page, "section": section, "code": code, "color": colors[index], "line": line, "imageIndex": 3})
                    continue

            if page in {7, 8, 10, 11, 12}:
                # Codes can be embedded after dimensional columns. Capturing
                # the code keeps the row searchable even when a PDF column has
                # split a measurement into several text fragments.
                candidates = re.findall(r"\b(?:BSBC|BMBC|BNBC|BDSM|BSEM|BMEM|HIBM|BM-X|BP-X|BN-X|HITP-X|BU|KBA)[A-Z0-9*-]*\w*", line.upper())
                if candidates:
                    for code in dict.fromkeys(candidates):
                        rows.append({"page": page, "section": section, "code": code, "line": line, "imageIndex": 3})
                    continue

            code, normalized = first_token_code(line, page)
            if not code:
                continue
            rows.append({"page": page, "section": section, "code": code, "line": normalized, "imageIndex": section_index})
    return rows


def build_records(pdf_text: dict[int, str], image_paths: dict[tuple[int, int], str]) -> list[dict]:
    raw_rows = extract_rows(pdf_text) + manual_products()
    records: list[dict] = []
    seen: set[tuple[int, str, str | None]] = set()
    for row in raw_rows:
        page = int(row["page"])
        code = clean_text(str(row.get("code", ""))).replace(" ", "")
        if not code or len(code) < 2:
            continue
        if code.upper() in {"BIMEDA1EX", "BIMED", "MEGA", "IPEK"}:
            continue
        code = code.replace("5D", "SD") if code.upper().startswith("5D") else code
        section = clean_text(str(row.get("section", "Kablo koruma sistemi")))
        color = clean_text(str(row["color"])) if row.get("color") else None
        key = (page, code.upper(), color)
        if key in seen:
            continue
        seen.add(key)
        category_slug, category = category_for(section, page)
        brand = brand_for_page(page)
        title_section = title_case(section)
        suffix = f" · {row['size']}" if row.get("size") else ""
        if color:
            suffix += f" · {color}"
        title = f"{title_section} {code}{suffix}"
        slug = slugify(f"{brand}-{title}")
        description = (
            f"{title_section} ürün grubunda yer alan {code} kodlu katalog seçeneği. "
            f"{('Renk: ' + color + '. ') if color else ''}"
            f"Ölçü, bağlantı tipi ve uygulama detayları için ürün teknik tablosunu inceleyin; güncel stok ve teklif bilgisi için Asel Elektronik ekibine danışın."
        )
        source_price_value = source_price(str(row.get("line", "")))
        specs = [
            {"label": "Katalog kodu", "value": code},
            {"label": "Marka / seri", "value": brand},
            {"label": "Katalog bölümü", "value": title_section},
            {"label": "Katalog sayfası", "value": str(page)},
        ]
        if row.get("size"):
            specs.insert(1, {"label": "Ölçü / seçenek", "value": str(row["size"])})
        if color:
            specs.insert(2, {"label": "Renk", "value": color})
        if source_price_value:
            specs.append({"label": "Kaynak liste", "value": f"Temmuz 2025 PDF · {source_price_value} (referans)"})
        image_index = row.get("imageIndex")
        if page in {24, 26, 27} and image_index is not None:
            image = image_paths.get((page, int(image_index)), "/images/og-cover.svg")
        else:
            image = image_for(page, int(image_index or 0), image_paths)
        records.append({
            "slug": slug,
            "brand": brand,
            "title": title,
            "category": category,
            "categorySlug": category_slug,
            "highlight": f"Katalogdan {title_section.lower()} çözümü.",
            "description": description,
            "image": image,
            "sourceUrl": "",
            "catalogCode": code,
            "catalogPage": page,
            "catalogSection": title_section,
            "color": color,
            "sourcePrice": source_price_value,
            "price": 100,
            "priceCurrency": "TRY",
            "specs": specs,
            "features": [
                "Katalog kodu ve varyant bilgisiyle kolay tekliflendirme",
                "Elektrik tesisatı ve kablo yönetimi uygulamalarına uygun ürün grubu",
                "Proje koşullarına göre teknik seçim ve tedarik danışmanlığı",
            ],
            "useCases": ["Pano ve makine bağlantıları", "Kablo koruma ve tesisat uygulamaları", "Endüstriyel elektrik projeleri"],
        })
    records.sort(key=lambda item: (item["catalogPage"], item["catalogSection"], item["catalogCode"], item.get("color") or ""))
    used_slugs: set[str] = set()
    for record in records:
        base_slug = record["slug"]
        candidate = base_slug
        if candidate in used_slugs:
            candidate = f"{base_slug}-p{record['catalogPage']}-{slugify(record['catalogCode'])}"
            counter = 2
            while candidate in used_slugs:
                candidate = f"{base_slug}-p{record['catalogPage']}-{slugify(record['catalogCode'])}-{counter}"
                counter += 1
            record["slug"] = candidate
        used_slugs.add(record["slug"])
    return records


def write_typescript(records: list[dict]) -> None:
    payload = json.dumps(records, ensure_ascii=False, indent=2)
    content = (
        "// Generated from the user-provided catalogue PDF.\n"
        "// Do not edit manually; run scripts/build-mega-catalog.py to refresh.\n"
        "import type { Product } from \"./products\";\n\n"
        f"export const megaProducts: Product[] = {payload};\n"
    )
    OUT_DATA.parent.mkdir(parents=True, exist_ok=True)
    OUT_DATA.write_text(content, encoding="utf-8")


def main() -> None:
    if not PDF_PATH.exists():
        raise SystemExit(f"PDF bulunamadı: {PDF_PATH}")
    with pdfplumber.open(PDF_PATH) as pdf:
        text_by_page = {index + 1: (page.extract_text(x_tolerance=1, y_tolerance=3) or "") for index, page in enumerate(pdf.pages)}
    reader = PdfReader(str(PDF_PATH))
    image_paths = save_pdf_images(reader)
    records = build_records(text_by_page, image_paths)
    write_typescript(records)
    print(f"{len(records)} katalog ürünü oluşturuldu")
    print(f"{len(image_paths)} optimize katalog görseli oluşturuldu")
    print(f"Çıktı: {OUT_DATA}")


if __name__ == "__main__":
    main()
