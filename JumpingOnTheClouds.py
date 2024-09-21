#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    
    n = len(c)
    i = k % n
    e = 99
    while i != 0:
        if c[i] == 1:
            e = e -2
        i = (i + k) % n
        e = e - 1
    
    if c[0] == 1:
        e = e - 2
    
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
