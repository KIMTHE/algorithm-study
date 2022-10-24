import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def find(temp_house,door):
    
    dir=[[-1,0],[1,0],[0,-1],[0,1]] #상,하,좌,우
    q=deque()

    for a in range(len(dir)): #문에서 상하좌우로 이동할 수 잇는 공간 찾기
        i=dir[a][0]
        j=dir[a][1]
        if 0<=door[0][0]+i<N and 0<=door[0][1]+j<N and temp_house[door[0][0]+i][door[0][1]+j]!='*':
            q.append([door[0][0],door[0][1],a]) #문과 이동방향 저장

    
    visit=[[[-1 for _ in range(N)] for _ in range(N)] for _ in range(4)] #시작하는 문에 방문 표시하기
    for i in range(4):
            visit[i][door[0][0]][door[0][1]]=0

    while q: #bfs로 찾기
        x1,y1,d=q.popleft()
        x=x1
        y=y1

        while True: #움직이는 점에서 한방향으로 쭉 움직인다.
            if x==door[1][0] and y==door[1][1]: #움직이다 다른 문 발견하면 종료
                print(visit[d][x1][y1])
                return

            x=x+dir[d][0] #d방향으로 쭉 이동
            y=y+dir[d][1]

            if 0<=x<N and 0<=y<N: #범위를 넘어서면 종료\

                if temp_house[x][y]=='*': #벽이면 종료
                    break
                    
                if temp_house[x][y]=='!': #거울을 설치할지 여부 결정
                    value=0 #상하로 오면 좌우로 이동, 좌우로 오면 상하로 이동
                    value2=0 #그래서 2개의 값으로 이동한다.
                    if d==0: 
                        value=3
                        value2=2
                    elif d==1:
                        value=2
                        value2=3
                    elif d==2: 
                        value=1
                        value2=0
                    elif d==3:
                        value=0
                        value2=1
                    
                    #처음 방문 or 중복 방문일 경우 좀 더 최단거리일 때 추가
                    if visit[value][x][y]==-1 or visit[value][x][y]>visit[d][x1][y1]+1:
                        visit[value][x][y]=visit[d][x1][y1]+1
                        q.append([x,y,value])
                        

                    if visit[value2][x][y]==-1 or visit[value2][x][y]>visit[d][x1][y1]+1:
                        visit[value2][x][y]=visit[d][x1][y1]+1
                        q.append([x,y,value2])

            else:
                break


N=int(input())

house=[]
door=[]
for i in range(N):
    value=list(input())
    house.append(value)
    
    for j in range(len(value)):
        if value[j]=='#': #문이라면
            door.append([i,j])

find(house,door)


