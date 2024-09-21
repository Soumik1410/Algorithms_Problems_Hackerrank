#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    count = []
    for i in range(101):
        count.append(0)
    
    for x in a:
        count[x] = count[x] + 1
        
    length = -1
    
    for i in range(100):
        l = count[i] + count[i + 1]
        if l > length:
            length = l
    
    return length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
