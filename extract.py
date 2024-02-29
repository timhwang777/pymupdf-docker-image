import sys
import os
import fitz # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def write_text_to_file(text, file_path):
    with open(file_path, "w") as file:
        file.write(text)

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    output_path = sys.argv[2]
    # Add file path to the pdf file and the output file
    pdf_full_path = os.path.join('./data', pdf_path)
    output_full_path = os.path.join('./data', output_path)
    
    text = extract_text_from_pdf(pdf_full_path)
    write_text_to_file(text, output_full_path)