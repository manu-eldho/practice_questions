'''Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero . Print the decimal value of each fraction on a new line with 6 places after the decimal.'''
#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    l = len(arr)
    pos= 0
    neg = 0
    zero = 0
    for i in arr:
        if i < 0: 
            neg +=1
        elif i > 0:
            pos +=1
        else:
            zero +=1
    print(pos/l,"\n",neg/l,"\n",zero/l)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
