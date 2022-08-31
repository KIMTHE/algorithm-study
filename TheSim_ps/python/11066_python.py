import sys
input = lambda : sys.stdin.readline().rstrip()

T=int(input())

for _ in range(T):
    K=int(input())
    chapter=list(map(int,input().split()))
    dp=[[0]*(K+1) for _ in range(K+1)]
    
    s=[0]*(K+1)
    for i in range(1,K+1): #1부터 n까지 누적합
        s[i]=s[i-1]+chapter[i-1]
    
    for i in range(2,K+1): #부분 파일의 길이, 몇개를 합쳤는지의 갯수
        for j in range(1,K-i+2): #시작점
            min_value=0 #부분 파일 중에서 최솟값
            for z in range(i-1):
                if min_value==0: #0이라면 들어간 값이없으므로 첫번째 값 넣어줌
                    min_value=dp[j][j+z]+dp[j+z+1][i+j-1]
                min_value=min(dp[j][j+z]+dp[j+z+1][i+j-1],min_value)

            dp[j][j+i-1]=min_value+(s[j+i-1]-s[j-1]) #부분 파일중 최솟값과 시작부터 끝까지의 누적합을 더해준다
    print(dp[1][K]) #최종적으로 누적합값을 출력