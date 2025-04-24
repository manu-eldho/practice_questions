'''
Two children, Lily and Ron, want to share a chocolate bar.
Each square on the chocolate bar has an integer.
Lily wants to share a contiguous segment of squares with Ron such that:
The length of the segment is equal to Ron’s birth month m.
The sum of the segment equals Ron’s birth day d.
Your task is to determine how many such segments exist in the chocolate bar.

Input Format
First line: Integer n – the number of squares in the chocolate bar.
Second line: n space-separated integers representing the chocolate squares.

Third line: Two integers – Ron’s birth day d and birth month m.

Function Signature
def birthday(s, d, m):
    # s: list of integers on chocolate squares
    # d: Ron's birth day
    # m: Ron's birth month
    # return: number of valid segments
Sample Inputs & Outputs
Sample Input 0:
5
1 2 1 3 2
3 2
Sample Output:
2
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def birthday(s, d, m):
    count = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i+m]) == d:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    first_multiple_input = input().rstrip().split()
    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    result = birthday(s, d, m)
    fptr.write(str(result) + '\n')
    fptr.close()
