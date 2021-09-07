# 참고 : https://wwlee94.github.io/category/algorithm/bfs-dfs/travel-route/

def solution(tickets):
    airport = {}
    
    #initialize graph
    for a,b in tickets:
        if a not in airport.keys() : airport[a] = []
        if b not in airport.keys() : airport[b] = []
        airport[a].append(b)
    
    for k in airport.keys(): airport[k].sort()
        
    def dfs(now,path):
        if len(tickets)+1 == len(path): return path
        
        for i,d in enumerate(airport[now]):
            airport[now].remove(d)
            
            cp = path[:]
            cp.append(d)
            
            next = dfs(d,cp)
            if next != False: return next #항공권을 모두 사용해서 반환됨
            
            airport[now].insert(i,d) #통과못했으면 다시반환
            
        return False #항공권을 모두 사용하지 못하고 끝남
    
    return dfs("ICN",["ICN"])
