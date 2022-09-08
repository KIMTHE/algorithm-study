import sys, math, heapq,copy,itertools #수학연산, 우선순위큐, 순열조합
from collections import deque #queue를 구현하는 덱
from copy import deepcopy #깊은복사
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

def solution(arrows):
    visit = set()
    dir = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    edge = {}
    answer = 0
    
    #edge 이동
    now = (0,0)
    edge['x0y0'] = set()
    visit.add('x0y0')
    
    for arrow in arrows:
        for _ in range(2): #2번씩 이동 - 모래시계 형태 예외처리
            x,y = now
            nx,ny = x+dir[arrow][0], y+dir[arrow][1]
            now_point = 'x'+str(x)+'y'+str(y)
            next_point = 'x'+str(nx)+'y'+str(ny)

            if next_point not in visit:
                edge[next_point] = set()
                visit.add(next_point)

            else: #이미 방문한 정점일 때
                
                #방문하지 않는 간선일 때
                if now_point not in edge[next_point]:
                    answer += 1


            edge[now_point].add(next_point)
            edge[next_point].add(now_point)

            now = (nx,ny)
        
    return answer


