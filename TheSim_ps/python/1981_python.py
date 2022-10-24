## 투 포인터

# import sys
# input = lambda : sys.stdin.readline().rstrip()
# from collections import deque

# def bfs(n,start,end):
#     dir=[[1,0],[0,1],[-1,0],[0,-1]]
#     q=deque()
#     q.append([0,0])
#     if start>arr[0][0] or arr[0][0]>end:
#         return False
#     visit=[[0 for _ in range(n)] for _ in range(n)]
#     visit[0][0]=1
#     while q:
#         x,y=q.popleft()

#         for a,b in dir:
#             ax=x+a
#             by=y+b

#             if 0<=ax<n and 0<=by<n and start<=arr[ax][by]<=end and visit[ax][by]==0:
#                 if ax==(n-1) and by==(n-1): #마지막 도달
#                     return True
#                 visit[ax][by]=1
#                 q.append([ax,by])

#     return False


# n=int(input())
# arr=[]
# max_value=-1
# min_value=201
# for _ in range(n):
#     temp=list(map(int,input().split()))
#     max_value=max(max(temp),max_value) #최대값 찾기
#     min_value=min(min(temp),min_value) #최솟값 찾기
#     arr.append(temp)

# start=min_value #최솟값으로 시작
# end=min_value

# answer=1000 #정답 구하기
 
# while start<=max_value and end<=max_value: #둘다 최댓값 안의 값이여야 한다.


#     if bfs(n,start,end): #bfs를 이용해서 start~end까지 범위로 이동할 수 있는 지 확인
#         answer=min(answer,end-start) #이동할 수 있으면 현재 정답과 비교해서 더 작은 값 넣기
#         start+=1 #좀더 작은 값으로 움직일수 있는지 확인

#     else: #움직일 수 없다면 end를 +1
#         end+=1
        
# print(answer)


# 이분 탐색

import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def bfs(n,mid):

    for i in range(min_value,max_value):
        if i+mid>max_value:
            return False
        start=i
        end=i+mid

        dir=[[1,0],[0,1],[-1,0],[0,-1]]
        q=deque()
        q.append([0,0])
        if start>arr[0][0] or arr[0][0]>end:
            continue

        visit=[[0 for _ in range(n)] for _ in range(n)]
        visit[0][0]=1
        while q:
            x,y=q.popleft()

            for a,b in dir:
                ax=x+a
                by=y+b

                if 0<=ax<n and 0<=by<n and start<=arr[ax][by]<=end and visit[ax][by]==0:
                    if ax==(n-1) and by==(n-1): #마지막 도달
                        return True
                    visit[ax][by]=1
                    q.append([ax,by])

    return False


n=int(input())
arr=[]
max_value=-1
min_value=201
for _ in range(n):
    temp=list(map(int,input().split()))
    max_value=max(max(temp),max_value) #최대값 찾기
    min_value=min(min(temp),min_value) #최솟값 찾기
    arr.append(temp)

start=0 #최솟값으로 시작
end=max_value-min_value

answer=1000 #정답 구하기
 
while start<=end:

    mid=(start+end)//2
    print(start,end)
    if bfs(n,mid):
        answer=mid
        end=mid-1
    else:
        start=mid+1

        
print(answer)