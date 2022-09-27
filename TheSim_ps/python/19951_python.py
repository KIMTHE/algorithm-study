import sys
input = lambda : sys.stdin.readline().rstrip()

N,M = map(int,input().split())
high=list(map(int,input().split()))

nsum=[0 for _ in range(N+1)]
for i in range(M):
    a,b,h=map(int,input().split())
    nsum[a-1]+=h
    nsum[b]-=h
    
for i in range(1,N+1):
    nsum[i]+=nsum[i-1]

for i in range(N):
    high[i]+=nsum[i]

print(*high)