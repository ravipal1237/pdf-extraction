import pdfplumber
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def process_pdf(pdf_path):
    text = ""

    # Step 1: Try pdfplumber (digital PDFs)
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        pass

    # Step 2: Fallback to OCR only if no text found
    if not text.strip():
        import pdf2image
        pages = pdf2image.convert_from_path(pdf_path)
        for page in pages:
            result = ocr.ocr(page, cls=True)
            for line in result[0]:
                text += line[1][0] + "\n"

    return text
