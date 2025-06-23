from extractor import extract_text_from_pdf
from report_generator import save_report
from utils import extract_invoice_data

if __name__ == "__main__":
    sample_pdf = "samples/sample.pdf"
    extracted = extract_text_from_pdf(sample_pdf)
    
    if extracted:
        print("Extracted text:")
        print("-" * 50)
        print(extracted[:1000])  # limit output for readability
        
        # Save raw text report
        save_report(extracted, "sample_report.txt")
        
        # Parse structured invoice data
        parsed_data = extract_invoice_data(extracted)
        print("\nParsed invoice data:")
        print("-" * 50)
        print(parsed_data)
    else:
        print("No text could be extracted from the PDF.")
