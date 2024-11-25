import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# grafico de linhas (plot)
'''
x = np.array([1, 2, 3, 4])
y = x * 2 #broadcasting
y2 = x ** 2
plt.plot(x, y, '*:g',
         x, y2, 'o-r', linewidth='5', markersize='20')
plt.show()

#subplots
x = np.array([1, 2, 3, 4])
y = x * 2 #broadcasting
plt.subplot(1, 2, 1) #linha 1, 2 colunas, esta na celula 1
plt.plot(x, y, '*:g', linewidth='5', markersize='20')

y2 = x ** 2
plt.subplot(1, 2, 2) #linha 1, 2 colunas, esta na celula 2
plt.plot(x, y2, 'o-r', linewidth='5', markersize='20')

plt.show()
'''

#scatter plot grafico de dispersao

file = os.path.abspath(r'Y:\Inatel\P8\C111\paises.csv')
dfPaises = pd.read_csv(file, delimiter=';')
print(dfPaises.columns)
dfPaises2 = dfPaises.nlargest(6, 'Area (sq. mi.)')
plt.scatter(dfPaises2['Country'], dfPaises2['Area (sq. mi.)'],
            s=dfPaises2['GDP ($ per capita)']/10)
plt.show()