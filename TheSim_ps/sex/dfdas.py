def solution(players, power, k):
    answer = 0
    
    #공격력이 높거나 같으면 승리
    # 고의로 패배 가능
    #dp=[] 이전값+k, 이전값+연승값 len(i)
    #dp[i]=max(dp[i-1]+k,dp[i-1]+(i+1))

    dp=[0]*(len(players)+1)
    dp[0]=power
    win=0
    for i in range(len(players)):
        win+=1
        if players[i]<=dp[i]:
            if k*win < (((win)*(win+1))//2): #연승이 패배하는것보다 크면
                dp[i+1]=max(dp[0]+(k*win),dp[0]+(((win)*(win+1))//2)) #전부다 지거나 승리하거나
            
        else: #필패
            dp[i+1]=max(dp[i]+k,dp[i+1])
            win=0
            dp[0]=dp[i+1]
    
    print(dp)

    answer=dp[-1]
    return answer

solution([10, 11, 15, 14, 16, 18, 19, 20],10,2)