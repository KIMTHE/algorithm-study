def solution(G):
    cnt_gem = len(set(G))
    N = len(G)
    interval_gem = {G[0]:1}
    answer = [1,N]
    
    E = 0
    for S in range(N):
        while E < N:
            if len(interval_gem) == cnt_gem:
                if (E-S) < (answer[1]-answer[0]): answer = [S+1,E+1]
                break
                
            E += 1
            if E >= N : break
            interval_gem[G[E]] = interval_gem.get(G[E],0) + 1
            
        if E >= N : break
        interval_gem[G[S]] -= 1
        if interval_gem[G[S]] == 0: del interval_gem[G[S]]
                
    return answer