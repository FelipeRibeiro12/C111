import os
import numpy as np

file = os.path.abspath(r'Y:\Inatel\P8\C111\paises.csv')

ds = np.loadtxt(file, delimiter=';',
                dtype='str', encoding='utf-8') #carregar dataset como texto(string)

qtd = len(ds[:, 9:10])
soma = np.sum(ds[1:, 9:10].astype('float'))
media = soma / qtd

m = np.mean(ds[1:, 9:10].astype('float'))

print(m)
print(media)