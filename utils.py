import re

def extract_invoice_data(text: str) -> dict:
    """
    Extracts invoice fields from text with improved regex and fallback logic.
    """
    data = {
        "invoice_number": "Not found",
        "date": "Not found",
        "client": "Not found",
        "description": "N/A",
        "total": "Not found",
        "vat": "Not found",
        "currency": "Not found"
    }

    # Invoice number — ограничен до познати шаблони
    invoice_number_match = re.search(r"(Invoice\s*(No\.?)?|Фактура\s*№|№)\s*[:#]?\s*(\d{3,})", text, re.IGNORECASE)
    if invoice_number_match:
        data["invoice_number"] = invoice_number_match.group(3).strip()

    # Date
    date_match = re.search(r"\b\d{2}[./-]\d{2}[./-]\d{4}\b", text)
    if date_match:
        data["date"] = date_match.group(0)

    # Client
    client_match = re.search(r"(Company Name|Фирма|Client)\s*[:,]?\s*(.+)", text, re.IGNORECASE)
    if client_match:
        data["client"] = client_match.group(2).strip().splitlines()[0]
    else:
        # Check first 10 lines for keywords
        lines = text.splitlines()
        for line in lines[:10]:
            if any(keyword in line for keyword in ["Ltd", "EООД", "ООД", "Inc.", "Corp.", "GmbH"]):
                data["client"] = line.strip()
                break

    # Description
    item_lines = []
    for line in text.splitlines():
        if re.search(r"\d+\s+\S+.*\d+\.\d{2}\s+\d+\.\d{2}", line):
            item_lines.append(line.strip())
    if item_lines:
        data["description"] = "\n".join(item_lines)

    # Total (по-надежден fallback)
    total_match = re.search(r"(Total|Общо)\s*[:,]?\s*(\d+\.\d{2})", text, re.IGNORECASE)
    if total_match:
        data["total"] = total_match.group(2)
    else:
        # Alternative: последно срещнато число с формат xx.xx, което често е тотал
        last_amounts = re.findall(r"\b\d+\.\d{2}\b", text)
        if last_amounts:
            data["total"] = last_amounts[-1]

    # VAT
    vat_match = re.search(r"(VAT|ДДС)\s*[:,]?\s*(\d+\.\d{2})", text, re.IGNORECASE)
    if vat_match:
        data["vat"] = vat_match.group(2)

    # Currency
    currency_match = re.search(r"\b(EUR|BGN|USD|GBP)\b", text)
    if currency_match:
        data["currency"] = currency_match.group(1)

    return data
