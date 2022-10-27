from fpdf import FPDF
import sys

name = ' '.join(sys.argv[1:])
print(name)
pdf_file = FPDF()
pdf_file.add_page()
pdf_file.set_font('helvetica', '', 50)
pdf_file.cell(0, 50,'CS50 Shirtificate', align='C', new_x='LEFT', new_y='TOP')
pdf_file.image('shirtificate.png', 10, 80, w=pdf_file.epw)
pdf_file.set_font('helvetica', '', 30)
pdf_file.set_text_color(255,255,255)
pdf_file.cell(190, 250,  f'{name} took CS50', align='C')
pdf_file.output('shirtificate.pdf')
