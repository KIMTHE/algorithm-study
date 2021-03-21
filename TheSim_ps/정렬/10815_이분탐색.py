import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
a=list(map(int,input().split()))
M=int(input())
b=list(map(int,input().split()))

a.sort()

check=[]

def search(i): #이진탐색 기법으로 해결
    high=len(a)-1
    low=0

    while low<=high:
        mid=(high+low)//2
        if a[mid]==b[i]:
            return 1
        elif a[mid]>b[i]:
            high=mid-1
        else:
            low=mid+1

    return 0


for i in range(M):
    print(search(i),end=" ")
