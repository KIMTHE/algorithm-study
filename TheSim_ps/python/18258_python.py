import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

dq=deque()

N=int(input())
for _ in range(N):
    S=input().split()
    
    if S[0]=='push':
        dq.append(int(S[1]))
    elif S[0]=='pop':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif S[0]=='size':
        print(len(dq))
    elif S[0]=='empty':
        if dq:
            print(0)
        else:
            print(1)
    elif S[0]=='front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif S[0]=='back':
        if dq:
            print(dq[-1])
        else:
            print(-1)