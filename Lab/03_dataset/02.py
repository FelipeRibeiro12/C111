import os
import numpy as np

file = os.path.abspath(r'Y:\Inatel\P8\C111\space.csv')

ds = np.loadtxt(file, delimiter=';',
                dtype='str', encoding='utf-8') #carregar dataset como texto(string)

cost = ds[1:, 6].astype(float) #transformar custo da missao em float(numero)

validCost = cost[cost > 0] #custos validos

avarageCost = np.mean(validCost) #media dos custos validos

print(avarageCost)