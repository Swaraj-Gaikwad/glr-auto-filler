GLR Auto-Filler (Insurance Claim Report)

This project extracts structured data from a photo inspection report (`.pdf`) and fills an `.docx` template automatically.

### 🧰 Tools Used
- Python (`python-docx`, `PyMuPDF`)
- Optional: HuggingFace LLMs
- Input: `report.pdf` + `template.docx`
- Output: `output.docx`

### 🚀 How to Run
```bash
python extract_pdf_text.py         # Optional: See extracted text
python task_3_code.py              # Fills the template
