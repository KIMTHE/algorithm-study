import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
num=list(map(int,input().split()))

count=[0]*N #감소 수열 값 저장

for i in range(len(num)):
    for j in range(i):
        if num[i]<num[j]:
            count[i]=max(count[i],count[j]+1)

print(max(count)+1)