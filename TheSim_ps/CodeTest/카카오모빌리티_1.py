def solution(flowers):
    answer = 0

    flowers.sort(key=lambda x:(x[0],x[1])) #빨리 피고 늦게 지는 순으로 정렬
    
    value=[0]*flowers[-1][1] #제일 마지막에 지는 꽃 일 수 만큼 리스트 생성
    
    for s,e in flowers: 
        for i in range(s,e): #시작일부터 마지막일 까지 꽃이 핀만큼 1
            value[i]=1
    
    for i in value: #값이 1이면 꽃이 핀것이므로 일자에 +1을 해준다
        if i==1:
            answer+=1

    return answer

print(solution([[2, 5], [3, 7], [10, 11]]))