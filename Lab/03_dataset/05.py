import os
import numpy as np

file = os.path.abspath(r'Y:\Inatel\P8\C111\space.csv')

ds = np.loadtxt(file, delimiter=';',
                dtype='str', encoding='utf-8') #carregar dataset como texto(string)

companyName = ds[1:, 1] #nome das empresas

unique, count = np.unique(companyName, return_counts=True) #quantidade de missoes por empresa

#empresas e quantidade de missoes
for i in range(len(unique)):
    company = unique[i]
    quantity = count[i]
    print(company, '|', quantity)