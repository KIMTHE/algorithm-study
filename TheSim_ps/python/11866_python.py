import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque


N,K = map(int,input().split())

d1=deque([i for i in range(1,N+1)])
count=0
answer=[]
while len(d1):
    count+=1
    temp=d1.popleft()

    if count==K:
        count=0
        answer.append(temp)
    else:
        d1.append(temp)
    
for i in range(len(d1)):
    answer.append(d1.popleft())

print("<",end="")
for i in range(len(answer)-1):
    print(answer[i],end=", ")
print(str(answer[-1])+">")


