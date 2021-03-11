import sys
input = lambda : sys.stdin.readline().rstrip()

def find(num):
    l=0
    h=len(LIS)-1
    ret = 1000000

    while l <= h:
        mid = (l+h)//2
        if LIS[mid]>=num:
            if ret > mid:
                ret = mid
            h = mid -1
        else:
            l = mid +1
    return ret


N = int(input())

A=list(map(int,input().split()))
LIS=[A[0]]

for i in range(1,N):
    if LIS[len(LIS)-1] < A[i]:
        LIS.append(A[i])
    else:
        LIS[find(A[i])] = A[i]
print(len(LIS))


 