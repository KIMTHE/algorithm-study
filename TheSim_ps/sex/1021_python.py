import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N,M = map(int,input().split())
num=list(map(int,input().split()))

dq=deque()
for i in range(1,N+1):
    dq.append(i)

answer=0
for i in num:
    value=dq.index(i)
    
    if value<=(len(dq)//2): #절반보다 작다면 왼쪽으로 이동
        # for j in range(value):
        #     temp=dq.popleft()
        #     dq.append(temp)
        dq.rotate(-value) #큐 내의 원소를 우측으로 rotate(k),k만큼 이동 시킨다 음수이면 좌측으로 절대값만큼 이동
        answer+=value
    else:
        # for j in range(len(dq)-value):
        #     temp=dq.pop()
        #     dq.appendleft(temp)
        #     answer+=1
        dq.rotate(len(dq)-value)
        answer+=(len(dq)-value)

    dq.popleft()

    
print(answer)