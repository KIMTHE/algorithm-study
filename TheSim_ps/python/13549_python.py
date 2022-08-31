import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque
import heapq

N,K = map(int,input().split())

#q=deque()
q=[]
#q.append([N,0])
heapq.heappush(q,(0,N))

num_visit=[0]*100001
#time_visit=[0]*100001
while True:
    
    #a=q.popleft()
    a=heapq.heappop(q)
    num=a[1]
    time=a[0]

    if num==K:
        print(time)
        break
    
    if num*2<100001 and num_visit[num*2]==0:
        heapq.heappush(q,(time,num*2))
        #q.append([num*2,time]) 데큐를 사용하면 *2를 appendleft를 사용해서 우선순위를 먼저 둔다
        num_visit[num*2]=1
    if num+1<100001 and num_visit[num+1]==0:
        heapq.heappush(q,(time+1,num+1))
        #q.append([num+1,time+1])
        num_visit[num+1]=1
    if num-1>=0 and num_visit[num-1]==0:
        heapq.heappush(q,(time+1,num-1))
        #q.append([num-1,time+1])
        num_visit[num-1]=1
        

    
    