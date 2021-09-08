
def solution(distance, rocks, n):
    answer = -int(1e9)
    rocks.sort()
    
    left,right = 0,distance
    
    while left<=right:
        mid = (left+right)//2 #거리의 최소값이 mid라고 가정
        
        #시뮬레이션
        N = 0
        i = 0
        aStack = []
        a,b = 0,rocks[i]
        
        while True:
            if b-a >= mid: 
                if b == distance: break
                aStack.append(a)
                a = b
                
            else: #돌을 제거할 때
                N += 1
                if b == distance:
                    a = aStack.pop()
                    continue
                    
            i += 1
            if i == len(rocks): b= distance
            else: b = rocks[i]
            
        #n개 이하로 제거했을때 최대값
        if N <= n : 
            left = mid-1
            if mid==answer: break
            answer = max(answer,mid)
        elif N > n : right = mid+1
    
    return answer