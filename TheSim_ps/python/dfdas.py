def find(value,info,a_point,l_point,result,visit):
    global answer
    global answer_point
    
    if value<=0:
        if a_point<l_point:#라이언이 이겼으면   
            if answer_point<(l_point-a_point):
                answer_point=l_point-a_point
                answer=result[:]
            elif answer_point==(l_point-a_point):
                for k in range(10,-1,-1):
                    if answer[k]!=0 and result[k]!=0:
                        if answer[k]>result[k]:
                            break
                        elif answer[k]<result[k]:
                            answer_point=l_point-a_point
                            answer=result[:]
                    elif answer[k]!=0 and result[k]==0:
                        break
                    elif answer[k]==0 and result[k]!=0:
                        answer_point=l_point-a_point
                        answer=result[:]
            
        return
    
    else:
        for i in range(11):
            if i==10 and value<=info[i] and visit[i]==0:
                visit[i]=1
                result[i]=value
                
                find(0,info,a_point,l_point,result,visit)

                visit[i]=0
                result[i]=0
                

            if value>info[i] and visit[i]==0:
                value-=(info[i]+1)
                result[i]=info[i]+1
                l_point+=(10-i)
                if info[i]!=0:
                    a_point-=(10-i)
                visit[i]=1
                
                find(value,info,a_point,l_point,result,visit)
                
                visit[i]=0
                value+=(info[i]+1)
                result[i]-=info[i]+1
                l_point-=(10-i)
                if info[i]!=0:
                    a_point+=(10-i)

            

def solution(n, info):
    global answer 
    answer = []
    global answer_point
    answer_point =0
    
    a_point_temp=0 #어피치 포인트
    for i in range(11): #어피치 포인트
        if info[i]!=0:
            a_point_temp+=(10-i)
        
    #for i in range(11): #과녁 갯수
        
    result=[0 for _ in range(11)]
    visit=[0 for _ in range(11)]
        
    # l_point=0 #라이언 포인트
    # a_point=a_point_temp 
    find(n,info,a_point_temp,0,result,visit)
    
        
    if len(answer)==0:
        answer=[-1]
        
    
    return answer

#         while True:
#             if i>=11:
#                 break
            
#             if value>info[i]:
#                 value-=(info[i]+1)
#                 result[i]=info[i]+1
#                 l_point+=(10-i)
#                 if info[i]!=0:
#                     a_point-=(10-i)
#             i+=1


print(solution(	10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))