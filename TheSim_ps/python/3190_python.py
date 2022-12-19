import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N=int(input())
K=int(input())

#m=[[0 for _ in range(N)] for _ in range(N)]

apple=[]
for i in range(K):
    a,b = map(int,input().split())
    #m[a-1][b-1]=1
    apple.append([a-1,b-1])

L = int(input())
dir=[]
for i in range(L):
    a,b = input().split()
    dir.append([int(a),b])

dir.append([20000,L])

time=0 #시간
d=[[1,0],[0,1],[-1,0],[0,-1]] #아래,오른쪽,위,왼쪽
d_type=1 #기본 오른쪽 직진

snack=deque()
snack.append((0,0))#뱀 위치

answer=0
for x,c in dir:

    if answer!=0:
        break

    while True:
            
            if time==x:
                if c=='L': #왼쪽
                    if d_type==0: #아래에서 왼쪽이면 오른쪽
                        d_type=1
                    elif d_type==1: #오른쪽일 경우 위
                        d_type=2
                    elif d_type==2: #위일 경우 왼쪽
                        d_type=3
                    elif d_type==3: #왼쪽일 경우 아래
                        d_type=0
                if c=='D': #오른쪽
                    if d_type==0: #아래일 경우 왼쪽
                        d_type=3
                    elif d_type==1: #오른쪽일 경우 오른쪽이면 아래
                        d_type=0
                    elif d_type==2: #위일 경우 오른쪽
                        d_type=1
                    elif d_type==3: #왼쪼깅ㄹ 경우 위
                        d_type=2
                x_value,y_value=snack[0][0],snack[0][1]
                x_value+=d[d_type][0]
                y_value+=d[d_type][1]

                snack.appendleft((x_value,y_value))

                if x_value>=N or x_value<0 or y_value<0 or y_value>=N or len(snack)!=len(set(snack)):##벽에 부딫혔을 경우, 몸에 부딫혔을 경우
                    answer=time
                    break

                if [x_value,y_value] not in apple: #사과를 먹지 않았으면 꼬리를 줄임
                        snack.pop()
                else:
                    idx=apple.index([x_value,y_value])
                    apple.pop(idx)
                    
                time+=1
                break

            x_value,y_value=snack[0][0],snack[0][1]
            x_value+=d[d_type][0]
            y_value+=d[d_type][1]

            snack.appendleft((x_value,y_value))

            if x_value>=N or x_value<0 or y_value<0 or y_value>=N or len(snack)!=len(set(snack)):#벽에 부딫혔을 경우, 몸에 부딫혔을 경우
                answer=time
                break

            if [x_value,y_value] not in apple: #사과를 먹지 않았으면 꼬리를 줄임 
                    snack.pop()
            else:
                idx=apple.index([x_value,y_value])
                apple.pop(idx)
            #print((snack[0]),((set(snack[0]))))

            time+=1

print(answer+1)