import os
import numpy as np

file = os.path.abspath(r'Y:\Inatel\P8\C111\paises.csv')

ds = np.loadtxt(file, delimiter=';',
                dtype='str', encoding='utf-8') #carregar dataset como texto(string)

qtd = len(np.unique(ds[1:, 1:2]))
regions = np.unique(ds[1:, 1:2])

print(qtd)
print(regions)