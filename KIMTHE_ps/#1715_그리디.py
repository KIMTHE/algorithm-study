import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

n = int(input())
q = []
for _ in range(n):
    tmp = int(input())
    heapq.heappush(q,tmp)

result = 0

while True:
    if len(q) <= 1 : break

    a = heapq.heappop(q)
    b = heapq.heappop(q)

    result += a+b
    heapq.heappush(q,a+b)
    
print(result)