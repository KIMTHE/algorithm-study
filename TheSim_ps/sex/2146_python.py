import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

bridge=[]
for i in range(N):
    bridge.append(list(map(int,input().split())))

visit=[[0]*N for i in range(N)]
dir=[[1,0],[-1,0],[0,1],[0,-1]] #동서남북 방향

ground=0 #영역 값
for i in range(N):
    for j in range(N):
        if visit[i][j]==0 and bridge[i][j]==1:
            ground+=1
            q=[]
            q.append([i,j])
            visit[i][j]=ground
            
            while q:
                a,b=q.pop(0)
                
                for x,y in dir:
                    if 0<=x+a < N and 0<=y+b < N: #범위를 넘지 않으면
                        if bridge[x+a][y+b]==1 and visit[x+a][y+b]==0:
                            
                            q.append([x+a,y+b])
                            visit[x+a][y+b]=ground

answer=N*N #섬과 섬사이의 최소값

for i in range(N):
    for j in range(N): #양옆으로 다른 땅으로 발견할 때까지 이동 그리고 최솟값 찾기
        
        if bridge[i][j]==1:
            q=[]
            q.append([i,j])
            research=[[0]*N for i in range(N)] #방문 여부
            research[i][j]=1
            while q:
                a,b=q.pop(0)
                
                for x,y in dir:
                    if 0<=x+a < N and 0<=y+b < N: #범위를 넘지 않으면
                        if visit[x+a][y+b]!=visit[i][j] and visit[x+a][y+b]!=0: #새로운 섬을 발견
                            answer=min(answer,(abs(x+a-i)+abs(y+b-j)))
                            break
                        if research[x+a][y+b]==0 and (abs(x+a-i)+abs(y+b-j))<=answer:
                            q.append([x+a,y+b])
                            research[x+a][y+b]=1


print(answer-1)

