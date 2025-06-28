import re

def extract_invoice_data(text):
    """
    Smarter invoice data extraction logic: tries to analyze by lines, separate top (header) and bottom (totals).
    """
    lines = text.splitlines()

    invoice_number = None
    date = None
    client = None
    description = None
    total = None
    vat = None
    currency = None

    # --------- Step 1: Try to extract header data (first ~15 lines) ---------
    header_lines = lines[:15]

    for line in header_lines:
        # Invoice number
        if re.search(r"(Invoice\s*No|Фактура\s*№|Inv\s*#|No[:\-]?)", line, re.IGNORECASE):
            num_match = re.search(r"(?:Invoice\s*No|Фактура\s*№|Inv\s*#|No[:\-]?)\s*(\d+)", line, re.IGNORECASE)
            if num_match:
                invoice_number = num_match.group(1).strip()

        # Date
        if re.search(r"(Date|Дата|Issued on)", line, re.IGNORECASE):
            date_match = re.search(r"([0-9]{2}[./\-][0-9]{2}[./\-][0-9]{4})", line)
            if date_match:
                date = date_match.group(1).strip()

        # Client
        if re.search(r"(Company Name|Получател|Client|Billed To)", line, re.IGNORECASE):
            client_match = re.search(r"(?:Company Name|Получател|Client|Billed To)[:\-]?\s*(.*)", line, re.IGNORECASE)
            if client_match:
                client = client_match.group(1).strip()

    # --------- Step 2: Search for totals (usually near the end) ---------
    for line in reversed(lines):
        # Total and currency
        if re.search(r"(EUR|BGN|USD)", line) and re.search(r"\d", line):
            cur_match = re.search(r"(EUR|BGN|USD)", line)
            total_match = re.search(r"([\d.,]+)", line)
            if cur_match and total_match:
                currency = cur_match.group(1)
                total = total_match.group(1).strip()
                break

    # VAT
    for line in reversed(lines):
        if re.search(r"(VAT|ДДС|Tax)", line, re.IGNORECASE):
            vat_match = re.search(r"([\d.,]+)", line)
            if vat_match:
                vat = vat_match.group(1).strip()
                break

    # Description (fallback: first line with Description keyword)
    for line in lines:
        if re.search(r"(Description|Описание)", line, re.IGNORECASE):
            desc_match = re.search(r"(?:Description|Описание)[:\-]?\s*(.*)", line, re.IGNORECASE)
            if desc_match:
                description = desc_match.group(1).strip()
                break

    return {
        "invoice_number": invoice_number or "Not found",
        "date": date or "Not found",
        "client": client or "Not found",
        "description": description or "Not found",
        "total": total or "Not found",
        "vat": vat or "Not found",
        "currency": currency or "Not found"
    }
