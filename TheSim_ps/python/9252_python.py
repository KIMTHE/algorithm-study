import sys
input = lambda : sys.stdin.readline().rstrip()

A=list(input())
B=list(input())

dp=[[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)] #dp[i][j]에서 i는 A의 0~i까지 j는 B의 0~j까지의 lcs 길이
for i in range(1,len(A)+1): #dp표채우기
    for j in range(1,len(B)+1):
        if A[i-1]==B[j-1]: #A와 B의 문자가 같다면 1증가
            dp[i][j]=dp[i-1][j-1]+1
        else: #아니라면 이전값 중 큰 값 가져오기
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

i=len(A)
j=len(B)
answer=[] #최종 lcs 수열 찾기
while True:
    if dp[i][j]==0: #dp가0이면 다찾은 것이므로 종료
        break

    if A[i-1]==B[j-1]: # 같은 문자이면 lcs 수열이므로 answer에 저장하고 대각선으로 이동
        answer.append(A[i-1])
        i-=1
        j-=1
    else: #아니라면 왼쪽이나 위 중에서 큰 값으로 이동
        if dp[i-1][j]<dp[i][j-1]:
            j-=1
        else:
            i-=1

print(dp[-1][-1]) #길이 출력

answer.reverse() #뒤에서 부터 구햇으므로 반대로 뒤집어서 출력
for i in answer:
    print(i,end="")
