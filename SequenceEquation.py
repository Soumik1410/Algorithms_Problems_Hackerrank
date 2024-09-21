#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    n = len(p)
    result = []
    for i in range(1, n+1, 1):
        x = -1
        for j in range(n):
            if p[j] == i:
                x = j + 1
                break
        
        for j in range(n):
            if p[j] == x:
                x = j + 1
                break
        
        result.append(x)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
