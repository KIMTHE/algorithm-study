import sys  # 입출력의 sys
import math  # 수학연산의 math
import heapq  # 우선순위큐에 사용되는 heapq
import copy  # 깊은복사의 copy
from collections import deque  # queue를 구현하는 덱
from itertools import combinations, product  # 조합,순열
from bisect import bisect_left, bisect_right  # 이진탐색
#sys.setrecursionlimit(100000) # 재귀깊이 설정
def input(): return sys.stdin.readline().rstrip()  # 입력속도빠르게
INF = math.inf

N = int(input())
seq = list(map(int,input().split()))
stack = []
answer = {}

for i,n in enumerate(seq):
    while stack:
        if n > stack[-1][1]:
            j,m = stack.pop()
            answer[j] = n
        else: break

    stack.append((i,n))

while stack:
    j,m = stack.pop()
    answer[j] = -1

for i in range(N): 
    print(answer[i],end=' ')