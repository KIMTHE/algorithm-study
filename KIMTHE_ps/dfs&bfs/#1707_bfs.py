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

K = int(input())

for _ in range(K):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    color = [-1]*(V+1)
    
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    
    answer = "YES"

    for i in range(1,V+1):
        if color[i] != -1: continue

        color[i] = 1
        queue = deque([i])

        #BFS
        while queue:
            now = queue.popleft()
            for v in graph[now]:
                if color[now]==color[v]:
                    answer="NO"
                    break

                if color[v]==-1:
                    color[v] = 1-color[now]
                    queue.append(v)

            if answer=="NO": break
        if answer=="NO": break


    print(answer)
