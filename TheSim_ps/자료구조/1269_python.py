import sys
input = lambda : sys.stdin.readline().rstrip()

N=list(map(int,input().split(' ')))
A=list(map(int,input().split(' ')))
B=list(map(int,input().split(' ')))

A.sort()
B.sort()

count=0
number=[]

A=set(A)
B=set(B)

print(len(A-B)+len(B-A))

