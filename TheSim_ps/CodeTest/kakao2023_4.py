def solution(numbers):
    answer = []

    for i in numbers:
        bnum=format(i,'b')
        
        n=1
        while 1:
            if len(bnum)<=n:
                break
            n=1+(n*2) 
        
        while len(bnum)!=n: #앞에 0을 채워줌
            bnum='0'+bnum

        check=0
        for i in range(0,n,2):
            if bnum[i]!='0':
                check=1
                break
        if check==1:
            for i in range(1,n,2):
                if bnum[i]!='1':
                        answer.append(0)
                        break
            else:
                answer.append(1)
        else:
            answer.append(0)

    return answer


#print(solution([2]))
solution([63,111,95])