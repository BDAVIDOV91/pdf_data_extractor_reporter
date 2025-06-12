# PDF Data Extractor & Reporter

This Python project extracts text from PDF files and saves it in a structured text format for review, storage, or reporting. It is designed to help professionals—such as accountants, auditors, or researchers—quickly extract and save information from documents.

## Features

- 📄 Extracts text content from PDF files
- 📝 Saves extracted text into clean `.txt` reports
- 📁 Handles missing directories and filenames gracefully
- 🧩 Modular code (organized in reusable components)
- 🧪 Ready for command-line use or further extension with a GUI

## Project Structure

pdf-extractor-project/
│
├── input_pdfs/ # Place your input PDF files here
├── output_reports/ # Extracted reports are saved here
├── samples/ # Example/sample PDFs
├── extractor.py # PDF text extraction logic
├── report_generator.py # Report saving utility
├── main.py # Entry point for running the tool
├── utils.py # (Optional) Utility/helper functions
├── ui.py # (Optional) GUI-related code (future)
├── README.md # Project description and usage
└── .gitignore # Ignores venv, output files, etc.


## License

- This project is open-source and free to use.

## Future Improvements

- Add graphical user interface (GUI)

- Extract metadata or tables

- Support batch PDF processing

- Export to formats like CSV or JSON


## Requirements

- Python 3.7+
- `PyPDF2` or other supported PDF libraries

Install dependencies:

```bash
pip install -r requirements.txt

