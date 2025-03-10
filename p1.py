N,M = list(map(int,input().split()))
import numpy as np

matrix = np.array([input().split() for _ in range(N)], dtype = int)

print(matrix.T)
print(matrix.ravel())
