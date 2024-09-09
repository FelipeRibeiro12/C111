import numpy as np

arr1 = np.arange(0, 52, 2) #apenas numeros pares
arr2 = np.arange(100, 49, -2) #apenas numeros pares (-) para decrescente

arr3 = np.concatenate((arr1, arr2))

arr4 = np.sort(arr3)

print(arr4)
