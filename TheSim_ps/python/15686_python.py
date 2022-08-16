import sys
input = lambda : sys.stdin.readline().rstrip()
import itertools

N,M= map(int,input().split())
road = []
for i in range(N):
    road.append(list(map(int,input().split())))

house=[]
chicken=[]

for i in range(N):
    for j in range(N):
        if road[i][j]==1:
            house.append([i,j])
        if road[i][j]==2:
            chicken.append([i,j])

a=[]
for team in list(itertools.combinations(chicken, M)):
    a.append(team)

answer=10000
for j in a: #선택한 치킨집 순서대로
    num=[10000]*len(house) # 집마다 치킨집 거리
    for i in range(len(house)): #집 순서대로
        

        for k in range(len(j)): #M개만큼 고른 치킨 만큼반복
            num[i]=min(num[i],abs(j[k][0]-house[i][0])+abs(j[k][1]-house[i][1]))

    answer=min(sum(num),answer)

print(answer)