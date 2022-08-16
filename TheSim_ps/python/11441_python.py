import sys
input = lambda : sys.stdin.readline().rstrip()

N= int(input())
value=list(map(int,input().split()))
value.insert(0,0)

M=int(input())

for i in range(1,N+1):
    value[i]+=value[i-1]



output=[]
for i in range(M):
    a=list(map(int,input().split()))
    print(value[a[1]]-value[a[0]-1])


