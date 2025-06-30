from extractor import extract_text_from_pdf
from report_generator import save_report, save_parsed_to_csv, save_parsed_to_excel
from utils import extract_invoice_data
import os
import logging

# Setup logging
if not os.path.exists("logs"):
    os.makedirs("logs")

log_file = "logs/extraction_log.txt"
file_handler = logging.FileHandler(log_file, encoding="utf-8")
formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")
file_handler.setFormatter(formatter)

logging.basicConfig(
    level=logging.INFO,
    handlers=[file_handler]
)

if __name__ == "__main__":
    input_dir = "input_pdfs"
    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".pdf")]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_dir, pdf_file)
        print(f"\nProcessing: {pdf_file}")
        logging.info(f"Started processing: {pdf_file}")

        try:
            extracted = extract_text_from_pdf(pdf_path)
            if extracted:
                report_name = f"{os.path.splitext(pdf_file)[0]}.txt"
                save_report(extracted, report_name)

                parsed_data = extract_invoice_data(extracted)
                print("Parsed data:")
                print(parsed_data)

                save_parsed_to_csv(parsed_data, "invoices.csv")
                save_parsed_to_excel(parsed_data, "invoices.xlsx")

                logging.info(f"Successfully parsed: {pdf_file}")
                logging.info(f"Parsed data: {parsed_data}")
            else:
                logging.warning(f"No text extracted from: {pdf_file}")
                print("No text could be extracted from the PDF.")
        except Exception as e:
            logging.error(f"Error processing {pdf_file}: {e}")
            print(f"Error processing {pdf_file}: {e}")
