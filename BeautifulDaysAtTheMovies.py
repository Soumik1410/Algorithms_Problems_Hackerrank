#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def rev(x):
    ans = 0
    while x != 0:
        dig = x % 10
        ans = ans * 10 + dig
        x = x // 10
    return ans

def beautifulDays(i, j, k):
    # Write your code here
    count = 0
    for day in range(i, j+1, 1):
        revday = rev(day)
        if abs(day - revday) % k == 0:
            count = count + 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
