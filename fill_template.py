from docx import Document

# Load template
doc = Document("template.docx")


field_values = {
    "XM8_INSURED_NAME": "WADE-JAMES",
    "XM8_DATE_LOSS": "11/21/2024",
    "XM8_INSURED_P_STREET": "7061 Springfield Hills Dr. S.",
    "XM8_INSURED_P_CITY": "Indianapolis",
    "XM8_INSURED_P_STATE": "IN",
    "XM8_INSURED_P_ZIP": "46229",
    "XM8_CLAIM_NUM": "N/A",
    "XM8_FILE_NO": "N/A",
    "XM8_ESTIMATOR_NAME": "Steven Kujawski",
    "XM8_DATE_INSPECTED": "11/21/2024",
    "XM8_CLAIM_REP_NAME": "N/A",
    "XM8_SUM_ACV": "N/A",
    "XM8_LR_RC_LOSS": "N/A",
    "XM8_SUM_DEDUCTIBLE_APPLIED": "N/A"
}


for para in doc.paragraphs:
    for key, value in field_values.items():
        if f"[{key}]" in para.text:
            para.text = para.text.replace(f"[{key}]", value)

doc.save("output.docx")
print("[✅] Template filled and saved as output.docx")
