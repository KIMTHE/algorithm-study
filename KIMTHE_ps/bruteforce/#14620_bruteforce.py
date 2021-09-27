import sys  # 입출력의 sys
import math  # 수학연산의 math
import heapq  # 우선순위큐에 사용되는 heapq
import copy  # 깊은복사의 copy
from collections import deque  # queue를 구현하는 덱
from itertools import combinations, product  # 조합,순열
from bisect import bisect_left, bisect_right  # 이진탐색
# sys.setrecursionlimit(10**9) # 재귀깊이 설정
def input(): return sys.stdin.readline().rstrip()  # 입력속도빠르게
INF = math.inf

N = int(input())

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
graph = [list(map(int, input().split())) for _ in range(N)]
price = [[INF]*N for _ in range(N)]
priceL = []

for i in range(N):
    for j in range(N):
        p = graph[i][j]
        for dy, dx in dir:
            ny = i+dy
            nx = j+dx

            if 0 <= ny < N and 0 <= nx < N:
                p += graph[ny][nx]
            else:
                p = INF
                break

        price[i][j] = p
        if p != INF:
            priceL.append((p, i, j))

priceL.sort()

# 꽃이 겹치는지 체크
def check_valid(visit, y, x):
    if visit[y][x] == True: return False

    for dy, dx in dir:
        ny = y+dy
        nx = x+dx
        if nx < 0 or nx >=N or ny < 0 or ny >= N :
            return False
        if visit[ny][nx] == True:
            return False

    return True

# 화단대여 체크
def buy_bed(visit, y, x):
    visit[y][x] = True
    for dy, dx in dir:
        ny = y+dy
        nx = x+dx
        visit[ny][nx] = True

answer = INF

for start1 in range(len(priceL)):
    p1, y1, x1 = priceL[start1]
    visit = [[False]*N for _ in range(N)]
    tmpS = p1
    buy_bed(visit,y1,x1)

    for start2 in range(len(priceL)):
        p2, y2, x2 = priceL[start2]
        if check_valid(visit,y2,x2) == False: continue
        tmpS += p2
        buy_bed(visit,y2,x2)

        for start3 in range(len(priceL)):
            p3, y3, x3 = priceL[start3]
            if check_valid(visit,y3,x3) == False: continue
            tmpS += p3
            answer = min(answer, tmpS)
            tmpS -= p3
            

        visit[y2][x2] = False
        tmpS -= p2
        for dy, dx in dir:
            ny = y2+dy
            nx = x2+dx
            visit[ny][nx] = False
    
print(answer)
