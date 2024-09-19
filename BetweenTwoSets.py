#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def GCD(a, b):
    if b==0:
        return a
    return GCD(b, a % b)

def LCM(a, b):
    return (a * b)/GCD(a, b)

def getTotalX(a, b):
    # Write your code here
    lcm = 1
    gcd = b[0]
    
    for x in a:
        lcm = LCM(lcm, x)
    
    for x in b:
        gcd = GCD(gcd, x)
    
    count = 0
    i = lcm
    while lcm<=gcd:
        if (gcd % lcm) == 0:
            count = count + 1
        lcm = lcm + i
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
