import os
import numpy as np

file = os.path.abspath(r'Y:\Inatel\P8\C111\paises.csv')

ds = np.loadtxt(file, delimiter=';',
                dtype='str', encoding='utf-8') #carregar dataset como texto(string)

print(ds[1:, 0:4]) #linha / coluna -> [a:b, x:z] a e b: inclusive e exclusive de linhas