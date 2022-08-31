import sys
input = lambda : sys.stdin.readline().rstrip()

N=list(map(int,input().split())) #미로의 크기

mirro = [[0]*(N[1]+1) for i in range(N[0]+1)]

for i in range(1,N[0]+1):
    a=list(map(int,input().split()))
    for j in range(N[1]):
        mirro[i][j+1]=a[j]

for i in range(1,N[0]+1):
    for j in range(1,N[1]+1):
       
       mirro[i][j]=mirro[i][j]+max(mirro[i][j-1],mirro[i-1][j],mirro[i-1][j-1])

print(mirro[N[0]][N[1]])
