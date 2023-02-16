import sys
input = lambda : sys.stdin.readline().rstrip()

def find(i,j):

    if dp[i][j]!=-1:
        return dp[i][j]

    dp[i][j]=find(i-2,j-1)%inf+find(i-1,j)%inf
    print(dp)
    return dp[i][j]%inf

N=int(input())
K=int(input())
inf=1000000003
if N//2<K:
    print(0)
else:
    dp=[[-1 for _ in range(K+1)] for _ in range(N+1)]
    #dp[i][j]는 i개의 색중 j개 선택하는 경우
    #dp[i][j]는 i번째를 선택할 경우 i-1을 선택못하므로 dp[i-2][j-1] + i를 선택 안한 경우인 dp[i-1][j]와 같다.

    for i in range(1,N+1):
        dp[i][1]=i
    
        for k in range(2,K+1):
            if i//2<k:
                dp[i][k]=0

    print(find(N,K))

    

