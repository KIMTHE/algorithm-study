import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = int(1e9) #10억 

n,k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
result = 0

coin.sort()

DP = [0]*(k+1)
pre_DP = DP

for i in range(1,k+1):
    if i>=coin[0] and i % coin[0] == 0:
        DP[i] = 1

#i번째 동전까지 사용 = i-1번째 동전까지사용+a
for i in range(1,n): #i번쨰 동전까지 사용
    pre_DP = DP
    pre_DP[0] = 1
    for j in range(1,k+1): #1원부터 k원까지 
        if j<coin[i] : DP[j] = pre_DP[j]
        else:
            DP[j] = pre_DP[j]+pre_DP[j-coin[i]]


print(DP[-1])



