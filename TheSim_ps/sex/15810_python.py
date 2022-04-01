import sys
input = lambda : sys.stdin.readline().rstrip()

N,M = map(int,input().split())
staff=list(map(int,input().split()))

end=100000000000
start=0
answer=0
while end>=start:
    mid=(end+start)//2 #시간값

    total=0 #총 갯수
    for i in staff:
        total+=(mid//i)

    if total>=M:
        end=mid-1
        answer=mid
    else: 
        start=mid+1
    
print(answer)
