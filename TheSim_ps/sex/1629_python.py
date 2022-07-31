import sys
input = lambda : sys.stdin.readline().rstrip()

def find(v,n):
    if n==1:
        return v%C
    if n%2==0:
        y=find(v,n//2)
        return (y*y)%C
    else:
        y=find(v,(n-1)//2)
        return (y*y*v)%C
    
A,B,C=map(int,input().split())

print(find(A,B))