import sys
input = lambda : sys.stdin.readline().rstrip()

V,E = map(int,input().split())
INF=10000000000

road=[[INF for _ in range(V)] for _ in range(V)]
for i in range(E):
    a,b,c=map(int,input().split())
    road[a-1][b-1]=c

visit=[[INF for _ in range(V)] for _ in range(V)]

for k in range(V):
    for i in range(V):
        for j in range(V):
            if road[i][j]>road[i][k]+road[k][j]:
                road[i][j]=road[i][k]+road[k][j]

answer=INF
for i in range(V):
    answer=min(answer,road[i][i])

if answer==INF:
    print(-1)
else:
    print(answer)