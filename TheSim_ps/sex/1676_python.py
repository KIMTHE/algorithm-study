import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5)

N=int(input())

result=1
for item in range(1,N+1,1): 
    result *= item

a=str(result)
a=list(a)
a.reverse()

count=0

for i in range(len(a)):
    if a[i]!='0':
        break
    count+=1

print(count)

