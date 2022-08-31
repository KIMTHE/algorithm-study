import imp
import sys
input = lambda : sys.stdin.readline().rstrip()
from itertools import combinations

N,M = map(int,input().split()) #자장면 수, 웍 갯수
S=list(map(int,input().split())) #웍 크기 종류

answer=0 #답

A=[]
for a,b in combinations(S,2): #최대 2개까지 웍 사용가능 2개 합친 모든 웍의 경우의 수
    A.append(a+b)
for i in S: #1개만 사용할 경우 경우의 수
    A.append(i)

A.sort(reverse=True) #내림차순으로 정렬

dp=[10001]*(N+1) #짜장면 그릇 갯수에 따라 최소의 경우수 구하기
dp[0]=0 #0그릇은 0

for i in range(1,N+1):
    for j in range(len(A)): #웍의 조합 갯수만큼 비교
        if (i-(A[j]))<0: #짜장면 현재 그릇 - 웍으로 조합 가능한 짜장면갯수 
            continue
        dp[i]=min(dp[i],dp[i-A[j]]+1) #현재값과 이전값 비교해서 더 작은 값을 추가

if dp[-1]==10001: #주문한 짜장면의 값이 나올 수 없는 경우의 수인 경우
    print(-1)
else:
    print(dp[-1])
