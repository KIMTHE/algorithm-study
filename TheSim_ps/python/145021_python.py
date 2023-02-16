import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque
import copy

def safe(lab): #안전 지대 찾기
    t_lab=copy.deepcopy(lab)
    dir=[[1,0],[0,1],[-1,0],[0,-1]]
    for i in range(N):
        for j in range(M):
            if t_lab[i][j]==2:
                q=deque()
                q.append([i,j])
                while q:
                    x,y=q.popleft()

                    for a,b in dir:
                        xa=x+a
                        yb=y+b

                        if 0<=xa<N and 0<=yb<M and t_lab[xa][yb]==0:
                            t_lab[xa][yb]=2
                            q.append([xa,yb])
    
    n=0
    
    for i in range(N):
        for j in range(M):
            if t_lab[i][j]==0:
                n+=1

    return n

def dfs(lab,n,a):
    global answer

    if n==3: #벽을 3개 다 세움
        #print(lab)
        answer=max(answer,safe(lab))
        return
        

    for i in range(a,N):
        for j in range(M):
            if lab[i][j]==0:
                lab[i][j]=1
                dfs(lab,n+1,i)
                lab[i][j]=0
    return


N,M = map(int,input().split())

l=[]
for i in range(N):
    temp=list(map(int,input().split()))
    l.append(temp)
answer=0

dfs(l,0,0)

print(answer)

