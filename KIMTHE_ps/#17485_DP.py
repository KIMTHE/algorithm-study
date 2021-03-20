import sys, math, heapq 
from collections import deque #queue를 구현하는 덱 라이브러리
from itertools import combinations, product #조합,순열
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = int(1e9) #10억 

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

#3차원 DP, 각 방향까지 고려
DP = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        DP[i][j] = [INF,INF,INF]


dir = [(-1,-1),(-1,0),(-1,+1),(0,0)]

for i in range(m):
    DP[0][i] = [graph[0][i],graph[0][i],graph[0][i]]
    

for row in range(1,n):
    for col in range(m):
        val = graph[row][col]

        for i in range(3):
            pre_row = row+dir[i][0]
            pre_col = col+dir[i][1]

            if pre_row < 0 or pre_row >= n or pre_col <0 or pre_col >= m :
                continue 

            pre_vals = []
            for pre_dir in range(3):
                if i != pre_dir : pre_vals.append(DP[pre_row][pre_col][pre_dir])

            DP[row][col][i] = val+min(pre_vals) 

last_row = DP[n-1]
last_min = []

for i in range(m): last_min.append(min(last_row[i]))

print(min(last_min))