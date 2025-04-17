'''
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Your task is to determine how many apples and oranges land on Sam's house.

Scenario
Sam's house is located between two points on the x-axis: s (start) and t (end), both inclusive.
The apple tree is located at point a.
The orange tree is located at point b.
When a fruit falls, it falls a certain distance d from its tree.
If d is negative, the fruit falls to the left of the tree.
If d is positive, it falls to the right.
You are given a list of distances each apple and orange falls from its tree. Your task is to determine how many of the apples and oranges fall on Sam's house.

Function Description
Complete the function countApplesAndOranges:
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # your code here
    
Parameters
s (int): starting point of Sam's house
t (int): ending point of Sam's house
a (int): location of the apple tree
b (int): location of the orange tree
apples (list of int): distances apples fall from tree a
oranges (list of int): distances oranges fall from tree b

Output
Print two integers on separate lines:
Number of apples that fall on Sam’s house.
Number of oranges that fall on Sam’s house.

Input Format
The first line contains two space-separated integers: s and t.
The second line contains two space-separated integers: a and b.
The third line contains two space-separated integers: m and n, the number of apples and oranges.
The fourth line contains m space-separated integers: distances at which each apple falls from tree a.
The fifth line contains n space-separated integers: distances at which each orange falls from tree b.

Sample Input
7 11
5 15
3 2
-2 2 1
5 -6
Sample Output
1
1

Explanation
Sam's house is from 7 to 11.
Apple tree is at 5. Apple distances are -2, 2, 1 → apples land at 3, 7, 6.
Only the apple that lands at 7 is on the house.
Orange tree is at 15. Orange distances are 5, -6 → oranges land at 20, 9.
Only the orange that lands at 9 is on the house.

So the final result is:
1
1
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = [x+a for x in apples]
    oranges = [x+b for x in oranges]
    app = len([x for x in apples if s<=x<=t])
    ora = len([x for x in oranges if s<=x<=t])
    print(app)
    print(ora)
  
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
