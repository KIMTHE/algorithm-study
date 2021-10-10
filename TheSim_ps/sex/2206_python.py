import sys
input = lambda : sys.stdin.readline().rstrip()

def find():
    count=[[[0]*M for i in range(N)]for a in range(2)] #3차원 리스트 거리
    q=[0,0,0]
    count[0][0][0]+=1
    count[1][0][0]+=1

    while q:
        i=q.pop(0) #현재 위치 세로
        j=q.pop(0) #가로
        over=q.pop(0) #벽을 부셨을때 1 안부시면 0

        if i+1<N: #아래
            if over==0 and load[i+1][j]==1 and count[1][i+1][j]==0: 
                count[1][i+1][j]=count[0][i][j]+1
                q.append(i+1)
                q.append(j)
                q.append(1)

            elif load[i+1][j]==0:
                if over==1 and count[1][i+1][j]==0:
                    if count[1][i+1][j]!=0:
                        count[1][i+1][j]=min(count[1][i][j]+1,count[1][i+1][j])
                    else:
                        count[1][i+1][j]=count[1][i][j]+1
                    q.append(i+1)
                    q.append(j)
                    q.append(1)
                elif count[0][i+1][j]==0 and over==0:
                    count[0][i+1][j]=count[0][i][j]+1
                    q.append(i+1)
                    q.append(j)
                    q.append(0)    

        if j+1<M: #오른
            if over==0 and load[i][j+1]==1 and count[1][i][j+1]==0:
                count[1][i][j+1]=count[0][i][j]+1
                q.append(i)
                q.append(j+1)
                q.append(1)

            elif load[i][j+1]==0:
                if over==1 and count[1][i][j+1]==0:
                    if count[1][i][j+1]!=0:
                        count[1][i][j+1]=min(count[1][i][j]+1,count[1][i][j+1])
                    else:
                        count[1][i][j+1]=count[1][i][j]+1
                    q.append(i)
                    q.append(j+1)
                    q.append(1)
                elif count[0][i][j+1]==0 and over==0:
                    count[0][i][j+1]=count[0][i][j]+1
                    q.append(i)
                    q.append(j+1)
                    q.append(0)   

       
        if i>0: #위
            if over==0 and load[i-1][j]==1 and count[1][i-1][j]==0:
                count[1][i-1][j]=count[0][i][j]+1
                q.append(i-1)
                q.append(j)
                q.append(1)

            elif load[i-1][j]==0:
                if over==1 and count[1][i-1][j]==0:
                    if count[1][i-1][j]!=0: 
                        count[1][i-1][j]=min(count[1][i][j]+1,count[1][i-1][j])
                    else:
                        count[1][i-1][j]=count[1][i][j]+1
                    q.append(i-1)
                    q.append(j)
                    q.append(1)
                elif count[0][i-1][j]==0 and over==0:
                    count[0][i-1][j]=count[0][i][j]+1
                    q.append(i-1)
                    q.append(j)
                    q.append(0)    


        
        if j>0: #왼
            if over==0 and load[i][j-1]==1 and count[1][i][j-1]==0:
                count[1][i][j-1]=count[0][i][j]+1
                q.append(i)
                q.append(j-1)
                q.append(1)

            elif load[i][j-1]==0:
                if over==1 and count[1][i][j-1]==0:
                    if count[1][i][j-1]!=0:
                        count[1][i][j-1]=min(count[1][i][j]+1,count[1][i][j-1])
                    else:
                        count[1][i][j-1]=count[1][i][j]+1
                    q.append(i)
                    q.append(j-1)
                    q.append(1)
                elif count[0][i][j-1]==0 and over==0:
                    count[0][i][j-1]=count[0][i][j]+1
                    q.append(i)
                    q.append(j-1)
                    q.append(0)  
    
    if count[0][N-1][M-1]==0 and count[1][N-1][M-1]==0:
        print(-1)
    elif count[0][N-1][M-1]==0 or count[1][N-1][M-1]==0:
        if count[0][N-1][M-1]==0:
            print(count[1][N-1][M-1])
        elif count[1][N-1][M-1]==0:
            print(count[0][N-1][M-1])
    else:
        print(min(count[0][N-1][M-1],count[1][N-1][M-1]))
    
N,M = (input().split())
N=int(N) #세로
M=int(M) #가로

load=[]

for i in range(N):
    a=list(map(int,input()))
    load.append(a)

find()


