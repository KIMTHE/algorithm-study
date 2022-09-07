import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

num=[]
for i in range(N):
    num.append(list(map(int,input().split())))

if N==1: #N이 1일 경우 연산의 수가 없으므로 0 출력
    print(0)
else:
    value=[[0]*N for i in range(N)] # x에서부터 y까지의 연산 수 2차원리스트로 저장

    for i in range(N-1): # 1칸 차이나는 값은 미리 연산
        value[i][i+1]=num[i][0]*num[i][1]*num[i+1][1]
        
    for i in range(N):
        x=0 #대각선을 구하기 위해 세로값을 새로 정의
        for j in range(i+2,N): #자기 자신과 바로 옆칸은 이미 정의되어 있음
            value[x][j]=2**32 #최솟값을 구하기 위해 최댓값 초기화
            for k in range(x,j): #x부터 j까지의 연산 수 구하기
                #x와j의 기준인 k 값을 옮기며 최소값 찾기
                #x부터 k까지의 총 연산 수 + k+1부터 j까지의 총 연산수 + 이 둘을 곱하는 연산 수
                value[x][j]=min(value[x][j],value[x][k]+value[k+1][j]+(num[x][0]*num[k][1]*num[j][1]))
            x+=1 #대각선 연산을 위해 아래로 한칸
    print(value[0][-1])