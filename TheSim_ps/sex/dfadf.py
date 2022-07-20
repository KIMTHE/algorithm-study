import sys
# sys.stdin=open('input.txt')
from collections import deque
mod = 10**9

N=int(sys.stdin.readline())
mm=[[0]*10 for _ in range(N+2)]
mm[1]=[0,1,1,1,1,1,1,1,1,1]

for i in range(2,N+1):
    mm[i][0] = mm[i-1][1]
    mm[i][9] = mm[i-1][8]
    for j in range(1,9):
        mm[i][j] = mm[i-1][j-1]+mm[i-1][j+1]

# print(mm)
print(sum(mm[N])%mod)
