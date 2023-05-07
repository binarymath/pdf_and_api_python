"""
PDF processor, reads the pdf
Makes the request to the api and returns another pdf with the response.
"""

import os
from dotenv import load_dotenv
from fpdf import FPDF
import requests
import PyPDF2


load_dotenv()
API_Key = os.getenv('API-Key')
API_Host = os.getenv('API-Host')

URL = "https://openai80.p.rapidapi.com/chat/completions"

with open('pdf/plano_de_aula.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)

    TEXT = []
    for page, _ in enumerate(pdf_reader.pages):
        text_list = pdf_reader.pages[page].extract_text().split('\n')
        new_text_list = []
        for i, line in enumerate(text_list):
            new_text_list.append(line)
        TEXT.extend(new_text_list)
    TEXT = ' '.join(TEXT)

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": TEXT
        }
    ]
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": API_Key,
    "X-RapidAPI-Host": API_Host
}
response = requests.post(URL, json=payload, headers=headers, timeout=1000)
data = response.json()

TEXT = data['choices'][0]['message']['content']

print("File generated successfully")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
MAX_WIDTH = 180
lines = pdf.multi_cell(MAX_WIDTH, 5, TEXT)
for line in lines:
    pdf.cell(0, 5, line)
pdf.output("pdf/plano_de_aula_feito.pdf")
