import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque
import heapq

def find(): #백조가 찾아 갈 수 있는지 여부 확인
    global answer

    q=[]
    #heapq.heappush(q,[0,swan[0][0],swan[0][1]])
    q.append([0,swan[0][0],swan[0][1]])
    dir=[[1,0],[-1,0],[0,1],[0,-1]]
    visit=[[0 for _ in range(C)] for _ in range(R)]
    while q:
        value,x,y=q.pop()
        #value,x,y=heapq.heappop(q)

        for a,b in dir:
            xa=x+a
            yb=y+b

            if 0<=xa<R and 0<=yb<C and visit[xa][yb]==0: # and time[xa][yb]<i:
                visit[xa][yb]=1
                if xa==swan[1][0] and yb==swan[1][1]:
                    answer=min(answer,value)
                    print(answer,value)
                    #return value
                v=max(time[xa][yb],value)
                q.append([v,xa,yb])

    

R,C = map(int,input().split())
swan=[]
m=[]

for i in range(R):
    temp=list(input())
    
    m.append(temp)

    for j in range(C):
        if temp[j]=='L':
            swan.append([i,j]) 

#먼저 어름이 최소 몇일만에 녹는지 기록
#그리고 백조가 가장 최소 값으로 길찾기
time=[[1500 for _ in range(C)] for _ in range(R)] #얼이 녹는 시간

water=[]
dir=[[1,0],[-1,0],[0,1],[0,-1]]
for i in range(R): #물은 녹아 있으니 0일 설정
    for j in range(C):
        if m[i][j]=='.':
            time[i][j]=0
            check=False
            for a,b in dir:
                ia=i+a
                jb=j+b
                
                if 0<=ia<R and 0<=jb<C:
                    if m[ia][jb]=='X':
                        check=True
                        break
            if check:
                water.append([i,j])
        if m[i][j]=='L':
            time[i][j]=0
        
#.일때 bfs로 주위 퍼져나가는 시간 계산 

# for i in range(R): #상하좌우로 이동하면서 최소 시간 체크
#     for j in range(C):
for i,j in water: 
    #if m[i][j]=='.':
        #가로 세로만 계산하여 멀어질 수록 +1씩더해서 최소값 저장하기

        #세로
        count=0
        for x in range(i+1,R):
            count+=1
            time[x][j]=min(time[x][j],count)
        
        count=0
        for x in range(i-1,-1,-1):
            count+=1
            time[x][j]=min(time[x][j],count)

        #가로
        count=0
        for y in range(j+1,C):
            count+=1
            time[i][y]=min(time[i][y],count)
        
        count=0
        for y in range(j-1,-1,-1):
            count+=1
            time[i][y]=min(time[i][y],count)





b=0
for i in range(R):
    for j in range(C):
        b=max(b,time[i][j])
global answer
answer=b
find()
print(answer)

# start=1
# end=max(R,C)

# while start<=end:
#     mid=(start+end)//2

#     if find(mid): #더 작은 값 찾기
#         end=mid-1
#     else:
#         start=mid+1


# print(end)

#print(time)





            #상하좌우가 하나씩 q에 넣는 것이 아니라 상하좌우 값을 구하고 대각선 길이로 다이아몬드 형태로 체크
            
#             num=0 #퍼져나가는 시간
            
#             while True:
#                 num+=1
#                 check=False #더이상 값이 넘어가면 종료

#                 down=[dir[0][0]*num+i,j]
#                 down2=[dir[0][0]*num+i,j]
#                 if 0<=down[0]<R and 0<=down[1]<C and m[down[0]][down[1]]=='X':
#                         time[down[0]][down[1]]=min(time[down[0]][down[1]],num)
#                         check=True
#                 up=[dir[1][0]*num+i,j]
#                 if 0<=up[0]<R and 0<=up[1]<C and m[up[0]][up[1]]=='X':
#                         time[up[0]][up[1]]=min(time[up[0]][up[1]],num)
#                         check=True

#                 right=[i,dir[2][0]*num+i]
#                 if 0<=right[0]<R and 0<=right[1]<C and m[right[0]][right[1]]=='X':
#                         time[right[0]][right[1]]=min(time[right[0]][right[1]],num)
#                         check=True

#                 left=[i,dir[3][0]*num+i]
#                 if 0<=left[0]<R and 0<=left[1]<C and m[left[0]][left[1]]=='X':
#                         time[left[0]][left[1]]=min(time[left[0]][left[1]],num)
#                         check=True

#                 #left y=x
#                 #down y=x
#                 #down2 y=-x
#                 #right y=-x

#                 for k in range(1,num):
#                     left[0]-=k
#                     left[1]+=k
#                     if 0<=left[0]<R and 0<=left[1]<C and m[left[0]][left[1]]=='X':
#                         time[left[0]][left[1]]=min(time[left[0]][left[1]],num)
#                         check=True

#                     down[0]-=k
#                     down[1]+=k
#                     if 0<=down[0]<R and 0<=down[1]<C and m[down[0]][down[1]]=='X':
#                         time[down[0]][down[1]]=min(time[down[0]][down[1]],num)
#                         check=True

#                     down2[0]-=k
#                     down2[1]-=k
#                     if 0<=down2[0]<R and 0<=down2[1]<C and m[down2[0]][down2[1]]=='X':
#                         time[down2[0]][down2[1]]=min(time[down2[0]][down2[1]],num)
#                         check=True

#                     right[0]-=k
#                     right[1]-=k
#                     if 0<=right[0]<R and 0<=right[1]<C and m[right[0]][right[1]]=='X':
#                         time[right[0]][right[1]]=min(time[right[0]][right[1]],num)
#                         check=True

#                 if check==False:
#                     break
                    

# print(time)
                    

                

            # while q:
            #     x,y=q.popleft()

                # for a,b in dir:
                #     xa=x+a
                #     yb=y+b

                #     if 0<=xa<R and 0<=yb<C:
                #         if time[xa][yb]>(time[x][y]+1): #얼음이 녹는 시간이 더 빠르면 q에 추가, 느리면 x
                #             time[xa][yb]=(time[x][y]+1)
                #             q.append([xa,yb])


