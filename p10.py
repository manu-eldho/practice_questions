'''
Marie has invented a Time Machine and wants to visit Russia on the Day of the Programmer — the 256th day of the year. However, due to calendar transitions in Russian history, the exact date of this day varies depending on the year.
Russia used the Julian calendar from 1700 to 1917, then switched to the Gregorian calendar from 1919 onwards. In the year 1918, due to the calendar shift, February 14th was the 32nd day of the year (i.e., Russia skipped from Jan 31 straight to Feb 14).
Leap Year Rules:
Julian calendar: A leap year is divisible by 4.
Gregorian calendar: A leap year is:
Divisible by 400, or
Divisible by 4 and not divisible by 100.
You are given a year y in the range 1700 ≤ y ≤ 2700. Write a function to determine the exact date of the Day of the Programmer (the 256th day) for that year, and return it in the format:
dd.mm.yyyy
Function Signature
def dayOfProgrammer(year: int) -> str:
Input
A single integer year (1700 ≤ year ≤ 2700)

Output
A string representing the date of the 256th day of that year in format dd.mm.yyyy.

Examples
Input 1:
2017
Output 1:
13.09.2017
Input 2:
2016
Output 2:
12.09.2016
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def dayOfProgrammer(year):
    if year == 1918:
        return f"26.09.{year}"
    elif (1700 <= year <= 1917 and year % 4 == 0) or \
         (year >= 1919 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
        return f"12.09.{year}"
    else:
        return f"13.09.{year}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    year = int(input().strip())
    result = dayOfProgrammer(year)
    fptr.write(result + '\n')
    fptr.close()
