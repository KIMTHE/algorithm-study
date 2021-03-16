import sys, math, heapq 
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = int(1e9) #10억 

V, E = map(int,input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
q = []
distance = [INF] * (V+1)

#간선 정보 입력
for _ in range(E):
    i,j,k = map(int,input().split())
    graph[i].append((j,k))

# heap을 이용한 다익스트라 알고리즘
heapq.heappush(q,(0,start))
distance[start] = 0

while len(q)>0:
    now_dist, now_v = heapq.heappop(q)

    if distance[now_v] < now_dist :
        continue

    for e in graph[now_v]:
        tmp_dist = now_dist+e[1]

        if distance[e[0]] > tmp_dist :
            heapq.heappush(q,(tmp_dist,e[0]))
            distance[e[0]] = tmp_dist 

#출력
for i in range(1,V+1):
    if distance[i] == INF : print('INF')

    else : print(distance[i])