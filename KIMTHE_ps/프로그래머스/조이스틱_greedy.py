def solution(name):
    answer1 = 0
    
    M = 'A'*len(name)
    idx = 0
    dir = 1
    
    while True:
        answer1 += min(abs(ord('A')-ord(name[idx])),abs(ord('Z')-ord(name[idx]))+1)
        M = M[0:idx]+name[idx]+M[idx+1:]
        
        if M == name : break
            
        next = idx+dir
        if next==-1 : next = len(name)-1
        if next == len(name): next = 0
            
        if name[next]!=M[next] :
            answer1 += 1
            idx = next
            continue
        
        right_next = idx+1
        left_next = idx-1
        right_step,left_step = 1,1
        if right_next == len(name): right_next = 0
        if left_next == -1: left_next = len(name)-1
            
        while True:
            if name[right_next]!=M[right_next]: break
            
            right_step += 1
            right_next += 1
            if right_next == len(name): right_next = 0
        
        while True:
            if name[left_next]!=M[left_next]: break
            
            left_step += 1
            left_next -= 1
            if left_next == -1: left_next = len(name)-1
        
        if right_step<left_step:
            answer1 += right_step
            dir = 1
            idx = right_next
        else:
            answer1 += left_step
            dir = -1
            idx = left_next
            
        
        
    return answer1