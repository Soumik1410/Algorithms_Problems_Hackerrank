#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    res_str = list(s)
    
    if s[8] == "A" and s[0:2] == "12":
        res_str[0] = "0"
        res_str[1] = "0"
    if s[8] == "P" and s[0:2] == "01":
        res_str[0] = "1"
        res_str[1] = "3"
    if s[8] == "P" and s[0:2] == "02":
        res_str[0] = "1"
        res_str[1] = "4"
    if s[8] == "P" and s[0:2] == "03":
        res_str[0] = "1"
        res_str[1] = "5"
    if s[8] == "P" and s[0:2] == "04":
        res_str[0] = "1"
        res_str[1] = "6"
    if s[8] == "P" and s[0:2] == "05":
        res_str[0] = "1"
        res_str[1] = "7"
    if s[8] == "P" and s[0:2] == "06":
        res_str[0] = "1"
        res_str[1] = "8"
    if s[8] == "P" and s[0:2] == "07":
        res_str[0] = "1"
        res_str[1] = "9"
    if s[8] == "P" and s[0:2] == "08":
        res_str[0] = "2"
        res_str[1] = "0"
    if s[8] == "P" and s[0:2] == "09":
        res_str[0] = "2"
        res_str[1] = "1"
    if s[8] == "P" and s[0:2] == "10":
        res_str[0] = "2"
        res_str[1] = "2"
    if s[8] == "P" and s[0:2] == "11":
        res_str[0] = "2"
        res_str[1] = "3"
    
    result = ""
    for x in res_str:
        if x!="P" and x!="A" and x!="M":
            result = result + x
    
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
