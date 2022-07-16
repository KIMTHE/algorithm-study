import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

answer=[]

count=665
while len(answer)<N:
    value=list(str(count))

    temp=0 
    for i in value:
        if i=='6':
            temp+=1
        else:
            temp=0
        
        if temp==3:
            answer.append(count)
            break

    count+=1
    
print(answer[N-1])
    