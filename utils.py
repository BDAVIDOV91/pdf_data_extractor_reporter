import re

def extract_invoice_data(text):
    """
    Extract invoice data with fallback logic and more flexible regex patterns.
    """
    data = {}

    # Invoice number
    invoice_number = re.search(r"Invoice[\s:]*([0-9]{4,})", text, re.IGNORECASE)
    if not invoice_number:
        invoice_number = re.search(r"№\s*(\d+)", text)
    data["invoice_number"] = invoice_number.group(1) if invoice_number else "Not found"

    # Date
    date = re.search(r"Date[\s:]*([\d]{2}\.[\d]{2}\.[\d]{4})", text)
    if not date:
        date = re.search(r"(\d{2}\.\d{2}\.\d{4})", text)
    data["date"] = date.group(1) if date else "Not found"

    # Client
    client = re.search(r"Company Name[:\s]*(.*?)(\n|$)", text, re.IGNORECASE)
    if not client:
        client = re.search(r"Customer[:\s]*(.*?)(\n|$)", text, re.IGNORECASE)
    data["client"] = client.group(1).strip() if client else "Not found"

    # Description
    desc = re.search(r"Description[\s:]*([\w\s\-.,]*)", text, re.IGNORECASE)
    data["description"] = desc.group(1).strip() if desc and desc.group(1).strip() else "N/A"

    # Total
    total = re.search(r"Total[\s:]*([\d.,]+)", text, re.IGNORECASE)
    if not total:
        total = re.search(r"Amount Due[\s:]*([\d.,]+)", text, re.IGNORECASE)
    if total:
        value = total.group(1).replace(",", ".").strip()
        data["total"] = value if value else "Not found"
    else:
        data["total"] = "Not found"

    # VAT
    vat = re.search(r"VAT[\s:]*([\d.,]+)", text, re.IGNORECASE)
    data["vat"] = vat.group(1).replace(",", ".") if vat else "Not found"

    # Currency
    currency = re.search(r"(BGN|EUR|USD|GBP)", text)
    data["currency"] = currency.group(1) if currency else "Not found"

    # Validate suspicious values
    if data["vat"] and (len(data["vat"]) < 1 or not re.match(r"^\d+(\.\d+)?$", data["vat"])):
        data["vat"] = "Invalid"
    if data["total"] and (len(data["total"]) < 1 or not re.match(r"^\d+(\.\d+)?$", data["total"])):
        data["total"] = "Invalid"

    return data
