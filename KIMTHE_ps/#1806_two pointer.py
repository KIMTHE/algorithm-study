import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

N,S = map(int,input().split())
seq = list(map(int,input().split()))
answer = INF

e = -1
tmp = 0

for s in range(N):
    while e<N-1 and tmp<S:
        e+=1
        tmp += seq[e]

    if tmp>=S:
        answer = min(answer,e-s+1)

    tmp -= seq[s]




if answer == INF: print(0)
else: print(answer)