#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    
    pagesfromstart = p//2
    pagesfromend = (n - p)//2
    if n % 2 == 0 and p == n - 1:
        pagesfromend = 1
    
    if pagesfromstart<pagesfromend:
        return pagesfromstart
    else:
        return pagesfromend

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()