import sys
input = lambda : sys.stdin.readline().rstrip()
p = 1000000007
def find(a,b):
    if b==1:
        return a%p
    if b%2==0:
        y=find(a,b//2)
        return (y*y)%p
    else:
        y=find(a,(b-1)//2)
        return (y*y*a)%p

N,K=map(int,input().split()) #nCk

A=1
B=1
temp=1
for i in range(1,N+1):
    A=(A*i)%p
    if i<=(N-K):
        temp=(temp*i)%p
    if i<=K:
        B=(B*i)%p
B=(B%p * temp%p)%p
# 페르마의 소정리
# (A/B) % p 
# = A * B^-1 % p 
# = A * B^-1 * B^p-1 % p 
# = A * B^p-2 % p 
# = (A % p) * (B^p-2 % p) % p 
print(((A%p)*(find(B,p-2)%p))%p)

