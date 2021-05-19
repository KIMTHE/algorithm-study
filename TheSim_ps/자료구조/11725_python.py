import sys
from typing import Coroutine
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(100001)
N=int(input())

connect=[[] for i in range(N+1)] #1~N개의 연결리스트

for i in range(N-1):
    a=list(map(int,input().split()))
    connect[a[0]].append(a[1])
    connect[a[1]].append(a[0])

parent=[0]*(N+1)
visit=[0]*(N+1)

def dfs(i):  
    visit[i]=1 #방문 표시
    for j in connect[i]:
       if visit[j]!=1:  
        if parent[j]==0:
            parent[j]=i
            dfs(j)

dfs(1)

for i in range(2,N+1):
    print (parent[i])