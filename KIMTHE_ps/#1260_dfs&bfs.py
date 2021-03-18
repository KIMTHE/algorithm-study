import sys, math, heapq 
from collections import deque #queue를 구현하는 덱 라이브러리
from itertools import combinations, product #조합,순열
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = int(1e9) #10억 

n,m,v = map(int,input().split())

E = [[] for _ in range(n+1)] 

for _ in range(m):
    a,b = map(int,input().split())
    E[b].append(a)
    E[a].append(b)

for i in range(1,n+1):
    E[i].sort()

def dfs(E,visit,v):
    visit[v] = True

    print(v,end = ' ')

    for i in E[v]:
        if visit[i] == False:
            dfs(E,visit,i)


def bfs(E,visit,v):
    q = deque()
    q.append(v)
    visit[v] = True
    while len(q) > 0:

        now = q.popleft()
        print(now,end = ' ')
        

        for i in E[now]:
            if visit[i] == False:
                q.append(i)
                visit[i] = True



visit = [False] * (n+1)
dfs(E,visit,v)
print()
visit = [False] * (n+1)
bfs(E,visit,v)