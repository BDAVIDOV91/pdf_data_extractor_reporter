import pdfplumber


def extract_text_from_pdf(pdf_path):
    extracted_text = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_text.append(text)

    return "\n".join(extracted_text)
