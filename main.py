from extractor import extract_text_from_pdf
from report_generator import save_report, save_parsed_to_csv, save_parsed_to_excel
from utils import extract_invoice_data
import os

def log_to_file(filename, text):
    if not os.path.exists("logs"):
        os.makedirs("logs")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text + "\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    input_dir = "input_pdfs"
    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".pdf")]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_dir, pdf_file)
        print(f"\nProcessing: {pdf_file}")

        extracted = extract_text_from_pdf(pdf_path)
        if extracted:
            report_name = f"{os.path.splitext(pdf_file)[0]}.txt"
            save_report(extracted, report_name)

            parsed_data = extract_invoice_data(extracted)
            print("Parsed data:")
            print(parsed_data)

            save_parsed_to_csv(parsed_data, "invoices.csv")
            save_parsed_to_excel(parsed_data, "invoices.xlsx")

            # Logging
            log_entry = f"Parsed data for {pdf_file}:\n{parsed_data}"
            log_to_file("logs/extraction_log.txt", log_entry)
        else:
            print("No text could be extracted from the PDF.")
