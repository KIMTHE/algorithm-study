import sys
import math
from collections import deque 
from itertools import combinations, product
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
can = list(map(int,input().split()))
nums = [True]*1001

#1000까지 소수판별_에라토스테네스의 체
nums[1] = False
for i in range(2,int(math.sqrt(1000))+1):
    if nums[i] == True:
        tmp = i
        j = 2

        while tmp*j <= 1000:
            nums[tmp*j] = False
            j += 1

result = 0

for num in can:
    if nums[num]:
        result += 1

print(result)

