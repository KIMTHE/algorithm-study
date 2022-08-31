import sys
input = lambda : sys.stdin.readline().rstrip()

N=list(map(int,input().split()))

table=[[0]*(N[0]+1) for i in range(N[0]+1)]

for i in range(1,N[0]+1):
    a=list(map(int,input().split()))
    for j in range(1,N[0]+1):
        table[i][j]=a[j-1]


location=[[0]*4 for i in range(N[1])]

for i in range(N[1]):
    a=list(map(int,input().split()))
    for j in range(4):
        location[i][j]=a[j]


for i in range(1,N[0]+1): #가로줄 더학
    for j in range(1,N[0]):
        table[i][j+1]+=table[i][j]

for i in range(1,N[0]+1): #세로줄 더하기
    for j in range(1,N[0]):
        table[j+1][i]+=table[j][i]

for i in range(N[1]):
    x1=location[i][0]
    x2=location[i][2]
    y1=location[i][1]
    y2=location[i][3]

    print(table[x2][y2]-(table[x2][y1-1]+table[x1-1][y2])+table[x1-1][y1-1])