import sys
input = lambda : sys.stdin.readline().rstrip()

INF=1000000
N,M=map(int,input().split())


edge=[]
for _ in range(M):
    A,B,C=map(int,input().split())
    edge.append((A-1,B-1,C))


answer=[INF]*N
answer[0]=0
value=0
for i in range(N):
    for j in range(M):
        a,b,c=edge[j]
        if answer[a]!=INF and answer[a]+c < answer[b]:
            answer[b]=answer[a]+c
            if i==N-1:
                value=1
                break

if value:
    print(-1)
else:
    for i in range(1,len(answer)):
        if answer[i]==INF:
            print(-1)
        else:
            print(answer[i])