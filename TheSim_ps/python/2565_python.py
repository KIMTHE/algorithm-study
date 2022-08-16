import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

elect=[]
for i in range(N):
    elect.append(list(map(int,input().split())))
#전기줄이 겹친다는 것은 범위가 겹친다는 뜻 A,B 둘다 크거나 둘다 작아야 한다

elect.sort(key= lambda x : x[0])

dp=[1]*N
for i in range(N):
    dp[i]=1
    for j in range(i):
        if elect[j][1]<elect[i][1]:
            dp[i]=max(dp[i],dp[j]+1)
print(N-max(dp))
