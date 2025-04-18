'''
You are given an array of integers and a positive integer k. Your task is to determine the number of (i, j) pairs in the array where:
i < j
(arr[i] + arr[j]) is divisible by k

Function Description
def divisibleSumPairs(n: int, k: int, arr: list[int]) -> int:
Input Format
The first line contains two space-separated integers, n (size of the array) and k (the divisor).
The second line contains n space-separated integers that make up the array arr.

Output Format
Return a single integer: the number of valid pairs.

Constraints
2 ≤ n ≤ 100
1 ≤ k ≤ 100
1 ≤ arr[i] ≤ 100

Example
Input
6 3
1 3 2 6 1 2
Output
5
Explanation
The following 5 pairs are divisible by 3:
(0, 2): 1 + 2 = 3
(0, 5): 1 + 2 = 3
(1, 3): 3 + 6 = 9
(2, 4): 2 + 1 = 3
(4, 5): 1 + 2 = 3
All of these are divisible by k = 3.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
