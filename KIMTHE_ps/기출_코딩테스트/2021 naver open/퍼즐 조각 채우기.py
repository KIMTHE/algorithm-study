import sys, math, heapq,copy,itertools #수학연산, 우선순위큐, 순열조합
from collections import deque #queue를 구현하는 덱
from copy import deepcopy #깊은복사
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

def bfs(G,V,i,j,find):
    N = len(G)
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    
    tmp_b = []
    Q = deque([(i,j)])
    V[i][j] = True
            
    while Q:
        r,c = Q.popleft()
        tmp_b.append((r,c))
                
        for dr,dc in dir:
            nr = r+dr
            nc = c+dc
                    
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            if G[nr][nc] != find or V[nr][nc] == True : continue
                    
            V[nr][nc] = True
            Q.append((nr,nc))
                
    return tmp_b

def convert_zero(B):
    #(0,0) 좌표를 기준으로 하도록 표준화
    dr,dc = B[0]
    for i in range(len(B)):
        r,c = B[i]
        B[i] = (r-dr,c-dc)

    return B

def rotate(P,N):
    #오른쪽으로 회전 4x4 -> (0,1)-(1,3)-(3,2)-(2,0)

    for i in range(len(P)):
        for j in range(len(P[i])):
            r,c = P[i][j]
            P[i][j] = (c,N-1-r)
        P[i].sort()
        
def solution(GB, T):
    N = len(GB)
    
    #game_board에서 빈칸 탐색 후 저장
    visited = [[False for _ in range(N)] for _ in range(N)]
    blank = [] 
    for i in range(N):
        for j in range(N):
            if GB[i][j] != 0 or visited[i][j] == True: continue
            
            blank.append(sorted(bfs(GB,visited,i,j,0)))
   

    #table에서 조각 탐색 후 저장
    visited = [[False for _ in range(N)] for _ in range(N)]
    piece = []
    for i in range(N):
        for j in range(N):
            if T[i][j] != 1 or visited[i][j] == True: continue
                
            piece.append(sorted(bfs(T,visited,i,j,1)))


    #table 전체를 4방향으로 돌리면서 매칭시도
    answer = 0
    for _ in range(4):
        i = 0
        while i < len(piece):
            is_match = False

            p = piece[i]
            for j in range(len(blank)):
                b = blank[j]

                if convert_zero(deepcopy(p)) == convert_zero(deepcopy(b)) : 
                    is_match = True
                    break

            #매칭되면 조각 맞춤
            if is_match:
                answer += len(piece[i])
                del piece[i]
                del blank[j]
            else: i += 1

        rotate(piece,N)

    return answer

print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
[[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))