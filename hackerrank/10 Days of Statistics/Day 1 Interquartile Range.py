#!/bin/python3

import math
import os
import random
import re
import sys

from statistics import median
#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    n=len(freqs)
    sum=0
    for x in freqs:
        sum=sum+x
    arr=[]
    for i in range(0,n,1):
        for j in range(0,freqs[i],1):
            arr.append(values[i])
    arr.sort()
    Q1=median(arr[:sum//2])
    Q3=median(arr[(sum+1)//2:])
    print("{:.1f}".format(Q3-Q1))
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
