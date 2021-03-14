import sys
import math
from collections import deque 
from itertools import combinations, product
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

nums = [True] * (n+1)

for i in range(2,int(math.sqrt(n))+1):
    if nums[i] == False : continue

    tmp = i*2
    while tmp<=n :
        nums[tmp] = False
        tmp += i

pri = []

for i in range(2,n+1):
    if nums[i] == True:
        pri.append(i)


result = 0

for i in range(len(pri)):
    tmp = 0

    for idx in range(i,len(pri)) :
        tmp += pri[idx]

        if tmp == n : 
            result += 1
            break
        elif tmp > n :
            break

        

print(result)