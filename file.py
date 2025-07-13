import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import argparse
import os

def extract_text_from_page(page):
    """Extract text directly from a PDF page using PyMuPDF."""
    return page.get_text()

def ocr_page_image(image):
    """Run OCR on an image using pytesseract."""
    return pytesseract.image_to_string(image)

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    all_text = ""

    print(f"\nTotal pages: {len(doc)}")

    for i, page in enumerate(doc):
        print(f"\nPage {i+1}:")

        text = extract_text_from_page(page)

        if text.strip():
            print("Text found, extracting directly.")
        else:
            print("No text found, using OCR...")
            images = convert_from_path(pdf_path, first_page=i+1, last_page=i+1)
            text = ocr_page_image(images[0])

        all_text += f"\n--- Page {i+1} ---\n{text}"

    return all_text

def save_output(text, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"\nExtracted text saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Extract text from PDF (with OCR fallback).")
    parser.add_argument("--input", "-i", required=True, help="Path to the PDF file.")
    parser.add_argument("--output", "-o", default="output.txt", help="Output text file (default: output.txt)")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print("Error: PDF file not found.")
        return

    print("Starting text extraction...")
    text = extract_text(args.input)
    save_output(text, args.output)

if __name__ == "__main__":
    main()
