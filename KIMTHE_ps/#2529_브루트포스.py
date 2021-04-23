import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = int(1e9) #10억 

n = int(input())
par = list(input().split())
min_num = [-1]*(n+1)
max_num = [-1]*(n+1)

def min_sol(idx,start,end,visit):
    if idx == n+1: return True

    for i in range(start,end+1):
        if visit[i] == True : continue

        min_num[idx] = i
        visit[i] = True

        if idx<n and par[idx] == '<':
            if min_sol(idx+1,i+1,n,visit) == True: return True

        else:
            if min_sol(idx+1,0,i-1,visit) == True : return True

        visit[i] = False

    return False

def max_sol(idx,start,end,visit):
    if idx == n+1: return True

    for i in range(start,end-1,-1):
        if visit[i] == True : continue

        max_num[idx] = i
        visit[i] = True

        if idx<n and par[idx] == '<':
            if max_sol(idx+1,9,i+1,visit) == True: return True

        else:
            if max_sol(idx+1,i-1,0,visit) == True : return True

        visit[i] = False

    return False

max_sol(0,9,0,[False]*10)
min_sol(0,0,n,[False]*10)

for i in max_num : print(i,end='')
print()
for i in min_num : print(i,end='')