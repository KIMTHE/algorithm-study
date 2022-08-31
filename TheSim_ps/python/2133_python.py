import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

dp=[0]*(N+1) 
dp[0]=1 #dp[0]은 1

for i in range(2,N+1,2): #홀수는 채우지못해 0이므로 짝수만 본다.
    value=0 #2가지의 경우 값 저장
    for j in range(4,i+1,2): #타일은 4번째 부터 새로운 타일의 경우의 수 2개가 나온다.
        value+=dp[i-j]*2 # 그래서 dp[i-4]에서 2가지 경우의 수 *2, dp[i-6]에서 *2를 해서 dp[0]까지 *2를 한다
    dp[i]=dp[i-2]*3+value # 기존에 3*2 틀에서 기본 틀 3가지의 경우의 수를 곱한 값 + 새로 생긴 모양 수

print(dp[-1]) #최종 값 출력

        