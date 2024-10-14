import os
import numpy as np

file = os.path.abspath(r'Y:\Inatel\P8\C111\paises.csv')

ds = np.loadtxt(file, delimiter=';',
                dtype='str', encoding='utf-8') #carregar dataset como texto(string)

region = ds[:,1]

qtd = np.char.count(region, 'NORTHERN AMERICA').sum()

print(qtd)