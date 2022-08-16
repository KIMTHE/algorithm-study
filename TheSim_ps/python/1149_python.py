import sys

input = lambda : sys.stdin.readline().rstrip()

N=int(input())

color=[]

for i in range(N):
    a=list(map(int,input().split(' ')))
    color.append([])
    for j in range(len(a)):
        color[i].append(a[j])

for i in range(1,N):
    color[i][0]=min(color[i-1][1],color[i-1][2])+color[i][0]
    color[i][1]=min(color[i-1][0],color[i-1][2])+color[i][1]
    color[i][2]=min(color[i-1][0],color[i-1][1])+color[i][2]

print(min(color[N-1]))