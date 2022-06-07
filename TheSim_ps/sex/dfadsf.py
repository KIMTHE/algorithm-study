


def solution(balance, transaction, abnormal):
    answer = []

    value=[[0]*(len(balance)+1) for i in range(len(balance)+1)] #B가 A한테 받은 돈
    stack=[[] for i in range(len(balance)+1)]
    
    for A,B,money in transaction:
        #돈을 주면 stack에 저장하고 stack에서 pop한다

        while stack[A]: #A가 B한테 돈을 줌
            user,m=stack[A].pop()
            
            if money<m:
                m-=money
                stack[B].append([user,money])
                stack[A].append([user,m]) #남은 돈 다시 넣기
                money=0
                break
            else:
                money-=m
                stack[B].append([user,m])
                

        
        if money!=0: #자기 돈을 줘야함
            stack[B].append([A,money])
            balance[A-1]-=money

    
    for i in range(1,len(stack)):
        for j in range(len(stack[i])):
            if stack[i][j][0] in abnormal: #이상한 값이면
                stack[i][j][1]=0
    
    
    #최종합
    
    for i in range(len(balance)):
        if i+1 not in abnormal:
            answer.append(balance[i])
        else:
            answer.append(0)

    for i in range(1,len(stack)):
        money=0
        for j in range(len(stack[i])):
            answer[i-1]+=stack[i][j][1]
    
    print(answer)

        # for i in range(len(value[A])-1,-1,-1):
        #     if value[A][i]:
        #         if money<value[A][i]: #money보다 많다면
        #             value[B][i]+=money
        #             value[A][i]-=money
        #             money=0
        #             break
        #         else:
        #             value[B][i]+=value[A][i]
        #             money-=value[A][i]
        #             value[A][i]=0
                    
        # if money!=0: #자기 돈을 줘야함
        #     balance[A-1]-=money
        #     value[B][A]+=money

    # for i in abnormal: #이상한돈 빼기
    #     balance[i-1]=0
    #     for j in value:
    #         j[i]=0
    
    # for i in range(1,len(value)): #최종 합
    #     money=0
    #     money+=balance[i-1]
    #     for j in value[i]:
    #         money+=j
    #     answer.append(money)

    
    return answer


b = [40, 30, 50]
t =[[1, 3, 20], [2, 1, 10], [3, 1, 45], [2, 3, 10], [1, 3, 35], [2, 1, 5], [3, 1, 10], [3, 2, 5]]
a = [2]
solution(b,t,a)