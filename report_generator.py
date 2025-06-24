import os
import pandas as pd

def save_report(text: str, filename: str, output_dir="output_reports"):
    """
    Saves the report as a text file inside the given directory.
    Creates the directory if it does not exist.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filepath = os.path.join(output_dir, filename)

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Report saved successfully: {filepath}")
    except Exception as e:
        print(f"Error saving report: {e}")

def save_parsed_to_csv(data: dict, filename: str, output_dir="output_reports"):
    """
    Saves the parsed invoice data into a CSV file.
    If file doesn't exist, creates it with headers.
    If file exists, appends a new row.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filepath = os.path.join(output_dir, filename)
    df = pd.DataFrame([data])  # One-row DataFrame

    if not os.path.exists(filepath):
        df.to_csv(filepath, index=False)
    else:
        df.to_csv(filepath, mode='a', index=False, header=False)

    print(f"Parsed data saved to CSV: {filepath}")
