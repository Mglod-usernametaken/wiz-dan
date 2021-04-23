import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt



plikplik = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(plikplik, header=0)

# zad 1

sumaroczna = df.groupby(['Rok']).agg({'Liczba': ['sum']})
print(sumaroczna)
plt.plot(sumaroczna)
plt.ylabel('suma urodzen')
# plt.show()

# zad 2

sumaplci = df.groupby(['Plec']).agg({'Liczba': ['suma']})
plt.plot(sumaplci)
plt.ylabel('urodzenia')
# plt.show()

# zad 3

sumapieclat = df[df['Rok'] > 2012].groupby(['Plec']).agg({'Liczba': ['suma']})
sumapieclat.plt.pie(subplots=True, autopct='%.2f %%')
# plt.show()

