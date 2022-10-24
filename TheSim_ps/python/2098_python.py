import sys
input = lambda : sys.stdin.readline().rstrip()

INF=1e9
N=int(input())

cost=[]
for _ in range(N):
    temp=list(map(int,input().split()))
    cost.append(temp)

visit=[[0 for _ in range(1<<N-1)] for _ in range(N)]

def dfs(i,v):

    if visit[i][v]!=0:
        return visit[i][v]

    if v==(1<<(N-1))-1:
        if cost[i][0]: #출발지로 가는 경로가 있어야 가능
            return cost[i][0]
        return INF
    
    bound=INF

    for j in range(1,N):
        if v & (1<<(j-1)) or not cost[i][j]:
            continue
        temp=dfs(j,v|(1<<(j-1)))+cost[i][j]
        
        if bound>temp:
            bound=temp
        print(j,bin(v|(1<<(j-1)))[2:],temp,bound)
    visit[i][v]=bound #min(visit[i][v],temp)
        
    return bound #visit[i][v]


print(dfs(0,0))

