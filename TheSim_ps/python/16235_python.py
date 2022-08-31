import sys
input = lambda : sys.stdin.readline().rstrip()

N,M,K = map(int,input().split())

A=[]
for i in range(N):
    A.append(list(map(int,input().split())))

ground=[[5]*(N) for i in range(N)]

tree=[[[] for i in range(N)]for i in range(N)]
for i in range(M):
    temp=list(map(int,input().split()))
    tree[temp[0]-1][temp[1]-1].append(temp[2])


for i in range(K):

    for j in range(N):
        for k in range(N):
            temp=tree[j][k]
            
            death=-1
            if temp:
                temp.sort()
                for a in range(len(temp)):
                    if ground[j][k]>=temp[a]: #양분있으면
                        ground[j][k]-=temp[a]
                        temp[a]+=1 #나이 증가
                        
                    else:
                        death=a
                        break
                if death!=-1:
                    
                    tree[j][k]=tree[j][k][:death]
                    
                    for z in range(death,len(temp)):
                        ground[j][k]+=(temp[z]//2)
        
    
    dir=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
    
    for j in range(N):
        for k in range(N):      
            for z in tree[j][k]:
                if z%5==0:
                    for a,b in dir:
                        if 0<=j+a<N and 0<=k+b<N:
                            tree[j+a][k+b].append(1)
                            
    
    for j in range(N):
        for k in range(N):
            ground[j][k]+=A[j][k]

answer=0

for i in range(N):
    for j in range(N):
        answer+=len(tree[i][j])

print(answer)
            