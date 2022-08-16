import sys
input=lambda : sys.stdin.readline().rstrip()

def find(mid): #해당 수의 밑에 몇개가 있는지 확인
    count=0
    for i in range(1,N+1):
        if (mid//i)>N: # 행의 갯수보다 많을순 없으므로 행값을 더한다
            count+=N
        else:
            count+=mid//i
        
    return count

N=int(input())
K=int(input())

start=1
end=K

while start<=end:
    mid=(start+end)//2
        
    if find(mid)<K:
            start=mid+1
    else:
            answer=mid
            end=mid-1
        
print(answer)