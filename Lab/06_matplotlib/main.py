import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1

file = os.path.abspath(r'Y:\Inatel\P8\C111\space.csv')
dfSpace = pd.read_csv(file, delimiter=';')
empresas_eua = dfSpace[dfSpace['Location'].str.contains('USA')]
empresas_china = dfSpace[dfSpace['Location'].str.contains('China')]
num_empresas_eua = len(empresas_eua)
num_empresas_china = len(empresas_china)
num_empresas = [num_empresas_eua, num_empresas_china]
plt.bar(['EUA', 'China'], num_empresas, color=['blue', 'red'])
plt.title('Número de Empresas Espaciais nos EUA e na China')
plt.show()

# 2

file = os.path.abspath(r'Y:\Inatel\P8\C111\paises.csv')
df = pd.read_csv(file, delimiter=';')
northern_america = df[df['Region'] == 'NORTHERN AMERICA                   ']
plt.figure(figsize=(12, 6))
plt.plot(northern_america['Country'], northern_america['Deathrate'], label='Taxa de Mortalidade')
plt.plot(northern_america['Country'], northern_america['Birthrate'], label='Taxa de Natalidade')
plt.title('Taxa de Mortalidade e Natalidade nos Países da América do Norte')
plt.xlabel('Países')
plt.ylabel('Taxas')
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.show()