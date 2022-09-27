import sys
input = lambda : sys.stdin.readline().rstrip()

N,M=map(int,input().split())
people=[]
for i in range(N):
    people.append(list(map(int,input().split())))

nsum=[[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        nsum[i][j] = people[i-1][j-1] + nsum[i-1][j] + nsum[i][j-1] - nsum[i-1][j-1]

K=int(input())

for i in range(K):
    x1,y1,x2,y2=map(int,input().split())

    value=nsum[x1-1][y1-1] + nsum[x2][y2] - nsum[x1-1][y2] - nsum[x2][y1-1]
    print(value)