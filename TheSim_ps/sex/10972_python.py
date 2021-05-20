import sys
input = lambda : sys.stdin.readline().rstrip()
from itertools import permutations

N=int(input())
sun=list(map(int,input().split()))



big=0
index=0
for i in range(N): #가장 큰값 찾기
    if sun[i-1]<sun[i]:
        big=max(big,sun[i])
        index=i

swap=0

for i in range(N-1,0,-1):
    if sun[i]>sun[index-1]:
        swap=sun[i]
        sun[i]=sun[index-1]
        sun[index-1]=swap
        break


output=[]
for i in range(index,N):
    output.append(sun[i])

output.sort()

j=index
for i in output:
    
    sun[j]=i
    j+=1

if index==0:
    print(-1)

else:
    for i in range(N):
        print(sun[i],end=' ')