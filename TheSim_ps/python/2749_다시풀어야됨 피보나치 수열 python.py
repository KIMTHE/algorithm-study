import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5)
N=int(input())

dic={}

def F(N):
    
    if N==0:
        return 0
    if N==1:
        return 1
    if N==2:
        return 1
    if N in dic:
        return dic[N]

    dic[N] = F(N-1)+F(N-2)
    return dic[N]

print(F(N%1000000)%1000000)