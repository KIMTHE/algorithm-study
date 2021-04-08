import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = int(1e9) #10억 

n,m=  map(int,input().split())
graph = []

for _ in range(n):
    graph.append(input())

visit = [[ [False,False]  for _ in range(m)] for _ in range(n)]

dir = [(0,-1),(0,1),(1,0),(-1,0)]

def check_go(next_row,next_col,broken): 
    global graph,visit,dir,n,m

    if next_row <0 or next_row >=n or next_col <0 or next_col >=m:
        return False
    if visit[next_row][next_col][broken] == True : return False
    return True

def bfs(row,col):
    global graph,visit,dir,n,m

    q = deque()
    q.append((row,col,1,0))
    visit[row][col][0] = True

    while len(q)>0:
        row,col,score,broken = q.popleft()

        if row == n-1 and col == m-1 : return score

        for r,c in dir:
            next_row = row+r
            next_col = col+c

            if check_go(next_row,next_col,broken) == False: continue

            if graph[next_row][next_col] == '1' : #벽을 만났을 때
                next_row += r
                next_col += c

                if broken == 1: continue
                if check_go(next_row,next_col,1) == False: continue
                if graph[next_row][next_col] == '1': continue
             
                visit[next_row][next_col][1] = True
                q.append((next_row,next_col,score+2,1))

            else:
                visit[next_row][next_col][broken] = True
                q.append((next_row,next_col,score+1,broken))
                
    return -1
                
print(bfs(0,0))