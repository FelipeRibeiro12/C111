import os
import numpy as np

file = os.path.abspath(r'Y:\Inatel\P8\C111\paises.csv')

ds = np.loadtxt(file, delimiter=';',
                dtype='str', encoding='utf-8') #carregar dataset como texto(string)

LeC = ds[ds[:,1] == 'LATIN AMER. & CARIB    ']

gdp_per_capita = LeC[:, 8].astype(float)

max_index = np.argmax(gdp_per_capita)

highestGDP = LeC[max_index]

print(highestGDP[0])