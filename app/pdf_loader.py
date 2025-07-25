import pytesseract
from pdf2image import convert_from_path
import os

# Set the path to tesseract.exe (update if installed in a different location)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(pdf_path):
    print("📸 Running OCR on each page...")
    pages = convert_from_path(pdf_path, dpi=300)
    full_text = ""

    for i, page in enumerate(pages):
        image_path = f"temp_page_{i}.jpg"
        page.save(image_path, "JPEG")
        try:
            text = pytesseract.image_to_string(image_path, lang="ben")
            full_text += text + "\n"
        except Exception as e:
            print(f"❌ OCR failed on page {i}: {e}")
        finally:
            os.remove(image_path)

    return full_text
