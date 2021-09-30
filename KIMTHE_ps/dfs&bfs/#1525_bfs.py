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

puzzle = [ list(map(int,input().split())) for _ in range(3)]
dir = [(0,1),(0,-1),(1,0),(-1,0)]
answer = -1
visit = set()

now = ''
for i in range(3):
    for j in range(3):
        if puzzle[i][j] == 0: puzzle[i][j] = 9
        now += str(puzzle[i][j])

queue = deque()
queue.append((now,0))
visit.add(now)

while queue:
    now,cnt = queue.popleft()

    if now == '123456789' :
        answer = cnt
        break

    now = list(now)
    blank = now.index('9')
    x = blank%3
    y = blank//3

    for dy,dx in dir:
        tmp = now[:]
        ny = y+dy
        nx = x+dx

        if ny < 0 or ny >= 3 or nx < 0 or nx >= 3: continue
        
        i = ny*3+nx
        
        tmp[blank],tmp[i] = tmp[i],tmp[blank]
        tmp = ''.join(tmp)

        if tmp in visit: continue

        queue.append((tmp,cnt+1))
        visit.add(tmp)

print(answer)