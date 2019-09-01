#Hackerrank Counting Valleys Problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    
    s = list(s)
    
    u = 0
    d = 0
    counter = 0
    i = 0

    while i < n:
        if s[i]=='U':
            u+=1
        else:
            d+=1

        if u == d and s[i] == 'U':
            counter += 1
            d = 0
            u = 0
            
        i+=1   
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
