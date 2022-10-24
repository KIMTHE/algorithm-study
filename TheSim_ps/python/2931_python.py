import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

R,C = map(int,input().split())

gas=[]
for j in range(R):
    value=list(input())

    for i in range(len(value)):
        if value[i]=='M':
            M_idx=[j,i]
        
        if value[i]=='Z':
            Z_idx=[j,i]

    gas.append(value)

dir=[[[-1,0],[1,0]],[[0,-1],[0,1]],[[-1,0],[1,0],[0,-1],[0,1]],[[1,0],[0,1]],[[-1,0],[0,1]],[[-1,0],[0,-1]],[[1,0],[0,-1]]]
#l,-,+,1,2,3,4

q=deque()

d_value=[[-1,0],[1,0],[0,-1],[0,1]] #M다음 파이프 위치 찾기

for i,j in d_value:
    x=M_idx[0]+i
    y=M_idx[1]+j
    
    if 0<=x<R and 0<=y<C:
        if gas[x][y]!='.':
            x_temp=x
            y_temp=y
            break

q.append([x_temp,y_temp])

visit=[[0 for _ in range(C)] for _ in range(R)]
visit[M_idx[0]][M_idx[1]]=1
visit[x_temp][y_temp]=1
while q:
    x,y=q.popleft()

    pipe_index=[]
    s=gas[x][y] #글자 찾기
    idx=0
    if s=='|':
        idx=0
    elif s=='-':
        idx=1
    elif s=='+':
        idx=2
    elif s=='1':
        idx=3
    elif s=='2':
        idx=4
    elif s=='3':
        idx=5
    elif s=='4':
        idx=6
    else: #'.'일 경우
        idx=-1
    
    for a,b in dir[idx]:
            xa=x+a
            yb=y+b
            if len(pipe_index)>0: #정답을 찾았으면 종료
                break

            if 0<=xa<R and 0<=yb<C and visit[xa][yb]==0:
                if gas[xa][yb]=='.': #해커가 없앤 파이프 인지 확인

                    # 파이프 확인 작업

                    con_pip=[] #연결된 파이프 구하기
                    pM=[]
                    pZ=[]
                    for i,j in d_value: #동서남북
                        if 0<=xa+i<R and 0<=yb+j<C:#해당 파이프가ㅏ 연결됐는지 확인 #gas[xa+i][yb+j]=='.': 
                            s_value=gas[xa+i][yb+j]

                            if s_value=='M': 
                                pM=[i,j] #M과 z생각
                                #con_pip.append([i,j])
                                continue
                            if s_value=='Z':
                                pZ=[i,j] #M과 z생각
                                #con_pip.append([i,j])
                                continue

                            d=0
                            if s_value=='|':
                                    d=0
                            elif s_value=='-':
                                    d=1
                            elif s_value=='+':
                                    d=2
                            elif s_value=='1':
                                    d=3
                            elif s_value=='2':
                                    d=4
                            elif s_value=='3':
                                    d=5
                            elif s_value=='4':
                                    d=6
                            else: #'.'일 경우
                                    d=-1

                            if d==-1:
                                    continue
                            if [-i,-j] in dir[d]:
                                    con_pip.append([i,j])
                            
                        else:
                            continue
                    
                    if con_pip in dir:
                        k=dir.index(con_pip)
                    elif len(pM)>0:
                        con_pip.append(pM)
                        k=dir.index(con_pip)
                        con_pip.pop()
                    elif len(pZ)>0:
                        con_pip.append(pZ)
                        k=dir.index(con_pip)
                        con_pip.pop()
                    elif len(pM)>0 and len(pZ)>0:
                        con_pip.append(pM)
                        con_pip.append(pZ)
                        k=dir.index(con_pip)


                    #else: #.이 아니라면 해당 파이프가 맞음
                    pipe_index=[xa,yb,k] #고장난 파이프의 위치, 어떤 파이프인지 인덱스값
                    break


                else:
                    if gas[xa][yb]!='Z': #Z면 패스
                        q.append([xa,yb])
                        visit[xa][yb]=1
    
    if len(pipe_index)>0: #정답을 찾았으면 종료
        value=""
        if pipe_index[2]==0:
            value='|'
        elif pipe_index[2]==1:
            value='-'
        elif pipe_index[2]==2:
            value='+'
        elif pipe_index[2]==3:
            value='1'
        elif pipe_index[2]==4:
            value='2'
        elif pipe_index[2]==5:
            value='3'
        elif pipe_index[2]==6:
            value='4'

        print(pipe_index[0]+1,pipe_index[1]+1,value)
        break