from extractor import extract_text_from_pdf
from report_generator import save_report

if __name__ == "__main__":
    sample_pdf = "samples/sample.pdf"  # Replace with your PDF file path
    extracted = extract_text_from_pdf(sample_pdf)
    
    if extracted:
        print("Extracting text:")
        print("-" * 50)
        print(extracted)

        save_report(extracted, "sample_report.txt")
    else:
        print("No text could be extracted from the PDF.")
