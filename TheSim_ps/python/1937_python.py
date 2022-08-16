import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5)

def find(answer,i,j):
    
    if answer[i][j]!=0:
        return answer[i][j]

    dir=[[0,1],[1,0],[0,-1],[-1,0]]

    value=0
    for a,b in dir:
         if 0<=a+i<N and 0<=b+j<N and bamboo[i][j]>bamboo[a+i][b+j]:
            value=max(value,find(answer,a+i,b+j))
    
    answer[i][j]=value+1

    return answer[i][j]

N=int(input())

bamboo=[]
for i in range(N):
    bamboo.append(list(map(int,input().split())))

answer=[[0]*N for i in range(N)]

big=0
for i in range(N):
    for j in range(N):
        big=max(big,find(answer,i,j))   
print(big)

# def find(i,j):

#     q=[]
#     q.append([i,j,1])
#     dir=[[0,1],[1,0],[0,-1],[-1,0]]
#     visit=[[0]*N for i in range(N)]
#     visit[i][j]=1

#     ans=0
#     while q:
#         a,b,value=q.pop(0)
#         ans=max(value,ans)

#         for x,y in dir:
#             if 0<=a+x<N and 0<=b+y<N and visit[a+x][b+y]==0 and bamboo[a][b]<bamboo[a+x][b+y]:
#                 q.append([a+x,b+y,value+1])
#                 visit[a+x][b+y]=1

#     return ans

# N=int(input())

# bamboo=[]
# for i in range(N):
#     bamboo.append(list(map(int,input().split())))


# answer=0
# for i in range(N):
#     for j in range(N):
#         answer=max(answer,find(i,j))

# print(answer)