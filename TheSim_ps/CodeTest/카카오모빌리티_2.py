def solution(id_list, k):
    answer = 0

    d={}
    for i in id_list:
        value=i.split()
        
        for j in set(value): #하루에 1장이므로 중복 제거를 위한 set
            if j in d: #값이 있으면 이 값에서 +1
                d[j]=d[j]+1
            else: #값이 없으면 새로 만들어서 1설정
                d[j]=1
    
    for key,v in d.items(): #전체 조회
        if v>k: #k를 초과하면 k를 더해준다
            answer+=k
        else: #아니라면 v를 더해준다
            answer+=v

    return answer

a=solution(["A B C D", "A D", "A B D", "B D"],2)
print(a)