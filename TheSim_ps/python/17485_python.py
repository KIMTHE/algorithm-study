import sys
input = lambda : sys.stdin.readline().rstrip()

N,M = map(int,input().split())

num=[]
for i in range(N):
    num.append(list(map(int,input().split())))

answer=[[[0]*M for i in range(N)] for i in range(3)] #우주선 이동 경비 합계 3차원 리스트로 나타냄
# 제일 앞에는 이전에 왼쪽,가운데,오른쪽 중에 어디서 받아왔는지 체크, 0이면 가운데, 1이면 왼쪽, 2면 오른쪽에서 받아온 것
# 0으로 받았으면 다음 값은 1,2중에서 하나로 받아야 된다
# 두번째는 세로 세번째는 가로
for i in range(N): #세로
    for j in range(M): #가로
        
        if j==0: #가장 왼쪽
            answer[0][i][j]=answer[2][i-1][j]+num[i][j] #가운데서 오는 값, 현재값 + 이전에 가운데값
            answer[2][i][j]=min(answer[0][i-1][j+1],answer[1][i-1][j+1])+num[i][j] #오른쪽에서 오는 값, 이전 오른쪽값중 가운데받은값과 왼쪽받은값중 작은값
            answer[1][i][j]=max(answer[2][i][j],answer[0][i][j]) #가장 왼쪽이므로 왼쪽으로는 올수 없으므로 큰 아무값이나 넣어준다

        elif j==(M-1): #가장 오른쪽
            answer[0][i][j]=answer[1][i-1][j]+num[i][j] #가운데에서 왼쪽으로 받은값 + 현재값
            answer[1][i][j]=min(answer[0][i-1][j-1],answer[2][i-1][j-1])+num[i][j] #왼쪽에서 오는 값중에서 가운데받은값과 오른쪽에서 받은값중 작은값 + 현재값
            answer[2][i][j]=max(answer[1][i][j],answer[0][i][j]) #가장 오른쪽이므로 오른쪽에는 올수 없으므로 아무값이나 넣어줌
        else:
            answer[0][i][j]=min(answer[1][i-1][j],answer[2][i-1][j])+num[i][j] #가운데에서 오는 값중 이전에 왼쪽과 오른쪽중 작은 값 + 현재값
            answer[1][i][j]=min(answer[0][i-1][j-1],answer[2][i-1][j-1])+num[i][j] # 왼쪽에서 오는 값중 이전에 가운데와 오른쪽
            answer[2][i][j]=min(answer[0][i-1][j+1],answer[1][i-1][j+1])+num[i][j] #오른쪽에서 오는 값중 이전에 가운데와 왼쪽

value=10000000 #최대값
for i in range(3): #가운데,왼쪽,오른쪽 중에서 가장 작은 값을 찾는다
    if value>min(answer[i][N-1]): # 각 방향별로 오는 값중 가장 작은 값
        value=min(answer[i][N-1])
print(value)
