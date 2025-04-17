'''
You are choreographing a circus show involving two kangaroos that start on a number line and jump in the positive direction (toward positive infinity).
Kangaroo 1 starts at position x1 and jumps v1 meters per jump.
Kangaroo 2 starts at position x2 and jumps v2 meters per jump.
You need to determine whether both kangaroos will land on the same location at the same time (after the same number of jumps). If it is possible, return "YES"; otherwise, return "NO".

Function Description
def kangaroo(x1, v1, x2, v2):
    # your code here
    
Parameters
x1 (int): Starting position of the first kangaroo
v1 (int): Jump distance of the first kangaroo
x2 (int): Starting position of the second kangaroo
v2 (int): Jump distance of the second kangaroo

Returns
A string: either "YES" if the kangaroos land together, or "NO" otherwise

Input Format
A single line containing four space-separated integers: x1, v1, x2, and v2.

Sample Input 0
0 3 4 2
Sample Output 0
YES
Explanation 0
First kangaroo starts at 0 and jumps 3 meters: positions → 0, 3, 6, 9, 12...
Second kangaroo starts at 4 and jumps 2 meters: positions → 4, 6, 8, 10, 12...
They both land at position 12 after 4 jumps, so the answer is "YES".

Sample Input 1
0 2 5 3
Sample Output 1
NO
Explanation 1
The second kangaroo starts ahead of the first kangaroo and also jumps farther per turn.
The first kangaroo can never catch up, so they will never land together.
Hence, the answer is "NO".
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    if v1!= v2 and (x2 - x1) % (v1 - v2) == 0 and (v1 > v2):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()
