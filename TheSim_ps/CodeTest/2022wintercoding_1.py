def solution(line):
    answer = ''

    value=list(line)
    
    temp=value[0]
    count=0
    answer=''
    for i in range(len(value)):
        if value[i]==temp:
            count+=1
        
        else:
            if count>1:
                answer+=temp
                answer+='*'
            else:
                answer+=temp
                
            temp=value[i]
            count=1

    if count<2:
        answer+=temp
    else:
        answer+=temp
        answer+='*'

    return answer



print(solution("aaaab"))