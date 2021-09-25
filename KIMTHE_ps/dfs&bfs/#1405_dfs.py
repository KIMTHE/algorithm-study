import sys #입출력의 sys
import math  # 수학연산의 math
import heapq  # 우선순위큐에 사용되는 heapq 
import copy # 깊은복사의 copy
from collections import deque  # queue를 구현하는 덱
from itertools import combinations, product  # 조합,순열
from bisect import bisect_left, bisect_right  # 이진탐색
#sys.setrecursionlimit(10**9) # 재귀깊이 설정
def input(): return sys.stdin.readline().rstrip()  # 입력속도빠르게


def dfs(y,x,n,p):
    global answer,N
    if n == N: 
        answer += p
        return

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]

        if per[i]>0 and 0<=ny<=2*N and 0<=nx<=2*N and visit[ny][nx]==0:
            visit[ny][nx] = 1
            dfs(ny,nx,n+1,p*per[i])
            visit[ny][nx] = 0

N,ep,wp,sp,np = map(int,input().split())
dy = [0,0,1,-1]
dx = [1,-1,0,0]
per = [ep/100,wp/100,sp/100,np/100]
answer = 0

visit = [[0]*(2*N+1) for _ in range(2*N+1) ]

visit[N][N] = 1 
dfs(N,N,0,1)
print(answer)