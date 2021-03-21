import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

V, E = input().split()
V=int(V)
E=int(E)

K = int(input())

line = [[] for _ in range(V+1)]

for i in range(E):
    a,b,c=map(int,input().split())
    line[a].append([c,b])

result=[3000000 for _ in range(V+1)]
result[K]=0


q=[]
heapq.heappush(q,[0,K])

while q:
    dis,end=heapq.heappop(q)
    for d,x in line[end]:
        d+=dis
        if d<result[x]:
            result[x]=d
            heapq.heappush(q,[d,x])

for i in range(1,V+1):
    print(result[i] if result[i]!=3000000 else "INF")
