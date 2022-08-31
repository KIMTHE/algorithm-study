import sys
input = lambda : sys.stdin.readline().rstrip()
from itertools import combinations, permutations

N=int(input())
value=list(map(str,input().split()))

a=list(permutations(value))


big=0
for j in range(len(a)):
    sum=0
    for i in range(N-1):
        sum+=abs(int(a[j][i])-int(a[j][i+1]))
    big=max(sum,big)

print(big)