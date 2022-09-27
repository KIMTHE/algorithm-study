from typing import List

def solution(queries: List[List[int]]) -> int:
    answer = 0
    
    a_value=[0 for _ in range(1000)]

    for i in queries:
        a,b=i
        if a_value[a]==0: #처음 값이면
            count=1
            while count<b:
                count*=2
            a_value[a]=[count,b]
        elif a_value[a][0]>a_value[a][1]+b: #현재 크기 > 실제값+들어갈값 보다 작으면 복사 없음
            a_value[a][1]=a_value[a][1]+b
        else: #복사 필요할 경우
            count=a_value[a][0]
            while count<a_value[a][1]+b:
                count*=2
            a_value[a]=[count,a_value[a][1]+b]
            answer+=a_value[a][1]
    if answer==0:
        answer=-1
    return answer

solution([[2,10],[7,1],[2,5],[2,9],[7,32]])