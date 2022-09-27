import sys
input = lambda : sys.stdin.readline().rstrip()
import copy

def find(cave,R,C): #동굴에 바닥과 이어진 미네랄만 visit 체크해서 리턴
    
    visit=[[0 for _ in range(C)] for _ in range(R)]

    temp=[] #'x'인 값 임시 보관
    for i in range(R): #위에서 부터 찾으니 자동으로 temp 맨뒤에는 맨 아래 값이 들어간다.
        for j in range(C): 
            if cave[i][j]=='x':
                temp.append([i,j]) 
                if i==R-1: #바닥과 이어진 미네랄만 체크
                    visit[i][j]=1

    dir=[[0,1],[1,0],[0,-1],[-1,0]]
    count=1
    while temp:
        x,y=temp.pop()

        if visit[x][y]==0: #바닥이 아닌 다른 블록
            count+=1
            visit[x][y]=count

        for a,b in dir:
            xa=x+a
            yb=y+b

            if 0<=xa<R and 0<=yb<C and visit[xa][yb]==0 and cave[xa][yb]=='x': #바닥과 합쳐지는 미네랄이라면
                visit[xa][yb]=count
                temp.append([xa,yb])
                
    return visit

R,C = map(int,input().split())

cave=[]
for i in range(R):
    temp=list(input())
    cave.append(temp)

N=int(input())
H=list(map(int,input().split()))

for i in range(N):
    if i%2==0: #짝수이면 왼쪽 홀수이면 오른쪽부터 던진다.
        for j in range(C):
            if cave[R-H[i]][j]=='x':
                cave[R-H[i]][j]='.'
                break
        cave_temp=copy.deepcopy(find(cave,R,C))
    
    else: #오른쪽 부터
        for j in range(C-1,-1,-1):
            if cave[R-H[i]][j]=='x':
                cave[R-H[i]][j]='.'
                break
        cave_temp=copy.deepcopy(find(cave,R,C))
    
    min_value=1000 #1과 만나는 최소의 값
    temp=[]
    for k in range(R):
        for z in range(C):
            if cave_temp[k][z]==2:
                temp.append([k,z])

    for k,z in temp:
        for j in range(1,R):
            if k+j>=R-1 or cave_temp[k+j+1][z]==1:
                min_value=min(j,min_value)
                break

    cave_value=[['.' for _ in range(C)] for _ in range(R)]
    for k in range(R):
        for z in range(C):
            
            if cave_temp[k][z]==1:
                cave_value[k][z]='x'
            elif cave_temp[k][z]==2:
                cave_value[k+min_value][z]='x'


    cave=copy.deepcopy(cave_value)
 
for i in range(R):
    for j in range(C):
        print(cave[i][j],end="")
    if i<R-1:
        print()

    
        

                



    