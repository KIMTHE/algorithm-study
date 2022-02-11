import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq #힙큐 

N=int(input()) #카드 묶음 갯수 입력
card=[] #카드묶음 카드 수
for i in range(N):
    card.append(int(input()))

heapq.heapify(card) #카드 리스트를 우선순위 큐로 바꿈
hap=0 # 카드의 합
answer=0 #최종 합
if len(card)==1: #카드 묶음이 1개라면 비교할 필요가 없으므로 0출력
    print(0)
else:
 while True:

    if len(card)==2: #카드 묶음이 마지막으로 2개 남으면 2개를 합쳐서 최종값 출력
        answer+=(card[0]+card[1])
        print(answer)
        break

    a=heapq.heappop(card) #카드 묶음중 가장 작은 값을 pop
    b=heapq.heappop(card) #카드 묶음중 그다음으로 작은 값을 pop
    heapq.heappush(card,a+b) #작은값 2개를 합친 다음 카드 묶음에 넣음
    answer+=(a+b) #합친 값을 최종 값에 더해준다

