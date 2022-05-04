import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

planilha = pd.read_excel("Dados-covid-19-municipios.xlsx")
municipios = planilha['Município']
obitos = planilha['Total de óbitos']

plt.figure(figsize=(15,14))
plt.barh(municipios, obitos , color='red', height=0.5)
plt.savefig("Óbitos por covid-19 - 10 Municípios.png")

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Times', 'i', 16)
pdf.cell(w=0, h=0, txt="Óbitos por covid-19 - 10 Municípios", align='C')
pdf.line(10, 15, 200,15)

pdf.image(name="Óbitos por covid-19 - 10 Municípios.png", x=0, y=25, w=220)
pdf.output("Óbitos por covid-19 - 10 Municípios.pdf")

print("PDF criado/alterado com sucesso!")
os.system("pause")