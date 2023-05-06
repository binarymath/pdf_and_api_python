from dotenv import load_dotenv
import os
from fpdf import FPDF
import PyPDF2
import requests

load_dotenv()
API_Key = os.getenv('API-Key')
API_Host = os.getenv('API-Host')

# division_of_line = input("Type the keyword to start the question: ")

url = "https://openai80.p.rapidapi.com/chat/completions"

with open('pdf/planodeaula.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)

    text = []
    for page in range(len(pdf_reader.pages)):
        text_list = pdf_reader.pages[page].extract_text().split('\n')
        new_text_list = []
        for i, line in enumerate(text_list):
            # if division_of_line in line:
            #     new_text_list.append('\n' + line + '\n')
            # else:
            new_text_list.append(line)
        text.extend(new_text_list)
    text = ' '.join(text)

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": text
        }
    ]
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": API_Key,
    "X-RapidAPI-Host": API_Host
}
response = requests.post(url, json=payload, headers=headers, timeout=1000)
data = response.json()

text = data['choices'][0]['message']['content']

print("Arquivo gerado com sucesso")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
max_width = 180
lines = pdf.multi_cell(max_width, 5, text)
for line in lines:
    pdf.cell(0, 5, line)
pdf.output("pdf/plano_de_aula_feito.pdf")
