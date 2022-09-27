from typing import List

def find(t,p,k): #단어 비교

    i=0 #t인덱스
    j=0 #p인덱스
    count=0
    while i<len(t) and j<len(p):
        if t[i]==p[j]:
            j+=1
            i+=1
            count=0
        elif count==0 and p[j]!='.' and t[i]!=p[j]:
            return False
        else: #같지 않다면
            i+=1
            if count==0: #처음이라면
                j+=1
            count+=1

            if count>k:
                if p[j]=='.':
                    count=0
                    continue
                return False
    return True

def solution(k: int, dic: List[str], chat: str) -> str:
    answer = ''

    chat_value=chat.split()
    
    for i in chat_value:
        if i in dic:
            v='#'*len(i)
            answer+=(v+" ")

        else:
            if '.' in i:
                for j in dic:
                    if find(j,i,k):
                        v='#'*len(i)
                        answer+=v+" "
                        break
                else:
                    answer+=i+" "
            else:
                answer+=i+" "
                
    return answer[:-1]


#print(solution(2,["slang", "badword"],"badword ab.cd bad.ord .word sl.. bad.word"))
print(solution(3,["abcde", "cdefg", "efgij","ttttfg"],".. ab. cdefgh .gi. .z. .tfg"))