# Enter your code here. Read input from STDIN. Print output to STDOUT
#First code
import numpy as np
import statistics
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))