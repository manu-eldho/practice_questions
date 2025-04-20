'''
A teacher asks the class to open their books to a page number p. A student can start turning pages from the front or the back of the book.
The book always opens to page 1.
When flipping pages, a student sees two pages at a time: for example, flipping once from the front shows pages 2 and 3.
The student should find the minimum number of page turns needed to reach page p.
Write a function that returns this minimum number of page turns.

Function Signature
def pageCount(n: int, p: int) -> int:
Input
n: Total number of pages in the book (an even or odd number).
p: Target page to reach.
Output
Return the minimum number of pages that must be turned to reach page p.

Constraints
1 ≤ n ≤ 10^5
1 ≤ p ≤ n

Example 1
Input
n = 6
p = 2
Output
1
Explanation:
From the front: turn 1 page → reach page 2.
From the back: turn 2 pages → reach page 2.
Minimum = 1.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def pageCount(n, p):
    front = p // 2
    back = (n // 2) - (p // 2)
    return min(front, back)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    p = int(input().strip())
    result = pageCount(n, p)
    fptr.write(str(result) + '\n')
    fptr.close()
