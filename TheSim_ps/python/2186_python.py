import sys
input = lambda : sys.stdin.readline().rstrip()
# from collections import deque
# import copy

def find(i,j,k,q):
    dir=[[0,1],[0,-1],[1,0],[-1,0]]

    if len(q)==len(w):
        return 1
    
    if visit[i][j][len(q)]!=-1:
        return visit[i][j][len(q)]
    
    visit[i][j][len(q)]=0
    
    for a,b in dir:
        for z in range(1,k+1):
            ai=(a*z)+i
            bj=(b*z)+j
            
            if 0<=ai<N and 0<=bj<M and word[ai][bj]==w[len(q)]:
                q.append([ai,bj])
                visit[i][j][len(q)-1]+=find(ai,bj,k,q)
                q.pop()

    return visit[i][j][len(q)]
        
N,M,K = map(int,input().split())

word=[]

for i in range(N):
    value=list(input())
    word.append(value)

w=list(input())


#answer=[]
count=0
q=[]
for i in range(N):
    for j in range(M):
        if word[i][j]==w[0]:
            q.append([i,j])

visit=[[[-1]*len(w) for _ in range(M)] for _ in range(N)]
for value in q:
    count+=find(value[0],value[1],K,[value])
#print(visit)
print(count)