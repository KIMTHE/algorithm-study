import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

a=[]
for i in range(N):
    a.append(int(input()))

a.sort()

for i in range(N):
    print(a[i])