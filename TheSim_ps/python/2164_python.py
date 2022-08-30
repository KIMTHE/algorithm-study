import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N=int(input())

num=deque([i for i in range(1,N+1)])


while len(num)>1:
    num.popleft()
    num.append(num.popleft())

print(num[0])
