#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sum = 0
    max = -1
    min = 100000000000
    
    for x in arr:
        sum = sum + x
        if x>max:
            max = x
        if x<min:
            min = x
    
    print(str(sum - max) + " " + str(sum-min))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
