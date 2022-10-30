import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

A,B,C=map(int,input().split())

check=0

q=deque()
s=set()
q.append([A,B,C])
s.add((A,B,C))

while q:
    value=q.popleft()
    value.sort()
    if value[0]==value[1] and value[0]==value[2]:
        check=1
        break

   #A,B
    A=value[0]*2
    B=value[1]-value[0]
    C=value[2]

    temp=[A,B,C]
    temp.sort()
    if (temp[0],temp[1],temp[2]) not in s:
        q.append(temp)
        s.add((temp[0],temp[1],temp[2]))

    #A,C
    A=value[0]*2
    B=value[1]
    C=value[2]-value[0]

    temp=[A,B,C]
    temp.sort()
    if (temp[0],temp[1],temp[2]) not in s:
        q.append(temp)
        s.add((temp[0],temp[1],temp[2]))

    #B,C
    A=value[0]
    B=value[1]*2
    C=value[2]-value[1]

    temp=[A,B,C]
    temp.sort()
    if (temp[0],temp[1],temp[2]) not in s:
        q.append(temp)
        s.add((temp[0],temp[1],temp[2]))
    
    

    
if check:
    print(1)
else:
    print(0)