import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N=list(map(int,input().split()))

shark=[]

for i in range(N[0]):
    shark.append(list(map(int,input().split())))

big=0

for i in range(N[0]):
    for j in range(N[1]):
        if shark[i][j]==0:
            que = deque()
            
            visit=[[0]*N[1] for _ in range(N[0])]

            dir=[[-1,-1],[-1,-0],[-1,+1],[0,-1],[0,+1],[+1,-1],[+1,0],[+1,+1]]

            que.append(i)
            que.append(j)
            c=0
            end=0

            while que:
                i=que.popleft()
                j=que.popleft()

                for k in range(8):    
                    a,b=dir[k]

                    if a+i>=0 and a+i<N[0] and b+j>=0 and b+j<N[1]:
                        if shark[a+i][b+j]==1:
                            end=1
                            break
                        if visit[a+i][b+j]==1:
                            continue
                        visit[a][b]=1

                        que.append(a+i)
                        que.append(b+j)
                        
                shark[i][j]+=2
                
                if end==1:
                    break 

            

print(shark)