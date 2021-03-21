import sys
input = lambda:sys.stdin.readline().rstrip()

N=int(input())
a=list(map(int,input().split()))

a=list(set(a))
a.sort()

for n in a :
     print(n, end=' ')