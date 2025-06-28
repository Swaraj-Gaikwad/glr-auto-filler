from extract_pdf_text import extract_text_from_pdf

pdf_path = "report.pdf"
text = extract_text_from_pdf(pdf_path)

print(text[:1000])  
