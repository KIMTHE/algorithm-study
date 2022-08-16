import sys
input = lambda : sys.stdin.readline().rstrip()

N,M = map(int,input().split()) #방학 총날짜, 갈 수 없는날 수
noday=list(map(int,input().split())) #갈 수 없는 날

# 첫날부터 최소값 구하기

dp=[[10000*N]*42 for i in range(N+6)] #쿠폰 갯수 n이 100이 최대이므로 최대 42개 까지

dp[0][0]=0 #첫날 하루전은 0
for i in range(N+1): # 0은 초기값이므로,1부터 N값까지 확인
    for j in range(40): #쿠폰은 40개까지 확인
        if dp[i][j]==(10000*N): #값이 최댓값인 경우는 확인안함
            continue
        
        if (i+1) in noday: #안가는 날
            dp[i+1][j]=min(dp[i+1][j],dp[i][j]) #다음날이 안가는 날이면 당일과 그다음날중 최솟값 

        if j>=3: #쿠폰이 3개 이상이므로 1일차일때 쿠폰 사용
            dp[i+1][j-3]=min(dp[i+1][j-3],dp[i][j])#쿠폰사용  

        dp[i+1][j]=min(dp[i+1][j],dp[i][j]+10000) #1일차, 다음날 1일차 이용한 경우
        
        
        for k in range(1,4): #3일차 사용하는 경우, 해당 날부터 3일까지 값 구하기
                dp[i+k][j+1]=min(dp[i+k][j+1],dp[i][j]+25000)
        
        for k in range(1,6): #5일차 사용하는 경우, 해당 날부터 5일까지 값 구하기
                dp[i+k][j+2]=min(dp[i+k][j+2],dp[i][j]+37000)

print(min(dp[N])) #N일차 중에서 쿠폰 사용 여부에 따라 값이 달라짐으로 최소값 출력