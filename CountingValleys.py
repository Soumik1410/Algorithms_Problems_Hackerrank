#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    count = 0
    height = 0
    start = -1
    for step in path:
        if step == "U":
            height = height + 1
        if step == "D":
            height = height - 1
        #print(height)
        if height == -1:
            start = 1
        if height == 0 and start == 1:
            count = count + 1
            start = -1
    
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
