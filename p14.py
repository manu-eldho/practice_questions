'''
You are given an array of integers. Find the length of the longest subarray where the absolute difference between any two elements is less than or equal to 1.

Function Signature:
def pickingNumbers(a: List[int]) -> int:
Parameters:
a (List[int]): An array of integers.
Returns:
int: Length of the longest subarray that satisfies the condition.
Input Format:
The first line contains a single integer n, the size of the array a.
The second line contains n space-separated integers.
Constraints:
2 <= n <= 100
0 < a[i] < 100

Sample Input 0:
6
4 6 5 3 3 1
Sample Output 0:
3
Explanation 0:
We choose the subarray [4, 3, 3]. All pairs have absolute differences less than or equal to 1.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    from collections import Counter
    count = Counter(a)
    max_length = 0
    
    for num in count:
        curr = count[num] + count.get(num + 1, 0)
        max_length = max(max_length, curr)
    
    return max_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    fptr.write(str(result) + '\n')
    fptr.close()
