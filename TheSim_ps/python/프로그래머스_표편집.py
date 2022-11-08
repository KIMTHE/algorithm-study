def solution(n, k, cmd):
    answer = ''
    
    num={i:[i-1,i+1] for i in range(1,n+1)}
    # num=[[]]
    # for i in range(1,n+1):
    #     num.append([i-1,i,i+1])
    
    OX=["O" for i in range(1,n+1)]
    k+=1
    stack=[]
    for value in cmd:
        v=list(value)
        
        if v[0]=="D":
                for _ in range(int("".join(v[2:]))):
                    k=num[k][1]
            
        elif v[0]=="U":
                for _ in range(int("".join(v[2:]))):
                    k=num[k][0]


        
        elif v[0]=="C":
                pre,next=num[k]
                stack.append([pre,k,next])
                #num[k][1]=-1
                OX[k-1]="X"

                if next==n+1: #마지막일 경우
                    k=num[k][0]
                else:
                    k=num[k][1]
        

                if next==n+1:
                    num[pre][1]=next 
                elif pre==0: #첫번째일 경우            
                    num[next][0]=pre     
                else: #일반적인 경우
                    num[pre][1]=next
                    num[next][0]=pre
                    
        elif v[0]=="Z":
                pre,s,next=stack.pop()
                #num[s][1]=s
                OX[s-1]="O"
                if next==n+1: #마지막일 경우
                    num[pre][1]=s
                
                elif pre==0: #첫번째일 경우
                    num[next][0]=s
                
                else: #일반적인 경우
                    num[pre][1]=s
                    num[next][0]=s
        

    return "".join(OX)


    for i in range(n):
        if num[i][1]!=-1:
            answer+="O"
        else:
            answer+="X"
    
    return answer

solution(8,2,["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
#solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])