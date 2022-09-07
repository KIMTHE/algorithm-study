import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N=int(input())

dir=[[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]] #x,y

for i in range(N):
    board=int(input()) #체스판 한 변의 길이

    visit=[[0 for _ in range(board)] for _ in range(board)]
    
    knight_x,knight_y = map(int,input().split())
    arrive_x,arrive_y = map(int,input().split())

    q=deque()
    q.append([knight_x,knight_y,0])
    visit[knight_x][knight_y]=1
    while q:
        x,y,count=q.popleft()

        if x==arrive_x and y==arrive_y:
            print(count)
            #print(visit[x][y]-1) #count를 사용하지 않고 visit에 거리 계산을 해서 출력하는 방법도 있음
            break
        
        for a,b in dir:
            xa=x+a
            yb=y+b

            if 0<=xa<board and 0<=yb<board and visit[xa][yb]==0: #체스칸을 넘지 않으면
                q.append([xa,yb,count+1])
                visit[xa][yb]=visit[x][y]+1
