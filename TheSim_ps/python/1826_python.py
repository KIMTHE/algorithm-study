import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

oil=[]
for i in range(N):
    oil.append(list(map(int,input().split())))

L,P=map(int,input().split())

heap=[]
oil.sort(key=lambda x:x[0]) #거리 순으로 정렬
answer=0 #최종답

for distance,amount in oil:
    while P<distance: #다른 마을에 갈 때 기름 양이 부족하다면
        if heap: #이전에 지나친 마을에 기름이 있을 경우
            temp=heapq.heappop(heap)[1] #가장 많은 기름을 더해준다
            P+=temp
            answer+=1 #해당 마을을 들린 것이므로 +1을 해준다
        else: #다른 마을이 없을 경우 기름이 부족하므로 도착하지 못한다
            answer= -1
            break
    if answer==-1: #바로 종료해준다
        break
    #지나간 마을의 기름을 최대 힙큐로 저장
    heapq.heappush(heap,(-amount,amount))

while P<L: #마을을 다 지났는데도 최종 도착지에 도착 못했을 경우 반복해준다
    if heap:  #지나친 마을에서 기름을 더해준다
        temp=heapq.heappop(heap)[1]
        P+=temp
        answer+=1
    else: #다른 마을 에 방문 못하는 것
        answer= -1
        break

print(answer)