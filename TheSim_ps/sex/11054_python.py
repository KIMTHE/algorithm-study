import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
S=list(map(int,input().split()))


value=0
for i in range(len(S)): #가장 큰수로 지정
    answer=0
    dp=[0]*N
    for j in range(i): #i의 앞부분 i보다 작아야됨
        if S[i]>S[j]:
            max_value=0
            for z in range(j):
                if S[z]<S[j] and max_value<dp[z]: #나보다 작은 값중에서 수열을 많이 가지고 있는 값
                    max_value=dp[z]
            dp[j]=max_value+1
    
    answer+=max(dp)

    dp=[0]*N
    for j in range(i,len(S)): #i의 뒷부분 i보다 작아야됨
        if S[i]>S[j]:
            max_value=0
            for z in range(i,j):
                if S[z]>S[j] and max_value<dp[z]: #나보다 큰 값중에서 수열을 많이 가지고 있는 값
                    max_value=dp[z]
            dp[j]=max_value+1
    answer+=max(dp)
    
    value=max(answer,value)
    
print(value+1)