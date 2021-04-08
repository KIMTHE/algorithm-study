import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = int(1e9) #10억 

n = int(input())

tmp = []

for _ in range(n):
    a,b = map(int,input().split())
    tmp.append((a,b))

tmp.sort()
DP = [0]*n

for i in range(n):
    DP[i] = 1
    for j in range(i):
        if tmp[i][1] > tmp[j][1] :
            DP[i] = max(DP[i],DP[j]+1)

print(n-max(DP))

