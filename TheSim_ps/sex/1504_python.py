import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq

def dijkstra(start):
    q=[]

    heapq.heappush(q,(0,start))
    visit=[INF]*(N+1)
    visit[start]=0

    while q:
        dist,now=heapq.heappop(q)

        if visit[now]<dist:
            continue
        for i in road[now]:
            if dist+i[1]<visit[i[0]]:
                visit[i[0]]=dist+i[1]
                heapq.heappush(q,(dist+i[1],i[0]))
    return visit
    
INF=sys.maxsize

N,E = map(int,input().split())
road=[[]for _ in range(N+1)]

for i in range(E):
    a,b,c=(map(int,input().split()))
    road[a].append([b,c])
    road[b].append([a,c])

v1,v2=map(int,input().split())

visit=dijkstra(1)
v1_visit=dijkstra(v1)
v2_visit=dijkstra(v2)
A=visit[v1]+v1_visit[v2]+v2_visit[N]
B=visit[v2]+v2_visit[v1]+v1_visit[N]

answer=min(A,B)
if answer>=INF:
    print(-1)
else:
    print(answer)



# 플로이드 위샬 방법, 값이 커서 시간초과가 남
# INF=sys.maxsize
# N,E = map(int,input().split())
# road=[[INF]*(N+1) for i in range(N+1)]
# for i in range(1,N+1):
#     road[i][i]=0

# for i in range(E):
#     a,b,c=(map(int,input().split()))
#     road[a][b]=c
#     road[b][a]=c

# for k in range(1,N+1):
#     for i in range(1,N+1):
#         for j in range(1,N+1):
#             if i==j:
#                 continue
#             road[i][j]=min(road[i][j],road[i][k]+road[k][j])


# v1,v2=map(int,input().split())

# A=road[1][v1]+road[v1][v2]+road[v2][N]
# B=road[1][v2]+road[v2][v1]+road[v1][N]

# answer=min(A,B)
# if answer>=INF:
#     print(-1)
# else:
#     print(answer)