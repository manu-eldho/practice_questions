'''
You are given an array of integers where each integer represents a type of bird sighting. Each type is identified by an integer ID ranging from 1 to 5.
Your task is to determine which type of bird is seen most frequently.
If more than one type has the same maximum frequency, return the smallest type ID among them.

Function Description
def migratoryBirds(arr: list[int]) -> int:

Input Format
The first line contains an integer n, the number of bird sightings.
The second line contains n space-separated integers — the bird type IDs.

Output Format
Return a single integer denoting the type ID of the most frequently sighted bird. If there is a tie, choose the smallest ID.

Constraints
5 ≤ n ≤ 2 × 10⁵
It is guaranteed that each type ID is an integer in the range [1, 5].

Input
6
1 4 4 4 5 3
Output
4
Explanation
Bird types and frequencies:
Type 1 → 1 time
Type 3 → 1 time
Type 4 → 3 times
Type 5 → 1 time
Type 4 appears the most.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    freq = [0] * 6  
    for bird in arr:
        freq[bird] += 1
    max_count = max(freq)
    for i in range(1, 6):
        if freq[i] == max_count:
            return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
