import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N,M = map(int,input().split())

move=dict()
for i in range(N+M):
    a,b=map(int,input().split())
    move[a]=b

dic=[1,2,3,4,5,6]

visit=[0]*101
q=deque()
q.append(1)
visit[1]=0

while q:
    num=q.popleft()
    if num==100:
        break
    for i in dic:
        ni=num+i
        if ni<=100:
            if ni in move.keys(): #뱀 사다리 이동
                ni=move[ni]
            if visit[ni]==0:
                q.append(ni)
                visit[ni]=visit[num]+1

print(visit[100])