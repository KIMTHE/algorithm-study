import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq

N,K=map(int,input().split()) #보석갯수, 가방 갯수
jewel=[] #보석 [무게,가격]
backpack=[] #가방 크기
for i in range(N): #보석 값 입력
    a,b=map(int,input().split())
    jewel.append([a,b])

heapq.heapify(jewel)

for i in range(K): # 가방 값 입력
    backpack.append(int(input()))

backpack.sort() #오름차순으로 가방 정렬

minibag=[] #임시 보관 가방
answer=0 # 최종 답
for bag in backpack:
    
    while jewel and bag>=jewel[0][0]: #보석이 있고, 보석중 가장 무게가 작은 값이 가방보다 작을 때 까지 반복
        a,b=heapq.heappop(jewel) #a는 무게, b는 가격
        heapq.heappush(minibag,(-b,b)) #가격이 큰 순으로 임시 보관 가방에 넣음

    if minibag: #임시 보관 가방에 보석이 있으면
        value=heapq.heappop(minibag) #보석중 가장 큰 값을 꺼내서 해당 가방에 넣어준다
        answer+=value[1] #가방에 넣었으므로 값을 더해준다 

print(answer)





    
