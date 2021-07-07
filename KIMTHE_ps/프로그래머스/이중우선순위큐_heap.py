import heapq

def solution(operations):
    answer = [0,0]
    Q = []
    
    for s in operations:
        c = s[0]
        n = int(s[2:])
        if c== 'I' :
            heapq.heappush(Q,n)
        elif c =='D':
            if not Q : continue
            if n == 1:
                Q.sort()
                Q.pop()
            elif n == -1:
                heapq.heappop(Q)
        
    
    Q.sort()
    if Q : 
        answer[0] = Q[-1]
        answer[1] = Q[0]
    return answer
    