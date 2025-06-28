import re

def extract_invoice_data(text):
    """
    Enhanced invoice data extraction.
    - Keeps total even if currency is missing.
    - Uses stricter keywords and fallback logic.
    """
    lines = text.splitlines()

    invoice_number = None
    date = None
    client = None
    description = "N/A"
    total = None
    vat = None
    currency = None

    # --------- Client detection ---------
    for line in lines[:15]:
        if re.search(r"(Company Name|Получател|Client|Billed To)", line, re.IGNORECASE):
            match = re.search(r"(?:Company Name|Получател|Client|Billed To)[:\-]?\s*(.*)", line, re.IGNORECASE)
            if match:
                client = match.group(1).strip()
                break
        if re.search(r"(Ltd|ЕООД|ООД|АД)", line):
            client = line.strip()
            break

    # --------- Invoice number and date ---------
    for line in lines[:20]:
        if re.search(r"(Invoice\s*No|Фактура\s*№|Inv\s*#|No[:\-]?)", line, re.IGNORECASE):
            num_match = re.search(r"(?:Invoice\s*No|Фактура\s*№|Inv\s*#|No[:\-]?)\s*(\d+)", line, re.IGNORECASE)
            if num_match:
                invoice_number = num_match.group(1).strip()
        if re.search(r"(Date|Дата|Issued on)", line, re.IGNORECASE):
            date_match = re.search(r"([0-9]{2}[./\-][0-9]{2}[./\-][0-9]{4})", line)
            if date_match:
                date = date_match.group(1).strip()

    # --------- Totals (bottom-up) ---------
    for line in reversed(lines):
        if re.search(r"(Total|Общо|Amount Due|Grand Total|Amount)", line, re.IGNORECASE):
            total_match = re.search(r"([\d.,]+)", line)
            currency_match = re.search(r"(EUR|BGN|USD)", line)
            if total_match:
                total = total_match.group(1).strip()
            if currency_match:
                currency = currency_match.group(1).strip()
            break

    # --------- VAT (bottom-up) ---------
    for line in reversed(lines):
        if re.search(r"(VAT|ДДС|Tax)", line, re.IGNORECASE) and re.search(r"[\d.,]+", line):
            vat_match = re.search(r"([\d.,]+)", line)
            if vat_match:
                vat = vat_match.group(1).strip()
                break

    # --------- Description ---------
    for line in lines:
        if re.search(r"(Description|Описание)", line, re.IGNORECASE):
            desc_match = re.search(r"(?:Description|Описание)[:\-]?\s*(.*)", line, re.IGNORECASE)
            if desc_match and len(desc_match.group(1).strip()) > 3:
                description = desc_match.group(1).strip()
                break

    return {
        "invoice_number": invoice_number or "Not found",
        "date": date or "Not found",
        "client": client or "Not found",
        "description": description or "N/A",
        "total": total or "Not found",
        "vat": vat or "Not found",
        "currency": currency or "Not found"
    }
