import sys
input = lambda : sys.stdin.readline().rstrip()

N,M,x,y,K = map(int,input().split())

guide=[]
for _ in range(N):
    value=list(map(int,input().split()))
    guide.append(value)

command=list(map(int,input().split())) #동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4

under=1 #밑에 값
dice=[6,3,4,2,5] #위,오른쪽,왼쪽,뒤,앞
dice_value=[0,0,0,0,0,0,0]
for d in command:
    if d==1: #동
        a=0
        b=1
        u,v0,v1,v2,v3,v4=dice[1],dice[2],dice[0],under,dice[3],dice[4]
    elif d==2: #서
        a=0
        b=-1
        u,v0,v1,v2,v3,v4=dice[2],dice[1],under,dice[0],dice[3],dice[4]
    elif d==3: #북
        a=-1
        u,v0,v1,v2,v3,v4=dice[3],dice[4],dice[1],dice[2],dice[0],under
        b=0
    elif d==4: #남
        a=1
        b=0
        u,v0,v1,v2,v3,v4=dice[4],dice[3],dice[1],dice[2],under,dice[0]
    
    if 0<=x+a<N and 0<=y+b<M: #범위 내일 경우만 계산
        x+=a
        y+=b
        under=u
        dice[0],dice[1],dice[2],dice[3],dice[4]=v0,v1,v2,v3,v4

        if guide[x][y]==0:
            guide[x][y]=dice_value[under]
        else:
            dice_value[under]=guide[x][y]
            guide[x][y]=0

        print(dice_value[dice[0]])
        
