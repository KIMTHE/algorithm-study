import sys, math, heapq,copy,itertools #수학연산, 우선순위큐, 순열조합
from collections import deque #queue를 구현하는 덱
from copy import deepcopy #깊은복사
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

def solution(rectangle, characterX, characterY, itemX, itemY):
    dir = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
    
    #모든 좌표를 2배 - 탐색할 때를 위해
    graph = [[0 for _ in range(101)] for _ in range(101)] 
    
    #직사각형 테두리,내부를 전부 1로 채워준다
    for ld_x,ld_y,ru_x,ru_y in rectangle: 
        for x in range(ld_x*2,ru_x*2+1):
            for y in range(ld_y*2,ru_y*2+1):
                graph[x][y] = 1
                
    #테두리는 2로 바꾼다
    for x in range(101):
        for y in range(101):
            if graph[x][y] != 1: continue
            if x==0 or x==100 or y==0 or y==100:
                graph[x][y] = 2
                continue
            
            adj = set()
            for dx,dy in dir:
                nx,ny = x+dx,y+dy
                if nx<0 or nx>100 or ny<0 or ny>100: continue
                adj.add(graph[nx][ny])
            if 0 in adj: graph[x][y] = 2
            
    #BFS
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    visit = [[False for _ in range(101)] for _ in range(101)] 
    Q = deque()
    Q.append(((characterX*2, characterY*2),0))
    visit[characterX*2][characterY*2] = True
    answer = []
    
    while Q:
        now,cnt = Q.popleft()
        x,y = now
        
        for dx,dy in dir:
            nx,ny = x+dx,y+dy
            if nx<0 or nx>100 or ny<0 or ny>100: continue
            if graph[nx][ny] != 2 or visit[nx][ny] == True: continue
            
            if nx==itemX*2 and ny==itemY*2:
                answer.append((cnt+1)//2)
                break
            
            visit[nx][ny] = True
            Q.append(((nx,ny),cnt+1))
    
    return min(answer)

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))


