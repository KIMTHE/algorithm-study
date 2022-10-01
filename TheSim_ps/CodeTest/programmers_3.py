import copy
def dfs(k,num,result,visit):
    global answer
    dic={2:[1],3:[7],4:[4],5:[2,3,5],6:[0,6,9],7:[8]}
    value=[2,3,4,5,6,7]  

    if k==0:
        if num not in result: 
            n=copy.deepcopy(num)
            result.append(n)
        return result
    
    if k<2:
        return result

    for i in value:
        k-=i
        if i==6 and len(num)==0 and k!=0: #0이 맨 앞으로 올 경우
            num.append([6,9])
        else:
            num.append(dic[i]) #길이를 넣어서 곱함
        if num not in visit:
            n=copy.deepcopy(num)
            visit.append(n)
            dfs(k,num,result,visit)
        k+=i
        num.pop()
    
    return result

def solution(k):
    global answer
    answer = -1
      
    num=[]
    r=[]
    visit=[]
    result=list(dfs(k,num,r,visit))

    if len(result)==0:
        answer=0
    else:
        answer=0
        for i in range(len(result)):
            n=1
            for j in result[i]:
                n*=len(j)
            answer+=n

    return answer

print(solution(5))