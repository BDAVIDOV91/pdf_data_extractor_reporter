import os
from extractor import extract_text_from_pdf
from report_generator import save_report, save_parsed_to_csv
from utils import extract_invoice_data

INPUT_FOLDER = "input_pdfs"

if __name__ == "__main__":
    pdf_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in input_pdfs/")
    else:
        for pdf_file in pdf_files:
            file_path = os.path.join(INPUT_FOLDER, pdf_file)
            print(f"\nProcessing: {pdf_file}")
            
            extracted = extract_text_from_pdf(file_path)
            
            if extracted:
                # Save raw text
                txt_filename = pdf_file.replace(".pdf", ".txt")
                save_report(extracted, txt_filename)
                
                # Extract structured data
                parsed_data = extract_invoice_data(extracted)
                print("Parsed data:")
                print(parsed_data)

                # Save to CSV
                save_parsed_to_csv(parsed_data, "invoices.csv")
            else:
                print(f"Could not extract text from {pdf_file}")
