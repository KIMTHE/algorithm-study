import sys
input = lambda : sys.stdin.readline().rstrip()

N,C = map(int,input().split()) # 집 갯수, 공유기 수

house=[]
for i in range(N): #집 위치 입력
    house.append(int(input())) 

house.sort() #집 위치별 정렬

start=0 #처음 거리
end=house[-1] #집 위치중 가장 먼 거리

while start<=end:
    mid=(start+end)//2 #공유기 사이 거리 값

    count=1 #공유기 설치 수, 첫번째 집에 1개가 있다고 가정
    share=0 #공유기 현재 위치
    for i in range(1,N):
        if (house[i]-house[share])>=mid: #공유기 사리 거리 값이 mid보다 작지 않으면 허용
            count+=1 # 공유기 갯수 추가
            share=i # 현재 공유기 위치 추가
    
    if count<C: # 설치한 공유기 갯수가 작으면 사이 거리 값이 너무 큼으로 줄인다
        end=mid-1
    else: # 갯수가 같거나 크면 더 넓혀도 됨으로 +1
        start=mid+1

print(end)

    