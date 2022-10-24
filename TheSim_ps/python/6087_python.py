import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

W,H = map(int,input().split())
mapp=[]
c_value=[]
for i in range(H):
    value=list(input())
    mapp.append(value)

for i in range(H):
    for j in range(W):
        if mapp[i][j]=='C':
            c_value.append([i,j])

dir=[[1,0],[0,1],[-1,0],[0,-1]] #아래,오른쪽,위,왼쪽
visit=[[10000 for _ in range(W)] for _ in range(H)]
visit[c_value[0][0]][c_value[0][1]]=0 #첫 시작은 0

q=deque()
q.append([c_value[0][0],c_value[0][1],0,-1]) #x,y좌표, 거울 갯수, 이전 진출 방향
answer=10000

while q:
    x,y,m,d=q.popleft() #x,y좌표, 거울 갯수, 이전 진출 방향

    if x==c_value[1][0] and y==c_value[1][1]: #도착
        answer=min(answer,m)
        continue

    for i in range(len(dir)):
        xa=x+dir[i][0]
        yb=y+dir[i][1]

        if 0<=xa<H and 0<=yb<W and mapp[xa][yb]!='*' and (visit[xa][yb]>m or (visit[xa][yb]==m and d==i)): #거울의 갯수가 더 작으면 진출
            if d==-1: #처음 시작 거울 생성 x
                visit[xa][yb]=m
                q.append([xa,yb,m,i])
            elif d!=i: #거울 생성
                visit[xa][yb]=m+1
                q.append([xa,yb,m+1,i])
            else: #거울 없이 진출, 직선 이동
                visit[xa][yb]=m
                q.append([xa,yb,m,i])
# print(visit)
print(answer)