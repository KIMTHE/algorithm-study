import sys
input = lambda : sys.stdin.readline().rstrip()

N,M = input().split()
N=int(N)
M=int(M)

connect=[[0]*(N+1) for i in range(N+1)] #연결 리스트 1부터 확인하기 위해 +1

output=[]
for i in range(N+1):
    output.append(i) #연결요소

for i in range(M):
    a=list(map(int,input().split()))
    connect[a[0]][a[1]]=a[1]
    connect[a[1]][a[0]]=a[0]

for i in range(1,N+1):
    for j in range(N+1):
        if connect[i][j]!=0:
            output[j]=min(output[j],output[i])

output=set(output)
output=list(output)

print(len(output)-1)