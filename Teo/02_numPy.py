#NUMPY
import numpy as np

#numpy array = ndarray -> estrutura de dados do numpy
#arr = np.array([1, 2, 3])
#print (type(arr))
#print (arr)

#array 2d
#mtz = np.array([
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]])
#print(type(mtz))
#print(mtz)

#propriedades do numpy array
#print(mtz.size) #numero de elementos
#print(mtz.ndim) #numero de dimensoes
#print(mtz.shape) #numero de linhas e colunas


#arange -> cria um array com valores de inicio, fim e escala
#mtz = np.arange(1, 10, 1) #inicio/ parada(10 nao entra)/ escala(2 em 2, ...)
#print(mtz)

#reshape -> transforma o array para matriz (unidiemnsional para multidimensional)
#mtz = mtz.reshape(3, 3) #3 linhas e 3 colunas = 9 elementos
#print(mtz)

#concatenate -> unir arrays
#arr = np.arange(1, 10, 1)
#arr2 = np.arange(10, 19, 1)
#print(arr)
#print(arr2)
#print(arr+arr2) #soma, subtrai, multiplica e divide os elementos de mesmo indice (coluna por coluna) !mesmo tamanho para ser possivel a operacao

#arr3 = np.concatenate([arr, arr2]) #print(np.concatenate([arr, arr2])) #unir os arrays (COLCHETES)

#random -> gerar numeros aleatorios
#np.random.seed(5) #semente de dados (seed)-> gerar numeros aleatorios iguais
#arr = np.random.randint(1, 10, 8) #inicio/ fim/ quantidade de elementos
#print(arr)

#unique -> valores unicos (sem repeticoes) e ordena em ordem crescente
#print(np.unique(arr))

#operacoes com matrizes
#np.random.seed(10)
#mtz = np.random.randint(1, 20, 9).reshape(3, 3)
#print(mtz)
#print('Soma da primeira linha', mtz.sum(axis=1)[0]) #soma das linhas com slicing
#print('Soma da primeira coluna', mtz.sum(axis=0)[0]) #soma das colunas com slicing

#broadcasting -> operacoes com arrays de tamanhos diferentes
#print(mtz * 0.9) #desconta 10% de todos os elementos da matriz