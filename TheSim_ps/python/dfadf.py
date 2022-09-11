import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq

T = int(input())

for _ in range(T):
    n,m,t = map(int,input().split()) #교차로, 도로, 목적지 후보 갯수
    s,g,h = map(int,input().split()) #출발지,

    inf= 1000000000
    road=[[] for _ in range(n+1)] #거리 값
    dest = []

    for _ in range(m):
        a,b,d = map(int,input().split())
        if (a==g and b==h) or (a==h and b==g):
            d-=0.1
        road[a].append([b,d])
        road[b].append([a,d])
    
    for _ in range(t):
        x=int(input())
        dest.append(x)

    distances = [inf] * (n+1)
    visit = [False] * (n+1)

    distances[s] = 0
    q=[]
    heapq.heappush(q,(distances[s],s))

    while q:
        cureent, node = heapq.heappop(q)

        if distances[node]<cureent:
            continue
        
        for i,j in (road[node]): #도착 노드, 도착노드까지 비용
                weighted_dis = cureent + j

                if weighted_dis < distances[i] and node!=i:
                    distances[i]=weighted_dis
                    if (weighted_dis,i) not in q:
                        heapq.heappush(q,(weighted_dis,i))

    dest.sort()
    for i in range(len(distances)):
        if (distances[i]-int(distances[i]))!=0:
            if i in dest:
                print(i,end=" ")
    print()