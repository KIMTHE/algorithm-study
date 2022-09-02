import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

num=[]
for i in range(N):
    num.append(list(map(int,input().split())))

if N==1:
    print(0)
else:
    value=[[0]*N for i in range(N)]

    for i in range(1,N):
        for j in range(N-i):
            if i==1:
                value[j][j+i] = num[j][0]*num[j][1]*num[j+i][1]
                continue
            value[j][j+i] = 2**32

            for k in range(j,j+i):
                value[j][j+i]=min(value[j][j+i], value[j][k]+value[k+1][j+i] + num[j][0]*num[k][1]*num[j+i][1])
    
    print(value[0][-1])