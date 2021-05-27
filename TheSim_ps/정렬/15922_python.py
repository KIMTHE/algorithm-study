import sys
input = lambda : sys.stdin.readline().rstrip()

N= int(input())

line=[[]*N for i in range(N)]
for i in range(N):
    a=list(map(int,input().split()))
    line[i].append(a[0])
    line[i].append(a[1])

sum=0
num=0
for i in range(N):
    if i==N-1:
        sum+=line[i][1]-line[i][0]
        break
    if line[i][1]>=line[i+1][0]:
        if line[i][1]>line[i+1][1]:
            line[i+1][1]=line[i][1]
        line[i+1][0]=line[i][0]

    else:
        sum+=line[i][1]-line[i][0]
        num=0

print(sum)
