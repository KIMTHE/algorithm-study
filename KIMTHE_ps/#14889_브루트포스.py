import sys
import math
from collections import deque 
from itertools import combinations, product
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
s = [[0] for _ in range(n+1)]

for i in range(1,n+1):
    s[i] += list(map(int,input().split()))

nums = [i for i in range(1,n+1)]
cases = list(combinations(nums,n//2)) 

result = 101
len_case = len(cases)

for i in range(len_case//2):
    case1 = cases[i]
    case2 = cases[len_case-1-i]

    score1 = 0
    score2 = 0

    for j in case1 :
        for k in case1 :
            score1 += s[j][k]

    for j in case2 :
        for k in case2 :
            score2 += s[j][k]

    tmp = abs(score1-score2)
    if tmp < result: result = tmp
#print(s)
print(result)