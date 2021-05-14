import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
num=list(map(int,input().split()))
value=[0]*N

result=-1001
for i in range(N):
    value[i]=max(value[i-1]+num[i],num[i])
    result=max(result,value[i])


print(result)
