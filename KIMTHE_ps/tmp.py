import sys
import math
from collections import deque 
from itertools import combinations, product
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
nums = [int(input()) for _ in range(n)]

inter = []

for i in range(1,n) : inter.append(nums[i]-nums[i-1])

def uclid(a,b):
    if a>b: a,b = b,a
    tmp = b%a

    if tmp == 0: return a

    else : return(uclid(tmp,a))
    
tmp = inter[0]
for i in inter:
    tmp = uclid(tmp,i)

result = 0

for i in inter:
    result += (i // tmp - 1)


print(result)