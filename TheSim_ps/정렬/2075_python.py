import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq

N=int(input())

heap=[]

a=list(map(int,input().split()))
for j in range(len(a)):
    heapq.heappush(heap,a[j])

for i in range(N-1):
    a=list(map(int,input().split()))
    for j in range(len(a)):
        heapq.heappush(heap,a[j])
        heapq.heappop(heap)



print(heap[0])