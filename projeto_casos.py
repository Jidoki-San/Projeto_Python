import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

planilha = pd.read_excel("Dados-covid-19-municipios.xlsx")

municipios = planilha['Município']
casos = planilha['Total de casos']

plt.pie(casos, labels=municipios, autopct='%1.2f%%')

plt.savefig("Casos de covid - 10 Municípios.png")

pdf = FPDF('P', 'mm', 'A3')
pdf.add_page()
pdf.set_font('Times', 'i', 16)
pdf.cell(w=0, h=0, txt="Casos de covid-19 - 10 Municípios", align="C")
pdf.image(name="Casos de covid - 10 Municípios.png", x=0, y=20, w=200)
pdf.output("Casos de covid - 10 Municípios.pdf")

print("O PDF foi criado/alterado com sucesso!")
os.system("pause") 