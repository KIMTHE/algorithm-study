import sys
input = lambda : sys.stdin.readline().rstrip()


N,K=map(int,input().split())

answer=[[0]*(N+1) for i in range(N+1)]

for i in range(K):
    a,b=(map(int,input().split()))
    
    answer[a][b]=1


for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if answer[i][k]+answer[k][j]==2:
                answer[i][j]=1

S=int(input())

for i in range(S):
    a,b=(map(int,input().split()))

    if answer[a][b]==1:
        print(-1)
    elif answer[b][a]==1:
        print(1)
    else:
        print(0)
