import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

work=[[]*N for i in range(N)]
for i in range(N):
    a=list(map(int,input().split()))
    work[i].append(a[0])
    work[i].append(a[1])

value=sorted(work, key=lambda x : (-x[0],-x[1]))

sum=0
a=0 #우선순위


for i in range(N,0,-1):
    big=0
    prime=0
    for j in range(N):
        if i>value[j][0]:
            continue
        if big<value[j][1]:
            prime=1
            big=value[j][1]
            a=j
    if prime==1:        
        sum+=value[a][1]
        value[a][0]=8

print(sum)
                