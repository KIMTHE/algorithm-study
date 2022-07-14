import sys
input = lambda : sys.stdin.readline().rstrip()

M,N=map(int,input().split())

board=[]
for i in range(M):
    board.append(list(input()))

value=100
for i in range(M-7):
    for j in range(N-7): #8*8크키기의 체스판 찾기
        #체스판이 몇번 칠해야하는지
        answer=0
        temp=''
        opposite_answer=0 #반대일경우
        opposite_temp=''

        if board[i][j]=='W': #왼쪽위가 흰색일 경우
            temp='B'
            opposite_temp='W'
        else:
            temp='W'
            opposite_temp='B'

        
        for x in range(i,i+8):
            count=0
            if temp=='W':
                temp='B'
                opposite_temp='B'
            else:
                temp='W'
                opposite_temp='W'
        
            for y in range(j,j+8):
                if (count%2)==0: #짝수일 경우 temp랑 같아야됨
                    if board[x][y]!=temp:
                        answer+=1
                    if board[x][y]==opposite_temp:
                        opposite_answer+=1
                else:
                    if board[x][y]==temp:
                        answer+=1
                    if board[x][y]!=opposite_temp:
                        opposite_answer+=1
                count+=1
        
        value=min(value,answer,opposite_answer)
print(value)