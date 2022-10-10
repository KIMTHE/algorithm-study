import sys
input = lambda : sys.stdin.readline().rstrip()
import itertools
from collections import deque

N,K = map(int,input().split())
s=set()
dir=list(itertools.combinations(range(len(str(N))),2))
def bfs(N,k,s,dir):
    
    q=deque()
    q.append([N,0])
    answer=[]
    while q:
        n,K_value=q.popleft()

        if K_value==k and len(str(n))==len(str(N)):
            answer.append(n)

        elif len(str(n))<2 or len(str(n))<len(str(N)):
            continue

        else:
            for i,j in dir:
                num=list(str(n))
                num[i],num[j]=num[j],num[i]

                temp=int("".join(num))

                if (temp,K_value+1) not in s:
                    s.add((temp,K_value+1))
                    q.append([temp,K_value+1])
            
    return answer

answer=bfs(N,K,s,dir)
if len(answer)==0:
    print(-1)
else:
    print(max(answer))