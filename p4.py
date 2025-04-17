'''
HackerLand University has the following grading policy:
Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 38 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:
If the difference between the grade and the next multiple of 5 is less than 3, round the grade up to the next multiple of 5.
If the grade is less than 38, no rounding occurs as the result will still be a failing grade.

Examples
grade = 84 → next multiple of 5 is 85 → difference is 1 → round to 85
grade = 29 → less than 38 → no rounding
grade = 57 → next multiple of 5 is 60 → difference is 3 → no rounding

Function Description
Complete the function gradingStudents in the editor below.
def gradingStudents(grades):
    # your code here
    
Parameters
grades: a list of integers representing student grades

Returns
A list of integers representing the final rounded grades

Input Format
The first line contains a single integer, n, the number of students.
Each of the next n lines contains a single integer, grade[i], where 0 ≤ grade[i] ≤ 100.

Constraints
1 ≤ n ≤ 60
0 ≤ grade[i] ≤ 100

Sample Input
4
73
67
38
33
Sample Output
75
67
40
33
Explanation
Student 1: grade = 73 → next multiple of 5 = 75 → difference = 2 → rounded to 75
Student 2: grade = 67 → next multiple of 5 = 70 → difference = 3 → no rounding
Student 3: grade = 38 → next multiple of 5 = 40 → difference = 2 → rounded to 40
Student 4: grade = 33 → less than 38 → no rounding
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    result =[]
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            multi = ((grade // 5)+1)*5
            if multi - grade < 3:
                result.append(multi)
            else:
                result.append(grade)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
