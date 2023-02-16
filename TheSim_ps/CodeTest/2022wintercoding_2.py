def solution(n, student, point):
    answer = 0
    
    high=[]
    low=[]
    for i in range(1,(n+1)//2+1):
        high.append([i,0])

    for i in range((n+1)//2+1,n+1):
        low.append([i,0])


    for i in range(len(student)):
        for j in high:
            if j[0]==student[i]:
                j[1]+=point[i]
                break
        for j in low:
            if j[0]==student[i]:
                j[1]+=point[i]
                break
        
        high.sort(key=lambda x:(-x[1],x[0]))
        low.sort(key=lambda x:(x[1],x[0]))

        if high[-1][1]<=low[-1][1]:
            
            if high[-1][1]==low[-1][1] and high[-1][0]<low[-1][0]:
                continue
            h=high.pop()
            l=low.pop()
            high.append(l)
            low.append(h)
            answer+=1
            
    return answer

print(solution(20,[3, 2, 10, 2, 8, 3, 9, 6, 1, 2],[3, 2, 2, 5, 4, 1, 2, 1, 3, 3]))