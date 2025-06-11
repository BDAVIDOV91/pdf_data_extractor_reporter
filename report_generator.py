import os

def save_report(text: str, filename: str, output_dir="output_reports"):
    """
    Saves the report as a text file inside the given directory.
    Creates the directory if it does not exist.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    
    print(f"Report saved successfully: {filepath}")
