import sys
input = lambda : sys.stdin.readline().rstrip()


N=int(input()) #연산 갯수
num=[0] #힙 배열 제일 처음 인덱스 0값에는 0 추가

def insert_sort(x): #값 추가 함수
    num.append(x) # 입력한 값 맨 마지막에 추가

    i=len(num)-1 #인덱스 0값을 제외한 값들 갯수
    while i>1: #루트 값에 도달할때 까지 반복
        if num[i]<num[i//2]: #부모값은 자식값 나누기 2
            num[i],num[i//2]=num[i//2],num[i] # 값 교환
            i=i//2 # 부모값 보다 더 작으므로 부모값이랑 교환
        else:
            break

    
def delete_sort(): # 값 삭제 함수
    num[1],num[-1]=num[-1],num[1] #제일 작은 수와 제일 큰수인 처음과 마지막 값 교환
    print(num[-1]) # 제일 작은 값 출력
    num.pop() # 제일 작은 값 제거

    i=1 #제일 큰값 위치
    while True: # 제일 큰 값을 제일 앞으로 옮겼으니 이를 다시 자식 값과 비교해서 새로 정렬해준다
        value=i 
        left=i*2 # 왼쪽 자식값
        right=(i*2)+1 # 오른쪽 자식값
        if left<len(num) and num[i]>num[left]: #왼쪽에 값이 있고, 왼쪽 자식값이 더 작으면
            i=left # 왼쪽 자식값 입력
        if right<len(num) and num[i]>num[right]: # 오른쪽에 값이 있고, 오른쪽 자식값이 더 작으면
            i=right #오른쪽 자식 값 입력
        
        if i!=value: #자식값과 비교해서 값이 바뀌었으면 루트배열에 값도 교환, 작은 값을 왼쪽으로 
            num[i],num[value]=num[value],num[i]
            
        else: # 자식값과 안바뀌면 종료
            break

for i in range(N): #연산 수 만큼 반복
    x=int(input()) # 값 입력
    
    if x==0:
        if len(num)==1: #힙 배열에 0값만 있으면 추가된 값이 없으므로 0출력
            print(0)
        else:
            delete_sort()

    else:
        insert_sort(x)