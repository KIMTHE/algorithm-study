import sys
input = lambda:sys.stdin.readline().rstrip()

N=int(input())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

result=0

for i in range(N):
   result += a[i]*b[i]

print(result)