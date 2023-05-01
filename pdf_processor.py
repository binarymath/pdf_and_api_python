from fpdf import FPDF
from PyPDF2 import PdfReader

reader = PdfReader("request.pdf")
page = reader.pages[0]
text = page.extract_text()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, text)
pdf.output("output.pdf")

