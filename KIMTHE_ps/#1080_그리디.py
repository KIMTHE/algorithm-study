import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

n,m = map(int,input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]
C = [['0']*m for _ in range(n)]

for i in range(n):
    for j in range(m):
            if A[i][j] != B[i][j] : C[i][j] = '1'

result = 0
oper_row = n-2
oper_col = m-2

if n>=3 and m>=3:
    for i in range(oper_row):
        for j in range(oper_col):

            if C[i][j] == '1':
                result += 1
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if C[r][c] == '1' : C[r][c] = '0'
                        else : C[r][c] = '1'

check = 0

for i in range(n):
    for j in range(m):
        if C[i][j] == '1':
            check = 1
            break
    if check==1: break

if check == 1: print(-1)
else : print(result)