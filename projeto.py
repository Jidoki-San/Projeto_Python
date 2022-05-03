import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

planilha = pd.read_excel("Dados-covid-19-municipios.xlsx")


municipios = planilha['Município']
casos = planilha['Total de casos']

plt.title("Casos de Covid - 15 municípios")

plt.bar(municipios, casos, color='green', width=0.5)

plt.show()