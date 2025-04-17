'''
Maria plays college basketball and wants to go pro. Each season she keeps track of her performance by recording the number of points she scores in each game. She also tracks the number of times she breaks her season records for the most and least points scored in a game.
Her first game's score sets the initial records for both highest and lowest points.
From the second game onward, each time her score is:
Higher than her highest so far, she breaks the record for most points.
Lower than her lowest so far, she breaks the record for least points.

Example
If her scores over 4 games are:
12 24 10 24
Then the breakdown looks like:


Game	Score	Min So Far	Max So Far	Min Breaks	Max Breaks
0	12	12	12	0	0
1	24	12	24	0	1 
2	10	10	24	1 1
3	24	10	24	1	1
She broke the maximum record once and the minimum record once, so the output is:
1 1
Function Description
Parameters
scores: a list of integers representing the points Maria scored in each game.

Returns
A list of two integers:
The number of times she broke her most points record.
The number of times she broke her least points record.

Input Format
The first line contains a single integer n, the number of games played.
The second line contains n space-separated integers: the scores of each game.

Constraints
1 ≤ n ≤ 1000
0 ≤ scores[i] ≤ 10⁸
Sample Input 0
9
10 5 20 20 4 5 2 25 1
Sample Output 0
2 4
Explanation
Maria breaks her most points record 2 times: at scores 20 and 25.
She breaks her least points record 4 times: at scores 5, 4, 2, and 1.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    highest = scores[0]
    lowest = scores[0]
    count_h = 0
    count_l = 0
    for score in scores:
        if score > highest:
            count_h +=1
            highest = score
        if score < lowest:
            count_l +=1
            lowest = score
    return count_h,count_l
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
