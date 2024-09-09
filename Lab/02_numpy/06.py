import numpy as np

np.random.seed(5)

arr = np.random.randint(-1, 1, 10)
arr2 = arr * 100
arr3 = arr2.astype(int)

print(arr3)