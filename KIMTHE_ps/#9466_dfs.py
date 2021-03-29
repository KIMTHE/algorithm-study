import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = int(1e9) #10억 

sys.setrecursionlimit(100000)

def dfs(i,ord):
    team.add(i)
    visit[i] = ord

    if visit[stu[i]] != -1:
        if stu[i] in team :
            return ord-visit[stu[i]]+1
        else : return 0

    return dfs(stu[i],ord+1)

for _ in range(int(input())): 
    n = int(input())
    stu=[0]
    stu += list(map(int,input().split()))
    visit = [-1] * (n+1)

    result = n

    for i in range(1,n+1):
        if visit[i] != -1 : continue

        team = set()
        nt = dfs(i,1)

        result -= nt

    print(result)