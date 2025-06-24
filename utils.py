import re

def extract_invoice_data(text):
    """
    Extracts basic invoice data from a block of text using regex.
    Returns a dictionary with the results.
    """
    data = {}

    # Adjust these patterns to match the structure of your PDFs
    invoice_number = re.search(r'Invoice\s*(No)?[:\-]?\s*(\w+)', text, re.IGNORECASE)
    date = re.search(r'Date[:\-]?\s*(\d{2}[./-]\d{2}[./-]\d{4})', text)
    total = re.search(r'Total[:\-]?\s*\$?(\d+\.\d{2})', text)
    vat = re.search(r'VAT[:\-]?\s*\$?(\d+\.\d{2})', text)
    customer = re.search(r'Customer[:\-]?\s*(.*)', text) 
    description = re.search(r'Description[:\-]?\s*(.+?)(\n|$)', text)


    if invoice_number:
        data['invoice_number'] = invoice_number.group(2)
    if date:
        data['date'] = date.group(1)
    if total:
        data['total'] = total.group(1)
    if vat:
        data['vat'] = vat.group(1)
    if customer:
        data['customer'] = customer.group(1).strip()
    if description:
        data['description'] = description.group(1).strip()

    return data