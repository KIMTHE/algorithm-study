import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
money=list(map(int,input().split()))
total = int(input())

money.sort()
start=1
end=money[-1]

while start<=end:
    mid=(start+end)//2 #상한액

    hap=0 #총액
    for i in money:
        if i<mid: #상한액보다 작으면 안빼고 더함
            hap+=i
            continue
        hap+=mid
    
    if hap>total:
        end=mid-1
    else:
        start=mid+1
    
print(end)
