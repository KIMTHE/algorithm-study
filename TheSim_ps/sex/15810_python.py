import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq

N,M = map(int,input().split())
staff=list(map(int,input().split()))

heap=[]
for i in staff:
    heapq.heappush(heap,[i,i]) #개인 시간과, 걸린 시간

time=0
count=0
while True: #힙큐로 해결
    if count==M:
        break
    
    b,a=heapq.heappop(heap)
    count+=1
    time=b
    heapq.heappush(heap,[a+b,a])

    
print(time)


# end=100000000000
# start=0
# answer=0
# while end>=start:
#     mid=(end+start)//2 #시간값

#     total=0 #총 갯수
#     for i in staff:
#         total+=(mid//i)

#     if total>=M:
#         end=mid-1
#         answer=mid
#     else: 
#         start=mid+1
    
# print(answer)
