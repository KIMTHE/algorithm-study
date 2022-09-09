import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input()) #도시 갯수
M=int(input()) #버스 갯수

max_value = 10000000

answer=[[max_value for _ in range(N+1)] for _ in range(N+1) ]
for i in range(N+1):
    for j in range(N+1):
        if i==j:
            answer[i][j]=0

for i in range(M):
    a,b,c=map(int,input().split())

    answer[a][b]=min(c,answer[a][b])
    #answer[b][a]=min(c,answer[b][a])



for k in range(N+1): #경유할 k를 제일 위로 하는 것에 주의
    for i in range(N+1):
        for j in range(1,N+1):
            answer[i][j]=min(answer[i][j],answer[i][k]+answer[k][j])

for i in range(1,N+1):
    for j in range(1,N+1):
        if answer[i][j]==max_value:
            print(0,end=" ")
        else:
            print(answer[i][j],end=" ")
    print()