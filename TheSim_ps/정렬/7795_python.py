import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

for i in range(N):
    N=list(map(int,input().split()))
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    
    A.sort()
    B.sort()
    count=0

    for j in range(len(A)):
        for k in range(len(B)):
            if A[j]<=B[k]:
                break
            if A[j]>B[k]:
                count+=1

    print(count)