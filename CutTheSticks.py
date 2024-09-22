#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here

    n = len(arr)
    result = []
    result.append(len(arr))
    while n > 0:
        minlength = 1001
        for x in arr:
            if x < minlength:
                minlength = x
        i = 0
        print(minlength)
        while i < n:
            if arr[i] == minlength:
                del arr[i]
                n = n - 1
            else:
                i = i + 1
        
        n = len(arr)
        for i in range(n):
            if arr[i] > minlength:
                arr[i] = arr[i] - minlength
        if n == 0:
            break
        result.append(n)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
