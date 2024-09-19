#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here

    list = [0,0,0,0,0]
    for x in arr:
        list[x - 1] = list[x - 1] + 1
    
    max = -1
    idx = -1
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
            idx = i
    
    return idx + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
