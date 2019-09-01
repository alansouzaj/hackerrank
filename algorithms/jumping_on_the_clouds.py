#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    i = 0
    n = len(c)
    counter = 0

    if n == 2:
        return 1
    else:
    
        while i < n-2:

            if c[i+2] == 0:
                i+=2
                counter+=1
            else:
                i+=1
                counter+=1

            if i == n-2:
                counter+=1
            
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
