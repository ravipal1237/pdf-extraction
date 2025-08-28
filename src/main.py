import os
import logging
from utils.logger import setup_logger
from ocr.ocr_processor import process_pdf
from llm.llm_extractor import extract_invoice_data
from rag.rag_manager import RAGManager
from export.exporter import save_to_excel

def main():
    setup_logger()
    logging.info("Starting invoice processing pipeline...")

    input_dir = "./input"
    output_dir = "./output"
    os.makedirs(output_dir, exist_ok=True)

    rag = RAGManager()

    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            logging.info(f"Processing {file}...")
            pdf_path = os.path.join(input_dir, file)

            # Step 1: OCR / Text extraction
            text = process_pdf(pdf_path)

            # Step 2: RAG context fetch
            context = rag.retrieve(text)

            # Step 3: LLM extraction
            invoice_data = extract_invoice_data(text, context)

            # Step 4: Save result
            save_to_excel(invoice_data, output_dir, file)

            # Step 5: Add to RAG for future
            rag.add(text, metadata={"file": file})

            logging.info(f"Completed processing {file}")

if __name__ == "__main__":
    main()
