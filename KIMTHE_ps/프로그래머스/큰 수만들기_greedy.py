def solution(number, k):
    answer = ''
    stack = []
    
    for num in number:
        if len(stack)==0:
            stack.append(num)
            continue
            
        while k>0 and len(stack)>0 and num>stack[-1]:
            k-=1
            stack.pop()
        
        stack.append(num)
    
    for _ in range(k):
        stack.pop()
    
    for i in stack: answer+=i
    
    return answer