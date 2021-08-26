
a="JEROEN"
def solution(name):
    answer = 0
    
    name=list(name)
    
    for i in range(len(name)):
        
        if name[i]<='N':
            answer+=(ord(name[i])-65)
        else:
            answer-=(ord(name[i])-65-26)
            
    visit=[0]*len(name)
    
    for i in range(len(name)):
        if name[i]=='A':
            visit[i]=1
    
    countL=0
    countR=0
    countZ=0
    i=1
    visit[0]=1
    while True:
        if 0 not in visit:
            break

        visit[i]=1
        countR+=1
        i+=1

    visit=[0]*len(name)
    for i in range(len(name)):
        if name[i]=='A':
            visit[i]=1
    i=-1
    visit[0]=1
    while True:
        if 0 not in visit:
            break

        visit[i]=1
        countL+=1
        i-=1


    visit=[0]*len(name)
    for i in range(len(name)):
        if name[i]=='A':
            visit[i]=1
    i=1
    visit[0]=1

    while True:
        if 0 not in visit:
            break
        visit[i]=1
        countZ+=1
        i+=1
        
        if 0 not in visit:
            break
        if name[i]=='A':
            while True:
                if 0 not in visit:
                    break

                visit[i]=1
                countZ+=1
                i-=1
            countZ-=2
            

    answer+=min(countZ,countL,countR)
        
    return answer
        
        
        

print(solution(a))
