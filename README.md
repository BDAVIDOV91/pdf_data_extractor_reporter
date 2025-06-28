# PDF Data Extractor & Reporter

This project automates extracting text and structured invoice data from PDF files and generates text reports, CSV, and Excel files.

## Features

- Extracts text from PDF invoices
- Flexible regex logic with fallback to handle different invoice formats
- Batch processing of multiple PDFs from `input_pdfs/` folder
- Exports parsed data to CSV and Excel
- Logs all parsed results to `logs/extraction_log.txt`
- Modular structure, ready for CLI or GUI extension

## Project Structure

- input_pdfs/ # Your PDF files
- output_reports/ # Text reports, CSV, Excel
- logs/ # Extraction logs
- samples/ # Example PDFs
- extractor.py # PDF extraction logic
- utils.py # Parsing logic and helpers
- report_generator.py # Save functions
- main.py # Main runner script
- README.md
- requirements.txt

## Installation

- pip install -r requirements.txt

## Each PDF will be:

- Processed and saved as output_reports/<filename>.txt
- Parsed data appended to invoices.csv and invoices.xlsx

## Batch Mode – Process Multiple PDFs

- To process all PDF files inside the input_pdfs/ directory in one run:
- python3 main.py

## Requirements

- Python 3.7+
- PyPDF2
- pdfminer.six
- pdfplumber
- pandas
- openpyxl

## The script will:

- Extract text from each PDF
- Save the extracted content as .txt files in output_reports/
- Parse invoice data (invoice number, date, total, VAT, etc.)
- Save structured data to both invoices.csv and invoices.xlsx
- Ensure your PDFs are placed inside the input_pdfs/ folder before running.

## Future Improvements

- CLI or GUI options
- OCR for scanned invoices
- Client-specific templates

## License
- Open-source, free to use.

## Notes

- The extractor saves the total amount even if currency is missing (marked as "Not found").
- If currency is not specified explicitly in the invoice text, it will not be inferred automatically.
- Users are encouraged to review output reports and fill missing currency manually if needed.
