import sys
input = lambda : sys.stdin.readline().rstrip()

def find(answer,count):
    number=[0,1,2,3,4,5,6,7,8,9]

    if count == len(sign)+1: #모든 값을 찾으면
        value.append(''.join(str(_) for _ in answer)) #value 리스트에 정수형을 일렬로 합쳐서 입력
        count-=1 
        answer.pop() #마지막 값 빼고 다음값 찾기
        return

    for i in number: #0~9까지 반복
        if i in answer: # 선택 숫자가 다 달라야 함으로 값이 있으면 다음값 찾기
            continue

        if count==0: #첫번째 값은 바로 입력
            answer.append(i)
            find(answer,count+1) #값을 입력하고 다음값으로 count+1
            continue

        if sign[count-1]=='>': #보다 작다라는 기호이면
            if answer[count-1]>i: #이전값보다 작으면
                answer.append(i) # 올바른 값이므로 값 추가
                find(answer,count+1) # count+1하고 다음값 찾으러

        elif sign[count-1]=='<': #보다 크다라는 기호이면
            if answer[count-1]<i: # 이전값보다 크면
                answer.append(i) #올바른 값으로 추가
                find(answer,count+1) # count+1하고 다음값 찾으러

    if answer: # 0~9까지 해당하는 값이 없고 answer에 값이 있을 경우
        count-=1 #마지막 값을 빼고 다음 값을 찾는다
        answer.pop()
    return

N = int(input())
sign=list(input().split())
answer=[] #값 찾기
count=0 #위치값
value=[] #답을 모음
find(answer,count)
print(max(value)) # 가장 큰값
print(min(value)) # 가장 작은 값
