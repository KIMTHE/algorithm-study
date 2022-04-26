import sys
input=lambda : sys.stdin.readline().rstrip()

def find(mid):
    max_value=num[0] #초기값을 제일 처음 수로 초기화
    min_value=num[0]
    cnt=1 #구간 갯수

    for i in range(1,N): #입력한 숫자 부터 하나씩 비교 첫번째 값은 이미 초기화 했으므로 두번째 값부터 시작한다.
        max_value=max(num[i],max_value) #최댓값 구하기
        min_value=min(num[i],min_value) #최솟값 구하기
        #하나의 구간에 최댓값과 최솟값을 구한 뒤 이둘을 뺀 값이 mid값보다 크면 더이상 작아질 수 없으므로 다음 구간으로 넘어간다. 
        if mid<(max_value-min_value):
            cnt+=1 #다음 구간으로 넘아간다는 의미로 1더해준다
            max_value=num[i] #다음 구간으로 넘어감으로 최댓값과 최솟값을 i번째 값으로 새로 초기화 해준다
            min_value=num[i]
    return cnt #최종적으로 구간 갯수를 리턴해준다.
    
N,M=map(int,input().split())
num=list(map(int,input().split()))

start=0 #배열에 들어 있는 수의 값 범위 최소 1~10,000이므로 0과 10,000을 start,end값으로 설정
end=10000
#먼저 최솟값을 설정한뒤 구간별로 나눠질수 있는지 확인한 후 가능하면 값을 더 낮춰서 확인
while start<=end: #이분탐색
    
    mid=(start+end)//2

    if find(mid)<=M: 
 #find(mid)로 구간을 나눌 수 있는 확인한 후 나누어진 구간이 최대 구간인 M값보다 작으면 더 작은 최솟값을 찾는다 
        end=mid-1 
        result=mid #결과값 저장
    else:
        start=mid+1
        
print(result)
        