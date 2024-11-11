#Felipe Gabriel Ribeiro, 329, GES

import numpy as np

ds = np.loadtxt('brands.csv', delimiter = ';', dtype = 'str', encoding = 'utf-8')

#Questão 1 = mostre quanto a empresa google valorizou de 2021 para 2022

print ('Questao 1:') #organize

google = ds[ds[:,0] == 'Google']
valGoogle2021 = google[:,10].astype('float')
valGoogle2022 = google[:,9].astype('float')

print (valGoogle2022 - valGoogle2021, '$M')

print()
print('----------------------------------------------------------------') #organize
print()

#Questão 2 = quantas marcas possuem a palavra 'Group' em seu nome

print ('Questao 2:') #organize

marcas = ds[:,0]
qtd = np.char.count(marcas, 'Group').sum()

print (qtd,'marcas')

print()
print('----------------------------------------------------------------') #organize
print()

#Questão 3 = nome e qual seria o valor de mercado das 5 primeiras empresas em 2023 caso tivessem um aumento de 10%

print ('Questao 3:') #organize

empresas = ds[1:6,:]
val2023 = empresas[:,9].astype('float') * 1.1

print (empresas[:,0], val2023)

print()
print('----------------------------------------------------------------') #organize
print()

#Questão 4 = slicing para extrair apenas as colunas: nome da marca, por quem foi fundado, ano que foi fundada. Em seguida mostre apenas o nome
# das empresas fundadas depois dos anos 2000

print ('Questao 4:') #organize

q4 = ds[1:, 0:3] #Colunas: nome da marca, por quem foi fundado, ano que foi fundada.
anos = q4[:,2].astype('int')

print ('empresas fundadas depois dos anos 2000:', q4[anos > 2000, 0])

print()
print('----------------------------------------------------------------') #organize
print()

#Questão 5 = busque os diferentes anos em que as empresas foram fundadas. Em seguida mostre o ano em que mais empresas abriram portas

print ('Questao 5:') #organize

anos = ds[1:,2] #diferentes anos em que as empresas foram fundadas

anosUnicos = np.unique(anos)
qtdEmpresas = np.zeros(len(anosUnicos))

for i in range(len(anosUnicos)):
    qtdEmpresas[i] = np.sum(anos == anosUnicos[i])
    
print (anosUnicos[np.argmax(qtdEmpresas)],'foi o ano em que mais empresas foram fundadas')

print()
print('----------------------------------------------------------------') #organize
print()