import sys  # 입출력의 sys
import math  # 수학연산의 math
import heapq  # 우선순위큐에 사용되는 heapq
import copy  # 깊은복사의 copy
from collections import deque  # queue를 구현하는 덱
from itertools import combinations, product  # 조합,순열
from bisect import bisect_left, bisect_right  # 이진탐색
#sys.setrecursionlimit(100000) # 재귀깊이 설정
def input(): return sys.stdin.readline().rstrip()  # 입력속도빠르게
INF = math.inf

N = int(input())
answer = 0
room = []

C = [tuple(map(int,input().split())) for _ in range(N)]
C.sort()

for s1,e1 in C:
    while room:
        e2,s2 = room[0]
        if e2 <= s1: heapq.heappop(room)
        else: break

    heapq.heappush(room,(e1,s1)) 
    answer = max(answer,len(room))

print(answer)