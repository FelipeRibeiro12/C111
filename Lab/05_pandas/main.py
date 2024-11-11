import os
import pandas as pd

file = os.path.abspath(r'Y:\Inatel\P8\C111\paises.csv')
df = pd.read_csv(file, delimiter=';')

print('1 A')
pOceania = df['Country'][df['Region'].str.contains('OCEANIA')]
print(pOceania)

print()
print('----------------------------------------------------------------')

print('B')
qtdOceania = (df['Region'].str.contains('OCEANIA')).sum()

print(qtdOceania)

print()
print('----------------------------------------------------------------')

print('2')
mAlfabt = df['Literacy (%)'].mean()

print(mAlfabt, "%")

print()
print('----------------------------------------------------------------')

print('3')
maxIndex = df['Population'].idxmax()
mPop = df.loc[maxIndex, ['Country', 'Region']]

print(mPop)

print()
print('----------------------------------------------------------------')

print('4')
noCoastCountries = df['Country'][df['Coastline (coast/area ratio)'] == 0]
noCoastCountries.to_csv('noCoast.csv', index=False)

print(noCoastCountries)