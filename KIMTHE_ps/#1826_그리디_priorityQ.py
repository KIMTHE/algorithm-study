import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

n = int(input())
GAS = []

for _ in range(n):
    a,b = map(int,input().split())
    heapq.heappush(GAS,(a,b)) #min heap

L,P = map(int,input().split())

result = 0
now = 0

Q = [] #max heap

while L > P+now :

    while GAS: #갈수있는 주유소를 max heap에 모두 push
        if GAS[0][0] > P+now : break

        a,b = heapq.heappop(GAS)
        heapq.heappush(Q,(-b,-a))

    if len(Q) == 0:
        result = -1
        break

    a,b = heapq.heappop(Q)
    P += -a+now+b
    now = -b
    result += 1

print(result)
