import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

sum=0
d=[0]*1001
def F(N):
    global d
    
    if N==0:
        return 0
    if N==1:
        return 1
    if N==2:
        return 1
    if d[N]!=0:
        return d[N]
    d[N] = F(N-1)+F(N-2)
    return d[N]

print(F(N))