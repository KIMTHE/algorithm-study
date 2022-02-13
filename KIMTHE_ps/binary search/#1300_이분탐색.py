import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

N = int(input())
k = int(input())

s = 1
e = N*N
answer = 0

# 해당 문제의 N*N행렬에서는 특정한 수 이하의 숫자의 개수를 구할수있다.
while s<=e:
    m = (s+e)//2

    cnt = 0
    for i in range(1,N+1):
        cnt += min(m//i,N)

    if cnt<k: s=m+1
    elif cnt>=k:
        answer = m 
        e=m-1

print(answer)



