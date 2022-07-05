import sys
input = lambda : sys.stdin.readline().rstrip()

def find(num): #학생의 인덱스 값
    if visited[num]: #방문했으면 false
        return False
    visited[num]=True #방문 표시

    for n in student[num]: #학생이 빌리고 싶은 책 빌릴 수 있는지 확인
        if book[n]==0 or find(book[n]): #0이라면 빌릴 수 있다 또는 빌린사람이 다른 책빌릴 수 있으면 빌릴 수 있다
            book[n]=num #책을 빌린 학생의 인덱스 표시
            return True #책을 빌렸으니 다른 학생이 책을 빌릴 수 있다는 True 리턴
    return False #책을 빌리지 못할 시 false

test=int(input()) #테스트 케이스

for _ in range(test): #테스트 케이스 만큼 반복
    N,M = map(int,input().split())

    book=[0]*(N+1) #줄수있는 책의 갯수
    student=[[]]

    for i in range(M): #신청서 작성
        a,b=map(int,input().split())
        temp=[]
        for j in range(a,b+1):
            temp.append(j)
        student.append(temp)
    
    for i in range(1,len(student)): #학생 수만큼 반복
        visited=[False]*(M+1) #이전에 방문한 학생을 다시 반복안하기 위한 방문표시
        find(i)
    
    answer=0
    for i in book:
        if i!=0:
            answer+=1
    print(answer)
