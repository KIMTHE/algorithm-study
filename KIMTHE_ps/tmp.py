import sys, math, heapq 
from collections import deque #queue를 구현하는 덱 라이브러리
from itertools import combinations, product #조합,순열
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = int(1e9) #10억 

n = int(input())

graph = [[] for _ in range(n)]
visit = [[False]*n for _ in range(n)]

for i in range(n):
    tmp = input()
    graph[i] = [int(num) for num in tmp]


def dfs(now):
    global visit,graph,n

    row,col = now
    visit[row][col] = True
    cnt = 1

    if col != 0 and graph[row][col-1] == 1 and visit[row][col-1] == False :
        cnt += dfs((row,col-1))
    if col != n-1 and graph[row][col+1] == 1 and visit[row][col+1] == False :
        cnt += dfs((row,col+1))
    if row != 0 and graph[row-1][col] == 1 and visit[row-1][col] == False :
        cnt += dfs((row-1,col))
    if row != n-1 and graph[row+1][col] == 1 and visit[row+1][col] == False :
        cnt += dfs((row+1,col))

    return cnt


result = []
cnt = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0 : continue
        if visit[i][j] == True : continue

        result.append(dfs((i,j)))
        cnt += 1

result.sort()
print(cnt)
for i in result : print(i)