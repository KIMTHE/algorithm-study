def solution(money):
    
    DP_first = [0 for _ in range(len(money))] #첫번째 집 무조건 포함
    DP_last = [0 for _ in range(len(money))] #마지막 집 무조건 포함
    
    DP_first[0] = money[0]
    DP_first[1] = max(money[0],money[1])
    
    for i in range(2,len(money)-1):
        DP_first[i] = max(DP_first[i-1],DP_first[i-2]+money[i])
    DP_first[-1] = DP_first[-2]
    
    DP_last[1] = money[1]
    
    for i in range(2,len(money)-2):
        DP_last[i] = max(DP_last[i-1],DP_last[i-2]+money[i])
    DP_last[-1] = DP_last[-3]+money[-1] 
    
    
    return max(DP_first[-1],DP_last[-1])