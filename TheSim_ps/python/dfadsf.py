def dfs(load,M,visit):
        for i in range(len(load)):
            if visit[i]==0 and load[i]<=M:
                visit[i]=1
                M-=load[i]
        return visit

def solution(M, load):
    answer = 0
    load.sort()
    visit=[0]*len(load)
    if load[-1]>M:
        answer=-1
    else:    
        for i in range(len(load)-1,-1,-1):
            if visit[i]==0:
                visit[i]=1

                dfs(load,M-load[i],visit)
                answer+=1
    return answer


print(solution(20, [16, 15, 9, 17, 1, 3]))