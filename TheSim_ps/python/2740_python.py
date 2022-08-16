import sys
input = lambda : sys.stdin.readline().rstrip()

N,M = map(int,(input().split()))
A=[]
for i in range(N):
    A.append(list(map(int,input().split())))

Z,K = map(int,(input().split()))
B=[]
for i in range(Z):
    B.append(list(map(int,input().split())))

for i in range(N):
    for q in range(K):
        temp=0
        for j in range(M):
            temp+=A[i][j]*B[j][q]
        print(temp,end=" ")
    print()