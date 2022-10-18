import sys
input = lambda : sys.stdin.readline().rstrip()

count=0

def dfs(x,y,visit):
    
    #visit=[[0 for _ in range(M)] for _ in range(N)]
    global count
    num=0 #갯수
    num+=1
    count+=1
    visit[x][y]=count
    dir=[[1,0],[-1,0],[0,1],[0,-1]]
    stack=[]
    stack.append([x,y])

    while stack:
        a,b=stack.pop()

        for i,j in dir:
            ai=a+i
            bj=b+j

            if 0<=ai<N and 0<=bj<M and visit[ai][bj]==0:
                visit[ai][bj]=count
                num+=1
                stack.append([ai,bj])

    return visit,num



N,M = map(int,input().split())

m=[]
wall=[]
visit=[[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    value=list(input())
    m.append(value)
    for j in range(len(value)):
        if value[j]=='1':
            visit[i][j]=-1
            wall.append([i,j])

d={}
for i in range(N):
    for j in range(M):
        if m[i][j]=='0' and visit[i][j]==0:
            visit,num=dfs(i,j,visit)
            d[count]=num

dir=[[1,0],[-1,0],[0,1],[0,-1]]

answer=[[0 for _ in range(M)] for _ in range(N)]
for x,y in wall:
    answer[x][y]+=1

    s=set()
    for a,b in dir:
        xa=x+a
        yb=y+b

        if 0<=xa<N and 0<=yb<M and visit[xa][yb]!=-1:
            s.add(visit[xa][yb])
            
    for k in s:
        answer[x][y]+=d[k]   
    answer[x][y]%=10


for i in range(len(answer)):
    for j in answer[i]:
        print(j,end="")
    if i!=len(answer)-1:
        print()

