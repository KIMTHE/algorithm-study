import sys
input = lambda : sys.stdin.readline().rstrip()

def find(Dp,x,y):
    
    if Dp[x][y]==-1:
        return 0

    if Dp[x][y]!=0:
        return Dp[x][y]
    
    else:
        dir=[[0,1],[0,-1],[-1,0],[1,0]]

        for i,j in dir:
            if 0<=x+i<M and 0<=y+j<N and stair[x][y]<stair[x+i][y+j]:
                Dp[x][y]+=find(Dp,x+i,y+j)
        if Dp[x][y]==0:
            Dp[x][y]=-1
            return 0

    return Dp[x][y]

M,N=map(int,input().split())

stair=[]
for i in range(M):
    stair.append(list(map(int,input().split())))

Dp=[[0]*N for i in range(M)]

Dp[0][0]=1
print(find(Dp,M-1,N-1))





# q=[]
# q.append([0,0])
# visit=[[0]*N for i in range(M)]
# answer=[[0]*N for i in range(M)]

# dir=[[0,1],[0,-1],[-1,0],[1,0]]
# while q:
#     x,y=q.pop(0)
    
#     for i,j in dir:
#         x_i=x+i
#         y_j=y+j

#         if 0<=x_i<M and 0<=y_j<N and stair[x][y]>stair[x_i][y_j]:
#                 if
#                 answer[x_i][y_j]=answer[x][y]+1
#                 q.append([x_i,y_j])
                

# print(answer[-1][-1])
    