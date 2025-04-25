'''
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps, for every step it was noted if it was an uphill step (U), or a downhill step (D). Hikes always start and end at sea level, and each step up or down represents a 1 unit change in altitude.
We define the following terms:
A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Task
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
Function Signature
def countingValleys(steps: int, path: str) -> int:
Input Format
The first line contains an integer steps, the number of steps in the hike.
The second line contains a single string path, of steps characters that describe the path.
Constraints
2 <= steps <= 10^6
path[i] is either U (uphill) or D (downhill)
Output Format
Print the number of valleys traversed.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    altitude = 0
    valleys = 0

    for step in path:
        if step == 'U':
            altitude += 1
        else: 
            altitude -= 1
        if altitude == 0 and step == 'U':
            valleys += 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    fptr.write(str(result) + '\n')
    fptr.close()
