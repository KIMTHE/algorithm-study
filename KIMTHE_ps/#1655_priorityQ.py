import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

n = int(input())

max_q = []
min_q = []

for _ in range(n):
    num = int(input())

    if len(max_q) == len(min_q):
        heapq.heappush(min_q,num)

    else : heapq.heappush(max_q,-1*num)


    if len(max_q) > 0 and len(min_q) > 0 :
        if -1*max_q[0] > min_q[0] :
            max_pop = -1*heapq.heappop(max_q)
            min_pop = heapq.heappop(min_q)

            heapq.heappush(max_q,-1*min_pop)
            heapq.heappush(min_q,max_pop)

    if (len(max_q)+len(min_q)) % 2 == 0:
        print(-1*max_q[0])
    else:
        print(min_q[0])
