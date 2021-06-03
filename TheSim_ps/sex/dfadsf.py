import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

a=[]

for i in range(N):
    a.append(list(map(int,input().split())))

a=sorted(a,key=lambda x:(abs(x[0]-x[1])))

big=0
for i in range(len(a)-1):
    big=max((abs(a[i][0]-a[i+1][0])+abs(a[i][1]-a[i+1][1])),big)

print(big)    