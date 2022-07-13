import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

n,c = map(int,input().split())
house = [int(input()) for _ in range(n)]

house.sort()


start, end = 1,house[-1]-house[0]

while start <= end :
    mid = (start+end) // 2

    count = 1
    now = house[0]

    while True:
        next = now+mid

        if next > house[-1] : break

        next_idx = bisect_left(house,next)
        now = house[next_idx]
        count += 1

    if count >= c:
        answer = mid 
        start = mid+1
    else : end = mid-1

print(answer)

        

