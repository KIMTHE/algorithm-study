import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque
K=int(input())

for i in range(K):
    V,E=map(int,input().split())
    line=[[]for _ in range(V+1)]
    for j in range(E):
        a,b=map(int,input().split())
        line[a].append(b)
        line[b].append(a)
    
    visit=[0]*(V+1)

    visit[0]=1
    
    answer="YES"
    for k in range(1,V+1): 
        #이분 그래프는 모든 노드가 이어지지 않아도 이분 그래프가 됨으로 모든 노드를 확인해줘야 한다.
        if visit[k]!=0:
            continue
        q=deque()
        q.append(k)
        visit[k]=1
        while q:
            value=q.popleft()
            num=visit[value] #이분 그래프 1과 2로 나뉨
            
            for i in line[value]:
                if visit[i]==num: #분할안됨으로 이분 그래프가 아님
                    answer="NO"
                    q.clear()
                    break
                if visit[i]==0:
                    q.append(i)
                    if num==1:
                        visit[i]=2
                    else:
                        visit[i]=1

    print(answer)