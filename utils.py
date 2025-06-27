import re

def extract_invoice_data(text):
    """
    Extracts invoice data using flexible patterns and optional matching.
    """
    def find_pattern(patterns, text):
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        return None

    invoice_number = find_pattern([
        r"Invoice\s*No[:\-]?\s*(\w+)",
        r"Inv(?:oice)?\s*#[:\-]?\s*(\w+)",
        r"Number[:\-]?\s*(\w+)"
    ], text)

    date = find_pattern([
        r"Date[:\-]?\s*([0-9]{2}/[0-9]{2}/[0-9]{4})",
        r"Issued on[:\-]?\s*([0-9]{2}/[0-9]{2}/[0-9]{4})"
    ], text)

    total = find_pattern([
        r"Total[:\-]?\s*([\d.,]+)",
        r"Amount Due[:\-]?\s*([\d.,]+)"
    ], text)

    vat = find_pattern([
        r"(?:VAT|Tax|Value Added Tax)[:\-]?\s*([\d.,]+)"
    ], text)

    customer = find_pattern([
        r"Customer[:\-]?\s*([^\n\r]+)",
        r"Billed To[:\-]?\s*([^\n\r]+)"
    ], text)

    description = find_pattern([
        r"Description[:\-]?\s*(.+?)(?:\n|$)"
    ], text)

    return {
        "invoice_number": invoice_number or "Not found",
        "date": date or "Not found",
        "total": total or "Not found",
        "vat": vat or "Not found",
        "customer": customer or "Not found",
        "description": description or "Not found"
    }
