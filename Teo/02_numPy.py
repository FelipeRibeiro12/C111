#NUMPY
import numpy as np

#Numpy Array = ndarray -> estrutura de dados do numpy

#arr = np.array([1, 2, 3])
#print (type(arr))
#print (arr)


#Array 2d
#mtz = np.array([
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]])
#print(type(mtz))
#print(mtz)


#Propriedades do numpy array

#print(mtz.size) #numero de elementos
#print(mtz.ndim) #numero de dimensoes
#print(mtz.shape) #numero de linhas e colunas


#Arange -> cria um array com valores de inicio, fim e escala

#mtz = np.arange(1, 10, 1) #inicio/ parada(10 nao entra)/ escala(2 em 2, ...)
#print(mtz)


#Reshape -> transforma o array para matriz (unidiemnsional para multidimensional)

#mtz = mtz.reshape(3, 3) #3 linhas e 3 colunas = 9 elementos
#print(mtz)


#Concatenate -> unir arrays

#arr = np.arange(1, 10, 1)
#arr2 = np.arange(10, 19, 1)
#print(arr)
#print(arr2)
#print(arr+arr2) #soma, subtrai, multiplica e divide os elementos de mesmo indice (coluna por coluna) !mesmo tamanho para ser possivel a operacao

#arr3 = np.concatenate([arr, arr2]) #unir os arrays (COLCHETES)
#print(arr3)


#Random -> gerar numeros aleatorios

#np.random.seed(5) #semente de dados (seed)-> gerar numeros aleatorios iguais
#arr = np.random.randint(1, 10, 8) #inicio/ fim/ quantidade de elementos
#print(arr)


#Unique -> valores unicos (sem repeticoes) e ordena em ordem crescente

#print(np.unique(arr))


#Operacoes com Matrizes

#np.random.seed(10)
#mtz = np.random.randint(1, 20, 9).reshape(3, 3)
#print(mtz)
#print('Soma da primeira linha', mtz.sum(axis=1)[0]) #soma das linhas com slicing
#print('Soma da primeira coluna', mtz.sum(axis=0)[0]) #soma das colunas com slicing

#Broadcasting -> operacoes com arrays de tamanhos diferentes

#print(mtz * 0.9) #desconta 10% de todos os elementos da matriz


#-----------------------------------------------------------------------------------------------------------------------------------
#Slicing de dados

np.random.seed(5)
arr = np.random.randint(1, 10, 10)
#arr2 = arr[0:4] #slicing -> pega os elementos de 0 a 4 (4 nao entra)
#arr2[0] = 9 #altera o valor do elemento 0 -> arr tambem altera, pois ele nao cria uma copia, mas sim uma referencia
#print(arr)
#print(arr2)


#Slicing com copia de dados

#arr3 = arr[0:4].copy() #cria uma copia do array
#arr3[1] = 10 #altera o valor do elemento 1 -> arr nao altera
#print(arr3)


#Condicionais

#cond = arr < 6 #retorna um array de booleanos (true/false) -> mascara de valores booleanos (menores que 6)
#cond = arr%2==1 #retorna um array de booleanos (true/false) -> mascara de valores booleanos (impares)
#print (cond)
#print(arr[cond]) #mostrando os elementos que atendem a mascara de valores


#Subpacote Char (manipulacao de strings(textos))

#arr = np.array(['Pedro', 'Ana', 'Tiago',
#                'Davi', 'Anelise'])
#cond = np.char.find(arr, 'o') >= 0 #procura a letra 'o' em cada elemento do array -> -1 false / 1... posicao da letra na palavra (apenas a 1°): 0,1,2... 
#print(arr[cond])