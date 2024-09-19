#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    max = scores[0]
    min = scores[0]
    
    maxcount = 0
    mincount = 0
    
    for score in scores:
        if score>max:
            max = score
            maxcount = maxcount + 1
        if score<min:
            min = score
            mincount = mincount + 1
    
    return list((maxcount, mincount))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
