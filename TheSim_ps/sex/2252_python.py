import sys
input = lambda : sys.stdin.readline().rstrip()

N=list(map(int,input().split()))

tall=[0]*(N[0]+1) 

M=[[0] for i in range(N[0]+1)]

for i in range(N[1]):
    a=list(map(int,input().split()))
    M[a[0]].append(a[1])  
    tall[a[1]]+=1

while True:
    prime=0

    for i in range(len(tall)):
        if tall[i]==0:
            tall[i]=-1
            for j in range(len(M[i])):
                tall[M[i][j]]-=1
            prime=1
            if i!=0:
                print(i,end=' ')
            break
    if prime==0:
        break        
