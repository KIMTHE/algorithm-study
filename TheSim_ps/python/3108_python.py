import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N=int(input())

rectangle=[] #사각형 저장

for i in range(N):
    x1,y1,x2,y2=map(int,input().split())
    rectangle.append([(x1+500)*2,(y1+500)*2,(x2+500)*2,(y2+500)*2]) 
    #음수 값을 없애기 위해 +500을 하고 두 점 사이의 구분을 명확하하게 하기 위해 *2를 한다.
value=[[0 for _ in range(2000+1)] for _ in range(2000+1)] #사각형 테두리 칠하기
for i in range(N):
    x1,y1,x2,y2=rectangle[i]

    if x1>x2:
        x1,x2=x2,x1
    if y1>y2:
        y1,y2=y2,y1
    #2가 1보다 큼
    
    for a in range(x1,x2+1):
        for b in range(y1,y2+1):
            if a==x1: #맨 아래만 칠하기
                value[a][b]=1
            elif a==x2: #맨위 칠하기
                value[a][b]=1
            else: #양옆에 칠하기
                value[a][y1]=1
                value[a][y2]=1
    
count=0
if value[1000][1000]==1: #1000,1000은 0,0을 지나는 경우 펜을 내리는 동작이 1나 줄어서 -1을 해준다.
    count-=1

q=deque()
dir=[[0,1],[0,-1],[1,0],[-1,0]]
for i in range(2001): #bfs로 이어져 있는 선 찾기
    for j in range(2001):
        if value[i][j]==1:
            count+=1
            value[i][j]=-1
            q.append([i,j])
            while q:
                x,y=q.popleft()
                for a,b in dir:
                    xa=x+a
                    yb=y+b
                    if 0<=xa<=2000 and 0<=yb<=2000 and value[xa][yb]==1:
                        value[xa][yb]=-1
                        q.append([xa,yb])

print(count)