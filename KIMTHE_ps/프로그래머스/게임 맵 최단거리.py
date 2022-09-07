import sys, math, heapq,copy,itertools #수학연산, 우선순위큐, 순열조합
from collections import deque #queue를 구현하는 덱
from copy import deepcopy #깊은복사
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    visit = [[False]*m for _ in range(n)]
    record_cnt = [[n*m]*m for _ in range(n)]
    
    if maps[n-2][m-1] == 0 and maps[n-1][m-2] == 0 : return -1
    
    Q = deque()
    visit[0][0] = True
    record_cnt[0][0] = 1
    Q.append([(0,0),1])
    
    while Q:
        now,cnt = Q.popleft()
        r,c = now
        
        if r==n-1 and c==m-1:
            return cnt
        
        for dr,dc in dir:
            nr,nc = r+dr, c+dc
            
            if nr<0 or nr>=n or nc<0 or nc>=m: continue
            if maps[nr][nc] == 0 or visit[nr][nc] == True: continue
            if record_cnt[nr][nc] < cnt+1: continue
            
            visit[nr][nc] = True
            record_cnt[nr][nc] = cnt+1
            Q.append([(nr,nc),cnt+1])
            
    return -1

