import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq

N=int(input())

heap=[] #배열

for i in range(N):
    value=int(input())
    if value==0:
        if len(heap)==0:
            print(0)
        else:
            a,b=heapq.heappop(heap)
            print(b)

    elif value!=0:
        heapq.heappush(heap,(abs(value),value))
    