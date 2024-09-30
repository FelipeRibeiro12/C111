import os
import numpy as np

file = os.path.abspath(r'Y:\Inatel\P8\C111\space.csv')

ds = np.loadtxt(file, delimiter=';',
                dtype='str', encoding='utf-8') #carregar dataset como texto(string)

missionsEUA = np.sum(np.char.find(ds[1:, 2], 'USA') != -1) #quantidade de missoes realizadas pelos EUA na coluna

print(missionsEUA)