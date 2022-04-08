import sys
input = lambda : sys.stdin.readline().rstrip()

chess=[]
for i in range(8):
    chess.append(list(input()))

wall=[]
for i in range(8):
    for j in range(8):
        if chess[i][j]=='#':
            wall.append([i,j])

dir=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1],[0,0]] #x,y
q=[[7,0,0]] #y좌표 x좌표, 벽 이동 거리
visit=[[0]*8 for i in range(8)]

ans=0
while q:
    y,x,move=q.pop(0)
   
    if (y==0) or move==9: #제일 위로 가거나 9번 움직이면 벽이 전부 사라짐
        ans=1
        break
    
    for i,j in dir:
        xn=x+i
        yn=y+j
        if 0<=xn<8 and 0<=yn<8:
            for w,z in wall: #벽 값
                if (xn==z and yn==w+move) or (xn==z and yn==(w+move+1)): #이동할 때 벽이 잇으면 break
                    break

            else: #벽을 안만났으면
                if visit[yn][xn]!=2: #다음 값으로 이동하는 것과 이동 후 제자리에 있는 것 까지 계산해서 같은 자리에 2번 있도록
                    visit[yn][xn]+=1
                    q.append([yn,xn,move+1])
            
print(ans)