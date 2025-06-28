# PDF Data Extractor & Reporter

This Python project extracts text and structured data from PDF files (e.g. invoices), and exports it to `.txt`, `.csv`, and `.xlsx` formats. It is designed to help professionals—such as accountants, auditors, or researchers—quickly extract, review, and archive document information.

---

## ✅ Features

- 📄 Extracts text content from PDF invoices
- 📁 Batch mode: process all PDFs in `input_pdfs/`
- 📝 Saves `.txt` reports per file in `output_reports/`
- 📊 Exports parsed data to `invoices.csv` and `invoices.xlsx`
- 🧠 Extracts invoice number, date, customer, total, VAT, description
- 🔒 Handles missing files or directories gracefully
- 🧩 Modular and extendable codebase

---

## 📁 Project Structure

pdf_data_extractor_reporter/
│
├── input_pdfs/ # Place input PDF files here
├── output_reports/ # Extracted .txt, .csv, and .xlsx reports
├── samples/ # Sample/test PDFs
├── extractor.py # PDF text extraction logic
├── report_generator.py # Report saving utilities
├── utils.py # Invoice parsing functions
├── main.py # Entry script (batch processor)
├── ui.py # (Optional) GUI logic (future)
├── README.md # Project documentation
└── .gitignore # Ignores venv/, pycache, etc.


---

## 🚀 How to Use

1. Add your `.pdf` invoices into the `input_pdfs/` folder  
2. Run the script:

python3 main.py

## Each PDF will be:

- Processed and saved as output_reports/<filename>.txt
- Parsed data appended to invoices.csv and invoices.xlsx

## Example Output:

- Processing: INV1002.pdf
- Report saved successfully: output_reports/INV1002.txt
- Parsed data saved to CSV: output_reports/invoices.csv
- Parsed data saved to Excel: output_reports/invoices.xlsx


## Requirements
- Python 3.7+
- pdfplumber
- pandas
- openpyxl


## Install all with:
- pip install -r requirements.txt


## Batch Mode – Process Multiple PDFs
- To process all PDF files inside the input_pdfs/ directory in one run:

python3 main.py

## The script will:

- Extract text from each PDF

- Save the extracted content as .txt files in output_reports/

- Parse invoice data (invoice number, date, total, VAT, etc.)

- Save structured data to both invoices.csv and invoices.xlsx

- Ensure your PDFs are placed inside the input_pdfs/ folder before running.



## Future Improvements

- Add graphical user interface (GUI)
- Detect and adapt to multiple invoice formats
- Handle scanned PDFs (OCR support)
- Add CLI menu for user-friendly interaction
- Export to JSON

## Notes

- The extractor saves the total amount even if currency is missing (marked as "Not found").
- If currency is not specified explicitly in the invoice text, it will not be inferred automatically.
- Users are encouraged to review output reports and fill missing currency manually if needed.
