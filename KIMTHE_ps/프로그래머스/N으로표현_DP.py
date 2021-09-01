def solution(N, number):
    case = [0]
    
    if N==number: return 1
    
    for i in range(1,9):
        tmp = ""
        for _ in range(i): tmp += str(N)
        case.append(set([int(tmp)]))
        
    for i in range(2,9):
        for j in range(1,i):
            
            for a in case[j]:
                for b in case[i-j]:
                    case[i].add(a+b)
                    case[i].add(a-b)
                    case[i].add(a*b)
                    if b!=0: case[i].add(a//b)
                    
        if number in case[i]: return i
    
    return -1