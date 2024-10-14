import os
import numpy as np

file = os.path.abspath(r'Y:\Inatel\P8\C111\space.csv')

ds = np.loadtxt(file, delimiter=';',
                dtype='str', encoding='utf-8') #carregar dataset como texto(string)

#ds = np.loadtxt('space.csv', delimiter=';',
#                dtype='str', encoding='utf-8') #carregar dataset como texto(string)

#print(ds) #mostrar o dataset
#print('colunas:', ds[0, :]) #mostrar todas as colunas da linha 0 (nome das colunas)

#quais as diferentes empresas que ja fizeream missoes espaciais segundo esse dataset?
#extrair a coluna company name
#cn = np.unique(ds[1:,1]) #(linha:coluna) todas as linhas da coluna 1, exceto o nome da coluna (linha 0) e os nomes repetidos
cn = len(np.unique(ds[1:,1])) #quantidade de linhas da coluna 1, exceto o nome da coluna (linha 0) e os nomes repetidos
print(cn)