import re

def solution(expression):
    answer = 0
    
    value=re.split('([-|+|*])',expression)
        
    dir=[['-','+','*'],['-','*','+'],['+','-','*'],['+','*','-'],['*','+','-'],['*','-','+']]
    
    for i in dir:
        value_temp=value[:]
        
        for j in i:
            count=0 #뺀 숫자
            for k in range(1,len(value_temp)):
                k-=count
                if value_temp[k]==j:
                    temp=eval(value_temp[k-1]+value_temp[k]+value_temp[k+1])
                    temp=str(temp)
                    
                    value_temp[k+1]=temp
                    value_temp.pop(k)
                    value_temp.pop(k-1)
                    
                    count+=2

                 
        answer=max(answer,abs(int(value_temp[0])))
    
    return answer

solution("100-200*300-500+20")