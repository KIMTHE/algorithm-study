import sys, math, heapq,itertools #수학연산, 우선순위큐, 순열&조합
from collections import deque #queue를 구현하는 덱
from copy import deepcopy #깊은복사
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf


A = input()
B = input()

#DP[i][j]:  A[i] 와 B[j]를 포함하는 최대길이의 부분문자열의 길이
DP = [[0 for _ in range(len(B))] for _ in range(len(A))] 

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            if i == 0 or j == 0: DP[i][j] = 1
            else: DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = 0

answer = 0

for l in DP:
    answer = max(answer, max(l))

print(answer)