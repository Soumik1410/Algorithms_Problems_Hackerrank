#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    m = len(s)
    n = len(t)
    moves = 0
    if n < m:
        j = 0
        while j < n:
            if s[j] == t[j]:
                j =j + 1
            else:
                break
        moves = m - j + n - j
    else:
        j = 0
        while j < m:
            if s[j] == t[j]:
                j = j + 1
            else:
                break
        moves = m - j + n - j
    
    if m + n <= k:
        return "Yes"
    elif k < moves:
        return "No"
    elif (k - moves) % 2 == 0:
        return "Yes"
    else:
        return "No"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
