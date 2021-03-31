import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = int(1e9) #10억 

n,m = map(int,input().split())
dir = [(0,1),(0,-1),(1,0),(-1,0)]
che = []

time = 0
cnt_che = 0
pre_cnt = 0

for _ in range(n):
    tmp = list(map(int,input().split()))
    che.append(tmp)
    #처음 치즈개수
    for c in tmp: 
        if c==1 : cnt_che += 1

visit = [[False]*m for _ in range(n)]
#첫번째 시작위치
next_q= deque()
next_q.append((0,0))
next_q.append((0,m-1))
next_q.append((n-1,0))
next_q.append((n-1,m-1))
visit[0][0] = True
visit[0][m-1] = True
visit[n-1][0] = True
visit[n-1][m-1] = True

while True:
    time += 1
    pre_cnt = cnt_che
    

    q = next_q
    next_q = deque()
    
    while len(q)>0: #bfs
        row,col = q.popleft()

        for dr,dc in dir:
            next_row = row+dr
            next_col = col+dc

            if next_row <0 or next_row >= n or next_col <0 or next_col >= m:
                continue
            if visit[next_row][next_col] == True : continue

            visit[next_row][next_col] = True
            if che[next_row][next_col] == 1: 
                next_q.append((next_row,next_col))
                cnt_che -= 1
            else : q.append((next_row,next_col))



    if cnt_che == 0: #치즈가 모두 녹음
        print(time)
        print(pre_cnt)
        break