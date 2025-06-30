# PDF Data Extractor & Reporter

This project automates extracting text and structured invoice data from PDF files and generates text reports, CSV, and Excel files.

## Features

- Extract text from PDF invoices
- Parse important invoice data:
  - Invoice number
  - Date
  - Client
  - Description (detailed item list)
  - Total
  - VAT
  - Currency
- Generate detailed text reports
- Export all parsed data into a cumulative CSV and Excel file
- Log all parsing operations and results to a separate log file

## Project Structure

- input_pdfs/
    Your PDF invoices here
- output_reports/
    Your generated reports and CSV/Excel
- logs/
    extraction_log.txt
- main.py
- extractor.py
- utils.py
- report_generator.py
- requirements.txt
- README.md

## Requirements

- Python 3.8 or higher (tested on 3.8)
- Install required packages:

- pip install -r requirements.txt

## Logging
- All operations, including start and completion of each file and any errors, are logged in logs/extraction_log.txt. This helps with tracking the process and debugging potential parsing issues

## Future Improvements

- Improve client and invoice number detection using better patterns.
- Add OCR support for scanned or image-based invoices (e.g., Tesseract).
- Add CLI options for more flexible batch runs (e.g., choose output formats, set custom output folder).
- Add support for more invoice layouts and formats.
- Add logging improvements (e.g., summary log at the end).
- Add optional web or GUI interface (consider in the future).

## License

- Open-source, free to use.

## Notes

- The extractor will save the total amount even if the currency is missing (marked as "Not found").
- If the currency is not explicitly specified in the invoice text, it will not be inferred automatically.
- Users should review the output reports and manually correct or fill in any missing currency if needed.