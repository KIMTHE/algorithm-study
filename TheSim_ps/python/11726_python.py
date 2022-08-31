import sys
input = lambda : sys.stdin.readline().rstrip()

def find(a):
    if a==1:
        return 1
    if a==2:
        return 2
    if remain[a]!=0:
        return remain[a]

    remain[a]=(find(a-1)+find(a-2))%10007
    return remain[a]

N=int(input())
remain=[0]*1000
remain[1]=1
remain[2]=2

print(find(N))

