import requests
import os
from dotenv import load_dotenv
from extract_pdf_text import extract_text_from_pdf


load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")


pdf_text = extract_text_from_pdf("report.pdf")[:2000] 


prompt = f"""
You are an insurance claim assistant. Your job is to extract structured key-value data from claim photo reports.

Return only JSON output with the following fields (no explanation):

- XM8_DATE_LOSS
- XM8_INSURED_NAME
- XM8_INSURED_P_STREET
- XM8_INSURED_P_CITY
- XM8_INSURED_P_STATE
- XM8_INSURED_P_ZIP
- XM8_CLAIM_NUM
- XM8_FILE_NO
- XM8_ESTIMATOR_NAME
- XM8_DATE_INSPECTED
- XM8_CLAIM_REP_NAME
- XM8_SUM_ACV
- XM8_LR_RC_LOSS
- XM8_SUM_DEDUCTIBLE_APPLIED

Report text:
{pdf_text}
"""


# API Call
url = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

res = requests.post(url, headers=headers, json={"inputs": prompt})

print("\n[ℹ️] Status:", res.status_code)
print("[✅] Output:\n", res.text)

