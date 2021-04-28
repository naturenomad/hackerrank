# https://www.hackerrank.com/challenges/grading/problem

# GRADING STUDENTS

# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade. 
# If the difference between the grade and the next multiple of is less than 38, 
# round up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    for index, grade in enumerate(grades):
        if grade >= 38 and (grade%5) > 2 :
            grades[index] = grade + (5-(grade%5))
    return(grades)

# Calling internally :
#gradingStudents([73, 67, 38, 33])
#print(gradingStudents([45,34,76,45,98,14,56]))

# Calling externally :
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    grades_count = int(input().strip())
    
    grades = []
    
    for i in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    
    result = gradingStudents(grades)
    
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
