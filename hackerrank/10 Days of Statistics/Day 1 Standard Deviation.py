#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    n=len(arr)
    sum=0
    for x in range(0,n,1):
        sum=sum+arr[x]
    arg=sum/n
    sum=0
    for x in range(0,n,1):
        sum=sum+((arr[x]-arg)*(arr[x]-arg))
    arg=sum/n
    print(round(math.sqrt(arg),1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
