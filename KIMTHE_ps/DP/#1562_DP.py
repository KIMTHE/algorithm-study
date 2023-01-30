import sys, math, heapq,itertools #수학연산, 우선순위큐, 순열&조합
from collections import deque #queue를 구현하는 덱
from copy import deepcopy #깊은복사
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

N = int(input())

# DP[자리수][마지막숫자][비트마스크] = 경우의 수
# 비트마스크는 2진수로 0~9까지 숫자가 사용되었는지 표시 (1111111111) = (9876543210 사용 유무)
DP = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(N+1)]

for i in range(1,10): #초기값, 0으로 시작하는 수는 없는 것 고려
    DP[1][i][2**i] = 1

for i in range(1,N):
    for j in range(10):
        for k in range(1024):
            if j==0: #0으로 끝나면 뒤에 1만 붙여야함
                DP[i+1][1][k|(2**1)] += DP[i][j][k] 
            elif j==9: #9로 끝나면 뒤에 8만 붙여야함
                DP[i+1][8][k|(2**8)] += DP[i][j][k]
            else: #비트 or 연산으로 숫자 포함 
                DP[i+1][j-1][k|(2**(j-1))] += DP[i][j][k]
                DP[i+1][j+1][k|(2**(j+1))] += DP[i][j][k]



answer = 0


for i in range(10):
    answer += DP[N][i][1023]



print(answer%1000000000)