import sys
input = lambda : sys.stdin.readline().rstrip()
from itertools import combinations, permutations 

N=int(input())

output=[]

for i in range(1,N+1):
    output.append(i)



s=list(permutations(output,len(output)))
   
for i in s:
    for j in i:
        print(j,end=' ')
    print()

