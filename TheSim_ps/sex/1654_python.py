import sys
input = lambda : sys.stdin.readline().rstrip()

N,M=map(int,input().split())
lan=[]#가지고있는 ㄹ랜선
for i in range(N):
    lan.append(int(input()))

lan.sort()
end=lan[-1]
start=1
count=0
while start<=end:
    mid=(end+start)//2
    count=0 #조건에 맞는 랜선
    for i in lan:
        count+=(i//mid)
    
    if count<M:
        end=mid-1
    else:
        start=mid+1

print(end)