from collections import defaultdict
def solution(grid):
    answer = 0
    grid = [list(row) for row in grid]
    N = len(grid)
    M = len(grid[0])
    def check():
        nonlocal grid
        visited = [[True for _ in range(M)] for _ in range(N)]
        cnt = defaultdict(int)
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for x in range(N):
            for y in range(M):
                if visited[x][y]:
                    visited[x][y] = False
                    word = grid[x][y]
                    stack = [(x,y)]
                    while stack:
                        cx,cy = stack.pop()
                        for i in range(4):
                            nx = cx + dx[i]
                            ny = cy + dy[i]
                            if 0<=nx<N and 0<=ny<M:
                                if visited[nx][ny] and grid[nx][ny] == word:
                                    stack.append((nx,ny))
                                    visited[nx][ny] = False
                    cnt[word] += 1
        
        for key in cnt:
            if cnt[key] > 1:
                return False
        return True
    def dfs(point):
        nonlocal grid,answer
        if point == N*M:
            if check():
                print(grid)
                answer += 1
            return
        else:
            x = point//M
            y = point%M
            if grid[x][y] == '?':
                
                for other in ['a','b','c']:
                    grid[x][y] = other
                    dfs(point+1)
                    grid[x][y] = '?'
            else:
                dfs(point+1) 
    dfs(0)
    return answer
print(solution(["??b", "abc", "cc?"]))
