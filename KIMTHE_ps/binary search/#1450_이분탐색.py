import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

n,c = map(int,input().split())

weights = list(map(int,input().split()))
weights.sort()

a_w = weights[:n//2]
b_w = weights[n//2:]

a_c = [0]
b_c = [0]

#1~n까지 조합으로 경우의수 뽑음
for i in range(1,n+1):
    a_c += list(map(sum,combinations(a_w,i)))
for i in range(1,n+1):
    b_c += list(map(sum,combinations(b_w,i)))

#print(a_c,b_c)

a_c.sort()
b_c.sort()

answer = 0
for i in a_c:
    if c-i < 0 : continue
    answer += bisect_right(b_c,c-i)

print(answer)

