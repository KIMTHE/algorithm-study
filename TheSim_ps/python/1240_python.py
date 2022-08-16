import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N=list(map(int,input().split()))

connect=[list() for i in range(N[0]+1)]

for i in range(N[0]-1):
    a=list(map(int,input().split()))
    connect[a[0]].append((a[1],a[2]))
    connect[a[1]].append((a[0],a[2]))

for i in range(N[1]):
    a=list(map(int,input().split()))
    
    q=deque()
    cost=[-1]*(N[0]+1)
    
    def dfs(start,end):
        q.append(start)    
        cost[start]=0
        while q:
            a=q.popleft()
            if a==end:
                break
            for k in connect[a]:
                if cost[k[0]]==-1:
                    cost[k[0]]=cost[a]+k[1]
                    q.append(k[0])
        return cost[end]
                                 

    print(dfs(a[0],a[1]))

    
    