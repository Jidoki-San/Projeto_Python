import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

planilha = pd.read_excel("Dados-covid-19-municipios.xlsx")

municipios = planilha['Município']
casos = planilha['Total de casos']

plt.figure(figsize=(10,9))
plt.pie(casos, labels=municipios, autopct='%1.2f%%')
texto = "Casos de covid-19 \n Esse gráfico de pizza mostra as porcentagens de casos de cada município, se liga:"
plt.savefig("Casos de covid - 10 Municípios.png")

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Times', '', 14)
pdf.multi_cell(w=0, h=7, txt=texto, align="C")
# pdf.line(25, 30, 215, 30)
pdf.image(name="Casos de covid - 10 Municípios.png", x=0, y=40, w=200,)
pdf.output("Casos de covid - 10 Municípios.pdf")

print("O PDF foi criado/alterado com sucesso!")
os.system("pause") 