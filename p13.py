'''
You are given a pile of socks represented as an array of integers, where each integer denotes the color of a sock. Your task is to count how many matching pairs of socks there are.

Function Description
def sockMerchant(n, ar):
Parameters:
int n: Number of socks
list ar: List of integers representing sock colors
Returns:
int: Number of matching pairs

Input Format
The first line contains an integer n, the total number of socks.
The second line contains n space-separated integers, representing the colors of the socks.

Constraints
1 ≤ n ≤ 100
1 ≤ ar[i] ≤ 100 (where ar[i] is the sock color)

Sample Input
9
10 20 20 10 10 30 50 10 20
Sample Output
3
Explanation
Socks by color:
10 → 4 socks → 2 pairs
20 → 3 socks → 1 pair
30 → 1 sock → 0 pairs
50 → 1 sock → 0 pairs
So, total pairs = 2 (for 10) + 1 (for 20) = 3 pairs
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    color_count = {}
    for sock in ar:
        color_count[sock] = color_count.get(sock, 0) + 1
    pairs = 0
    for count in color_count.values():
        pairs += count // 2
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
