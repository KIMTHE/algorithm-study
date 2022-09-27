import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())

    ground=[[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        x,y = map(int,input().split())
        ground[x][y]=1

    visit=[[0 for _ in range(N)] for _ in range(M)]
    dir=[[1,0],[0,1],[-1,0],[0,-1]]
    answer=0
    for i in range(M):
        for j in range(N):
            if ground[i][j]==1 and visit[i][j]==0:
                q=deque()
                q.append([i,j])
                while q: #배추 찾기
                    a,b=q.popleft()
                    
                    for x_value,y_value in dir:
                        ax=a+x_value
                        by=b+y_value

                        if 0<=ax<M and 0<=by<N:
                            if ground[ax][by]==1 and visit[ax][by]==0:
                                q.append([ax,by])
                                visit[ax][by]=1
                answer+=1
    print(answer)


                
                
            
