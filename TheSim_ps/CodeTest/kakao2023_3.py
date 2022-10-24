#from itertools import product
import itertools

def solution(users, emoticons):
    answer = []

    sale=[ i for i in range(1,41)]  
    
    value=list(itertools.product(emoticons,sale))

    temp=[[] for _ in range(len(emoticons))]

    j=-1
    for i in range(len(emoticons)*40):
        if i%40==0:
            j+=1
        #print(value[i])
        temp[j].append([value[i][0],value[i][1]])

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            p=temp[i][j][0] #가격
            s=temp[i][j][1] #할인율
    

    return answer

solution([[40, 10000], [25, 10000]],[7000, 9000])