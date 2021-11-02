import sys
input = lambda : sys.stdin.readline().rstrip()

M,N,K=map(int,input().split())


rectangle=[[0]*N for i in range(M)]

for i in range(K):
    x_x,x_y,y_x,y_y=map(int,input().split())


    for x in range(x_x,y_x):
        for y in range(x_y,y_y):
            rectangle[M-y-1][x]=1 

area=[]

for i in range(M):
    for j in range(N):
        if rectangle[i][j]==0:
            area.append([i,j])     

direct=[[0,1],[1,0],[0,-1],[-1,0]] #오,아,왼,위

answer=[]

while area:
    a,b=area.pop(0) #빈공간
    
    
    if rectangle[a][b]==0:
        count=0
        q=[]
        q.append([a,b])

        while q:
            a,b=q.pop(0)
            for i,j in direct:
                if i+a>=0 and i+a<M and j+b>=0 and j+b<N and  rectangle[i+a][j+b]==0:
                    q.append([i+a,j+b])
                    rectangle[i+a][j+b]=1
                    count+=1
        
        if count==0:
            count+=1

        answer.append(count)


print(len(answer))
answer.sort()

for i in answer:
    print(i, end=' ')