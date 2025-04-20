'''
Anna and Brian are sharing the cost of a meal. Each of them only pays for the items they actually consume. After the meal, Brian calculates how much Anna owes and collects money from her.
Given the list of item prices, the index of the item Anna didn’t eat, and the amount Brian charged her, determine whether Brian calculated correctly. If he did, print "Bon Appetit". Otherwise, print the amount Brian owes Anna as a refund.

Function Signature
def bonAppetit(bill: List[int], k: int, b: int) -> None:

Input
bill: A list of integers where bill[i] is the cost of the i-th item.
k: An integer representing the zero-based index of the item Anna did not eat.
b: An integer, the amount of money Brian charged Anna.

Output
Print "Bon Appetit" if Brian's charge is correct.
Otherwise, print the overcharged amount (an integer).

Constraints
2 ≤ len(bill) ≤ 10^5
0 ≤ bill[i] ≤ 10^4
0 ≤ k < len(bill)
0 ≤ b ≤ sum(bill)

Example 1
Input
bill = [3, 10, 2, 9]
k = 1
b = 12
Output
5
Explanation:
Anna didn’t eat item at index 1 (cost = 10). The total of the remaining items = 3 + 2 + 9 = 14, split between two people = 7.
Brian charged Anna 12, so he owes her 12 - 7 = 5.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    actual_share = (sum(bill) - bill[k]) // 2
    if b == actual_share:
        print("Bon Appetit")
    else:
        print(b - actual_share)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)
