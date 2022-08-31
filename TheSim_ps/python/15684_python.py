import sys
input = lambda : sys.stdin.readline().rstrip()

def find(x): #사다리 타기 결과 여부
    value=x #사다리 번호 value로 저장
    for i in range(1,H+1):
        if value<N+1 and length[value][i]==1: #[세로줄][가로줄]
            value+=1
        elif value<N+1 and length[value-1][i]==1:
            value-=1
        
    if x==value:
        return True
    else:
        return False

def backtracking(x,y,value): #백트레킹 (세로줄, 가로줄, 사다리 추가한 값)
    global answer

    if value>3: #추가한 사다리가 3이상이면 더이상 확인할 필요가 없음
        return 

    for i in range(1,N+1): #모든 사다리가 올바른지 확인
        if not find(i):
            break
    else: #모든 사다리가 올바른 답이면 answer에 값 추가한 사다리값 저장
        if answer>value:
            answer=value
        return 

    for i in range(x,N):
        for j in range(y,H+1):
            if i<N:
                if length[i][j]==0 and length[i-1][j]==0 and length[i+1][j]==0:
                    length[i][j]=1
                    backtracking(i,1,value+1) #세로줄은 확인한거 그대로 확인하고 가로줄은 처음부터 확인한다
                    length[i][j]=0

    
N,M,H = map(int,input().split())

horizontal=[] #가로줄 위치
length=[[0]*(H+1) for i in range(N+1)] #[세로줄][가로줄]

for i in range(M):
    temp=list(map(int,input().split()))
    horizontal.append(temp)
    length[temp[1]][temp[0]]=1


value=0 #추가한 값
answer=5 #사다리 값
backtracking(1,1,value) #세로줄, 가로줄

if answer>3:
    print(-1)
else:
    print(answer)