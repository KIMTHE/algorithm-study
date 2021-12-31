import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

N = int(input())
A = list(map(int, input().split()))

case = []

for i in A:
    if len(case)==0: case.append(i)
    elif case[-1]<i: case.append(i)
    else: case[bisect_left(case,i)]=i

print(len(case))
        
