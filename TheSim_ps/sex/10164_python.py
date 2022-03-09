import sys
input = lambda : sys.stdin.readline().rstrip()

N,M,K=map(int,input().split()) #M열세로, N행가로

num=[[0]*(M+1) for i in range(N+1)]
visit=[[0]*(M+1) for i in range(N+1)] #방문 여부
dir=[[0,1],[1,0]] #오른쪽, 아래

num[1][1]=1
visit[1][1]=1
for i in range(1,N+1):
    for j in range(1,M+1):
        if visit[i][j]==0:
            num[i][j]=num[i-1][j]+num[i][j-1]
            visit[i][j]=1

if K!=0:
    b=(K//M)+1 #K의 열 위치
    a=(K%M) #K의 행 위치
    if K%M==0:
        b-=1
        a=M
        
    
    for i in range(b,N+1):
        num[i][a]=num[b][a]

    for i in range(a,M+1):
        num[b][i]=num[b][a]

    for i in range(b+1,N+1):
        for j in range(a+1,M+1):
            num[i][j]=num[i-1][j]+num[i][j-1]
    
print(num[N][M])