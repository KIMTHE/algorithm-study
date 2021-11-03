import sys
input = lambda : sys.stdin.readline().rstrip()

n=int(input())


num=[0]*1000
num[0]=1
num[1]=3

for i in range(2,n):
    num[i]=2*num[i-2]+num[i-1]
    
print(num[n-1]%10007)
