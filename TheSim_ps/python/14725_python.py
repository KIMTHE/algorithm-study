import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
ant=[]

for i in range(N):
    a=list(map(str,input().split()))
    ant.append(a[1:])
print(ant)
ant.sort()
print(ant)
for i in range(N):
    if i==0:
        for j in range(len(ant[i])):
            print("--"*j+ant[i][j])
    else:
        count=-1
        for j in range(len(ant[i])):
            if len(ant[i-1])<=j or ant[i-1][j]!=ant[i][j]:
                break
            else:
                count=j
        for j in range(count+1,len(ant[i])):
            print("--"*j+ant[i][j])