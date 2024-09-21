#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    i = 1
    h = 1
    q = n // 2
    while i <= q:
        h = 2 * h
        h = h +1
        i = i + 1
    
    if n % 2 == 1:
        h = 2 * h
    
    return h

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
