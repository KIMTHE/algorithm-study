import sys
input = lambda : sys.stdin.readline().rstrip()

test=int(input()) #테스트 케이스

for _ in range(test): #테스트 케이스 만큼 반복
    N,M = map(int,input().split())

    book=[0]*N #줄수있는 책의 갯수
    student=[]

    for i in range(M): #신청서 작성
        student.append(list(map(int,input().split())))
    
    
    student.sort(key=lambda x:(x[0],x[1])) #오름차순으로 정렬
    
