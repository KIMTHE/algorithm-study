import sys, math, heapq,itertools #수학연산, 우선순위큐, 순열&조합
from collections import deque #queue를 구현하는 덱
from copy import deepcopy #깊은복사
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

N = int(input())
L = list(map(int,input().split()))
L.sort()

value = 2*max(max(L),abs(min(L))) #처음 최대값 설정을 잘해야함;
ans = [max(L),max(L)]

def BS(i):
    global value,ans,L

    left = i+1
    right = N-1

    while left <= right:
        mid = (left+right)//2

        if abs(value) > abs(L[mid] + L[i]):
            value = L[mid] + L[i]
            ans = sorted([L[i],L[mid]])

        if L[mid] + L[i] == 0:
            break

        elif L[mid] + L[i] > 0:
            right = mid-1

        elif L[mid] + L[i] < 0:
            left = mid+1


    if value == 0: return
 

for i in range(N):
    BS(i)
    

print(ans[0],ans[1])