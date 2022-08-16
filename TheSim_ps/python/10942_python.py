import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
num=list(map(int,(input().split())))
M=int(input())


dp=[[0]*(N) for i in range(N)]


for j in range(N): #끝값
    for i in range(j,-1,-1): #시작값
        if i==j:
            dp[i][j]=1
        
        elif num[i]==num[j]:
            if i==(j-1):
                dp[i][j]=1

            elif dp[i+1][j-1]==1:
                dp[i][j]=1

#print(dp)
for q in range(M):
    S,E=map(int,input().split())
    print(dp[S-1][E-1])
    