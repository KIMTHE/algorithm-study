import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq

N=int(input())
left=[] #작은 수 최대 힙
right=[] #큰 수 최소 힙
mid=0 #중앙값

mid=int(input()) #첫번째 값 입력
print(mid) #첫번째 값 중앙값으로 출력

for i in range(1,N): #첫번째 값 제외한 나머지 반복
    x=int(input()) #값 입력

    if len(left)==len(right): #짝수인 경우
        if mid<=x: #중앙값이 입력값보다 작거나 같으면
            heapq.heappush(right,x) #짝수일 경우 더 작은 값을 출력함으로 큰 값은 right에 추가한다
        else: # 중앙값이 입력값보다 크면 입력값을 출력해야 한다.
            if len(left)==0 or x>=left[0][1]: #입력값이 left에서 가장 큰 값보다 크면 입력값을 출력
                heapq.heappush(right,mid) #기존의 중앙값은 right에 추가
                mid=x #입력값을 중앙값으로 설정
            else: # 입력값이 left보다 작으면 left에서 가장 큰 값을 중앙값으로 설정한다
                heapq.heappush(right,mid) # 기존의 중앙값을 먼저 right에 추가
                mid=heapq.heappop(left)[1] #left값중 가장 큰 값을 중앙값으로 설정
                heapq.heappush(left,(-x,x)) #입력값을 left값에 추가

    else: #right가 더 긴 경우, left가 더 긴 경우는 없다 , 홀수인 경우
        if mid<x: # 중앙값이 입력값보다 작으면 입력값이 중앙값을 대신한다
            if len(left)==0 or x>=left[0][1]: # 입력값이 left값중에서 가장 큰값보다 크면
                heapq.heappush(left,(-mid,mid)) # 중앙값을 left에 넣고 
                mid=x #입력값을 중앙값으로 설정
                if mid>right[0]: # 설정한 중앙값인 즉 입력값이 right에서 가장 작은 값보다 크면
                    heapq.heappush(right,mid) #right에서 가장 작은값을 중앙값으로 설정함으로 입력값을 right값에 넣고
                    mid=heapq.heappop(right) # right값을 중앙값으로 설정
            else: # 입력값이 left값보다 작으면 left값을 중앙값으로 해야 함으로
                heapq.heappush(left,(-mid,mid)) #기존의 중앙값을 left로
                heapq.heappush(left,(-x,x)) # 입력값도 left로 넣고
                mid=heapq.heappop(left) #left값을 중앙값으로 설정
        else: # 중앙 값이 입력값보다 크면 중앙값을 그대로 쓸지 확인한다
            if len(left)==0 or mid>=left[0][1]: #중앙값이 left값보다 크면 중앙값을 그대로 쓴다
                heapq.heappush(left,(-x,x)) #입력값을 left로 추가
            else: #중앙값이 left값보다 작으면 left값을 중앙값으로 사용
                heapq.heappush(left,(-x,x)) #입력값과
                heapq.heappush(left,(-mid,mid)) #중앙값을 left에 추가
                mid=heapq.heappop(left) #left값을 중앙값으로 설정
        
    print(mid) #설정된 중앙값을 입력할 때 마다 출력해준다