import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def find():
    direct = [[0,1],[1,0],[0,-1],[-1,0]] # 오,아,왼,위
    q=deque()
    q.append([0,0,0]) #세로, 가로, 벽뚫었는지 여부 0이면 안뚫음 1이면 뚫음
    
    
    while q:
           
        n,m,check=q.popleft() 

        for i,j in direct: #4방향 이동
            if n+i>=0 and n+i<N and m+j>=0 and m+j<M : #맵을 넘는지 확인

                if load[n+i][m+j]==0 and visit[check][n+i][m+j]==0: #다음 값에 이동 가능하고 방문하지 않았을 경우
                    visit[check][n+i][m+j]=visit[check][n][m]+1 #현재값 +1
                    q.append([n+i,m+j,check]) # q에 추가
                elif load[n+i][m+j]==1 and check==0: #벽을 만났을 경우 아직 벽을 안뚫었을 때
                    visit[1][n+i][m+j]=visit[check][n][m]+1 #벽 뚫은 값 1에 현재 값 +1
                    q.append([n+i,m+j,1]) #q에 추가
                
    return load
    
N,M = (input().split())
N=int(N) #세로
M=int(M) #가로

load=[] #맵

for i in range(N): #맵 입력
    a=list(map(int,input()))
    load.append(a)

visit=[[[0]*M for i in range(N)] for j in range(2)] #방문 확인과 거리 확인
visit[0][0][0]=1 #시작 거리는 1, 0이면 벽 안뚫음 1이면 벽 둟음 , N, M

find() # 함수 실행

if N==1 and M==1: #1칸짜리면 거리는 1
    print(1)
elif visit[0][N-1][M-1]==0 and visit[1][N-1][M-1]==0: #마지막 값이 0이면 도착불가 -1
    print(-1)
else:
    if visit[0][N-1][M-1]!=0 and visit[1][N-1][M-1]!=0: #둘중 최소거리 출력
        print(min(visit[0][N-1][M-1],visit[1][N-1][M-1]))
    elif visit[0][N-1][M-1]==0: # 한쪽이 0일 경우 도착불가이므로 다른쪽 출력
        print(visit[1][N-1][M-1])
    else:
        print(visit[0][N-1][M-1])


