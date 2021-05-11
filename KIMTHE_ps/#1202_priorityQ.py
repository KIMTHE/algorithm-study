import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

n,k = map(int,input().split())
item = []
bag = [] #min heap

for _ in range(n):
    a,b = map(int,input().split())
    item.append((a,b))
item.sort()

for _ in range(k): heapq.heappush(bag,int(input()))

can_thief = [] #max heap
idx = 0
result = 0

for _ in range(k):
    capacity = heapq.heappop(bag)

    while idx<n:
        if item[idx][0] <= capacity:
            heapq.heappush(can_thief,item[idx][1]*-1)
            idx += 1
        else :
            break
    
    if len(can_thief) > 0:
        result += -1*heapq.heappop(can_thief)

print(result)


