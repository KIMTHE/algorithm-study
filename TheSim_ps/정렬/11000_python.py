import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq

N=int(input())

S=[] #수업 시간
for i in range(N):
    S.append(list(map(int,input().split())))


S=sorted(S,key=lambda S:S[0])
heap=[]
heapq.heappush(heap,S[0][1])

for i in range(1,N):
    if S[i][0]>=heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap,S[i][1])
    else:
        heapq.heappush(heap,S[i][1])

print(len(heap))