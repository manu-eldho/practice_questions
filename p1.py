"""You are given a X integer array matrix with space separated elements ( N = rows and M = columns).
Your task is to print the transpose and flatten results.

Input Format

The first line contains the space separated values of  N and M.
The next  lines contains the space separated elements of  columns.

Output Format

First, print the transpose array and then print the flatten.N,M = list(map(int,input().split()))"""

import numpy as np

matrix = np.array([input().split() for _ in range(N)], dtype = int)

print(matrix.T)
print(matrix.ravel())
