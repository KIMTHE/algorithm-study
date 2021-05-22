from itertools import permutations

def solution(numbers):
    answer = 0
    case = set()
    C= []
    
    for i in range(1,len(numbers)+1):
        C += list(permutations(numbers,i))

    for i in C:
        tmp = "".join(i)
        case.add(int(tmp))

    for c in case:
        if c==0 or c==1: continue
        check =1
        for i in range(2,int(c**0.5)+1):
            if c%i == 0:
                check = 0
                break
                
        if check==1: answer+=1
    
    return answer