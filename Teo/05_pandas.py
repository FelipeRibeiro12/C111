import os
import pandas as pd
import numpy as np


#SERIES(1D)(espera um dicionario->chave valor)
dic = {'a':10,'b':20,'c':30}

s1 = pd.Series(dic)
s2 = pd.Series(data=[20,30,40],index=['a','b','d'])
#print(s1+s2)
#print(s1.add(s2,fill_value=0))#fill value, todos que são vazio(Nan) se tornará zero, add é veferente a soma
#print(s1['b'])#acessa um unico valor
#print(s1[['b','c']])#acessa o valor de b e o valor de c
#print(s1[s1>s1.mean()])#pega os valores maiores que a media dos elementos

#DATAFRAMES(2D)
df = pd.DataFrame(
    index=['A','B','C','D'],
    columns=['X','Y','Z'],
    data=np.random.randint(1,50,[4,3])
)
#print(df)
#slicing com loc
#print(df.loc[['B','C'],['X','Y','Z']])#linhas b e c e colunas xyz

#sling com iloc
#print(df.iloc[1:3,:])#linhas de 1 a 2 e todas colunas

#lendo um csv com pandas
#df=pd.read_csv('paises.csv',delimiter=';')
file = os.path.abspath(r'Y:\Inatel\P8\C111\paises.csv')
df = pd.read_csv(file, delimiter=';')
print(df)
print('********')
print(df.columns)
print('********')
print(df['Country'])#valores da coluna country
print('********')
print(df.head(5))#os 5 primeiros registros
print('********')
print((df.tail(2)))#os dois ultimos