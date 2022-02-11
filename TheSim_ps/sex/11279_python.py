import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input()) # 연산 개수 입력
num=[0] # 힙 배열 0번째 인덱스에 0값 입력

def insert(x): # 값 추가시 실행 함수
    num.append(x) #힙 배열에 마지막에 값 추가
    i=len(num)-1 # 인덱스 0값을 제외한 값, 즉 제일 마지막 값
    
    while i>1: #제일 처음 값인 1이 될때 까지 반복, 루트 값이 될때 까지
        if num[i]>num[i//2]: #부모 인덱스는 자식인덱스 나누기 2, 부모 인덱스가 더 작으면
            num[i],num[i//2]=num[i//2],num[i] # 부모 인덱스와 값 교환
            i=i//2 
        else: #교환할 값이 없으면 종료
            break

def delete(): # 삭제 함수
    print(num[1]) #루트 값인 제일 큰 값 출력

    num[1],num[-1]=num[-1],num[1] #제일 큰값과 제일 작은값, 처음과 마지막 값 교환
    num.pop() #제일 큰값이 마지막값 삭제

    i=1 #제일 앞에있는 작은 값 위치
    while True: # 앞에 있는 작은 값을 자식들과 비교하여 새로 정렬
        left=i*2 #왼쪽 자식값
        right=i*2+1 #오른쪽 자식값
        value=i #현재 작은 값의 위치

        if left<len(num) and num[i]<num[left]: #왼쪽에 자식값이 있고, 자식값보다 작으면 실행
            i=left #왼쪽 자식 인덱스 값을 받음
        if right<len(num) and num[i]<num[right]: # 오른쪽에 자식이 있고, 오른쪽 자식값 보다 작으며 실행
            i=right # 오른쪽 자식 인덱스 값을 받음
        
        if value!=i: # 왼쪽이나 오른쪽 자식값을 받았으면 바뀐 값에 해당하는 값과 교환
            num[value],num[i]=num[i],num[value]

        else: #바꿀 값이 없으면 종료
            break
        
for i in range(N):
    x=int(input())

    if x==0:
        if len(num)==1:
            print(0)
        else:
            delete()
    else:
        insert(x)