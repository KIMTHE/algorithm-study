import sys
input = lambda : sys.stdin.readline().rstrip()

n,k=input().split()
n=int(n)
k=int(k)

count=0

money=[]
for i in range(n):
    money.append(int(input()))

for i in range(n,0,-1):
    if money[i-1]>k:
        continue
    else:
        count += k//money[i-1]
        k = k%money[i-1]

print(count)
    

