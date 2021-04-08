import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = int(1e9) #10억 

n = int(input())

cost = [0]
cost += list(map(int,input().split()))

DP = [0]*(n+1)

for i in range(1,n+1): #i개 카드팩까지 구매할때
    for j in range(1,n+1): #j개 카드구매 최대값
        if i > j : continue

        if j % i == 0:
            DP[j] = max(DP[j],(j//i)*cost[i])

        DP[j] = max(DP[j],DP[j-i]+cost[i])

print(DP[-1])