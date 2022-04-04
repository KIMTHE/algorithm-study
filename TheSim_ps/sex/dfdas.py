def solution(grid):
    global answer
    global map
    answer = -1

    
    map=[] #2차원 리스트
    for i in grid:
        map.append(list(i))
    
    traking(0)

    return answer

def traking(N):
    global answer

    for i in map:
        if '?' in i:
            break
    else:
        print(map)
        answer+=1
        return

    alpa=['a','b','c']

    i=N//len(map[0])
    j=N%len(map[0])
    
    if map[i][j]=='?':
            for k in alpa:
                if find(i,j,k): #참값 찾기
                    map[i][j]=k #알파벳 주입
                    
                    traking(N+1)
                    map[i][j]='?'
    
    else:
        traking(N+1)

def find(i,j,k):
    for l in map:
        if k in l:
            break
    else:
        return True
    
    visit=[[0]*len(map) for i in range(len(map[0]))]
    dir=[[-1,0],[1,0],[0,-1],[0,1]]


       
    q=[[i,j]]
    while q:
            x,y=q.pop(0)
            for a,b in dir:
                if x+a<len(map) and x+a>=0 and y+b>=0 and y+b<len(map[0]) and visit[x+a][y+b]==0 and (map[x+a][y+b]==k or map[x+a][y+b]=='?'):
                    visit[x+a][y+b]=1
                    q.append([x+a,y+b])
    
    for a in range(len(map)):
        for b in range(len(map[a])):
            if visit[a][b]==0:
                if map[a][b]==k:
                    return False
    return True

print(solution(["??b", "abc", "cc?"]))