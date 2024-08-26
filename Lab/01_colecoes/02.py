loja1 = {'S24', 'Iphone 14', 'Iphone 15'}
loja2 = {'S23', 'S24'}

#a
print(len(loja1), "modelos de celular na loja 1")
print(len(loja2), "modelos de celular na loja 2")

#b
modelosComuns = loja1.intersection(loja2)
print(len(modelosComuns), "modelo(s) de celular em comum")
print(modelosComuns) #retorna o valor