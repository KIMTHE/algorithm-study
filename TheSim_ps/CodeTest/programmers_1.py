import copy

def sep(temp,new_id):

    new_s="" #문자열 리스트
    new_n="" #숫자 리스트
    if temp!=0:
         new_s=new_id[:temp]
         new_n=new_id[temp:]
    else:
        new_s=new_id[:]

    return new_s,new_n


def solution(registered_list, new_id):
    answer = ''

    temp=0  #문자열 인덱스 구하기
    for i in range(len(new_id)):
        if new_id[i].isdigit():
            temp=i
            break

    while True:
        if new_id not in registered_list: #1번 조건
            answer=new_id
            break
        else: #2번 조건
            new_s,new_n=sep(temp,new_id)
            temp=len(new_s)

            if new_n=="": #값이 없을 경우 0
                num=0
            else:
                num=int("".join(new_n))
            
            num+=1
            new_id = "".join(new_s)+str(num)
        
    return answer

# print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"],"ace15"))
#print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"],"cow"))
print(solution(["bird99", "bird98", "bird101", "gotoxy"],"bird98"))
# print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"],"ace15"))
