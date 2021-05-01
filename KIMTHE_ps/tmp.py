import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

n,c = map(int,input().split())
house = [int(input()) for _ in range(n)]
router = [0]*c

house.sort()
router[0] = house[0]

def b_s(start,end,idx):
    if start>end : return


interval = n//c
start = 1
end = 1+interval
for i in range(1,c):
