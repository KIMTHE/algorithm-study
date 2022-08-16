import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N,M=input().split()
N=int(N) #가로줄
M=int(M) #세로줄

tomato=[]
for i in range(M):
    tomato.append(list(map(int,input().split())))


move=[[1,0],[0,1],[-1,0],[0,-1]] #아래, 오른쪽,왼쪽,위

q=deque([])
for i in range(M):
    for j in range(N):
        if tomato[i][j]==1:
            q.append([i,j,0])

while q:
    i,j,time=q.popleft()

    for a,b in move:
        a+=i
        b+=j
        if a<M and 0<=a and 0<=b and b<N and tomato[a][b]==0:
            tomato[a][b]=1
            q.append([a,b,time+1])

for i in range(M):
        if 0 in tomato[i]: #다 못익은 상태
            print(-1)
            break
else:
    if time==0:
        print(0)
    else:
        print(time)