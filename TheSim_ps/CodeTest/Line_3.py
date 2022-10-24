from typing import List
import copy

def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    answer = [[0 for _ in range(n)] for _ in range(n)]

    fire_dir=[[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]] #불은 상하좌우대각선 이동
    ice_dir=[[1,0],[0,1],[-1,0],[0,-1]] #얼음은 상하좌우 이동

    fire_visit=[[0 for _ in range(n)] for _ in range(n)] #방문 표시
    ice_visit=[[0 for _ in range(n)] for _ in range(n)] #방문 표시
    
    # for a,b in fires: 
    #     fire_visit[a-1][b-1]=1
    # for a,b in ices:
    #     ice_visit[a-1][b-1]=1

    f=[]
    for i,j in fires:
            f.append([i-1,j-1])
    fires=f[:]
    ic=[]
    for i,j in ices:
            ic.append([i-1,j-1])
    ices=ic[:]
    
    
    for i in range(len(fires)):
        f=[]
        f.append([fires[i][0],fires[i][1]])
        f_visit=copy.deepcopy(fire_visit)
        for _ in range(1,m+1): 
            fire=f[:]
            for x,y in fire:
                answer[x][y]+=1
                f_visit[x][y]=1
                for a,b in fire_dir:
                    ax=a+x
                    by=b+y
                    if 0<=ax<n and 0<=by<n and f_visit[ax][by]==0:
                        f_visit[ax][by]=1
                        f.append([ax,by])
                        answer[ax][by]+=1
        
    
    for i in range(len(ices)):
        ic=[]
        ic.append([ices[i][0],ices[i][1]])
        i_visit=copy.deepcopy(ice_visit)
        for _ in range(1,m+1): 
            ice=ic[:]
            for x,y in ice:
                answer[x][y]-=1
                i_visit[x][y]=1
                for a,b in ice_dir:
                    ax=a+x
                    by=b+y
                    if 0<=ax<n and 0<=by<n and i_visit[ax][by]==0:
                        i_visit[ax][by]=1
                        ic.append([ax,by])
                        answer[ax][by]-=1


    return answer

print(solution(5, 3, [[5, 5], [1, 3], [5, 2]], [[1, 5], [3, 2]]))