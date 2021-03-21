import sys
input = lambda:sys.stdin.readline().rstrip()

N=int(input())
a=[[0]*2 for i in range(N)]
for i in range(N):
    c,b=list(map(int,input().split()))
    a[i][0]=b
    a[i][1]=c


a.sort()

for i,j in a:
    print(j,i)