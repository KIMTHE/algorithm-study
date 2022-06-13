import sys
input = lambda : sys.stdin.readline().rstrip()

N,M=map(int,input().split())

board=[]

for i in range(N):
    temp=input()
    board.append(list(temp))

dir=[[1,0],[-1,0],[0,1],[0,-1]]

Red=[]
Blue=[]
for i in range(N):
    for j in range(M):
        if board[i][j]=="R":
            Red.append(i)
            Red.append(j)
        if board[i][j]=="B":
            Blue.append(i)
            Blue.append(j)

q=[[Red[0],Red[1],Blue[0],Blue[1]]] #빨간공 파란공 순으로 
c=[1] #횟수
visit=[[Red[0],Red[1],Blue[0],Blue[1]]]
answer=11 #최종 답

while q: #q에 좌표값 들어가잇음
    if answer!=11:
        break

    red_x,red_y,blue_x,blue_y=q.pop(0)
    count=c.pop(0)

    for a,b in dir:
        rx,ry,bx,by=red_x,red_y,blue_x,blue_y
        while True:
            rx+=a
            ry+=b
            
            if board[rx][ry]=='#':
                rx-=a
                ry-=b
                break
            if board[rx][ry]=='O':
                break
        while True:
            bx+=a
            by+=b
            if board[bx][by]=='#':
                bx-=a
                by-=b
                break
            if board[bx][by]=='O':
                break

        if board[rx][ry]=='O' and board[bx][by]!='O':
            answer=count
            break

        if board[bx][by]=='O':
                continue

        if rx==bx and ry==by: #같은 곳에 있으면 겹치므로 값이 큰쪽이 뒤로
            if (a>0 or b>0): #아래로 가거나 오른쪽으로가면
                if (red_x>blue_x or red_y>blue_y): #red가 더 아래쪽에 있거나 오른쪽에 있으면
                    bx-=a
                    by-=b
                else:
                    rx-=a
                    ry-=b
            else:
                if (red_x<blue_x or red_y<blue_y): #red가 더 위나 왼쪽에 있으면   
                    
                    bx-=a
                    by-=b
                else:
                    rx-=a
                    ry-=b
                    
        if [rx,ry,bx,by] not in visit and count<11:
            q.append([rx,ry,bx,by])
            visit.append([rx,ry,bx,by])
            c.append(count+1)
    

if answer!=11:
    print(answer)
else:
    print(-1)