import sys
input = lambda : sys.stdin.readline().rstrip()
import heapq

N=list(map(int,input().split()))

first=[0]*(N[0]+1) #선행해야할 문제수

M=[[0] for i in range(N[0]+1)]
#for i in range(N[0]+1): #문제 입력
#    M[i]=[int(i),int(i)]


for i in range(N[1]): #우선순위 선별 
    a=list(map(int,input().split()))
    M[a[0]].append(a[1])  
    first[a[1]]+=1


while True:
    prime=0

    for i in range(len(first)):
        if first[i]==0:
            first[i]=-1
            for j in range(len(M[i])):
                first[M[i][j]]-=1
            prime=1
            if i!=0:
                print(i,end=' ')
            break
    if prime==0:
        break        
