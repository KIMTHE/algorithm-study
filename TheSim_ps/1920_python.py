import sys
input = lambda : sys.stdin.readline().rstrip()

def search(i):
    low=0
    high=len(A)-1

    while(low<=high):
        mid=(low+high)//2

        if(A[mid]==B[i]):
            return 1
        elif(A[mid]>B[i]):
            high=mid-1
        else:
            low=mid+1
    return 0


N = int(input())

A=list(map(int,input().split()))

M = int(input())

B=list(map(int,input().split()))

A.sort()


for i in range(M):
    print(search(i))

