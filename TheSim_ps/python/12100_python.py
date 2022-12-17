import sys
input = lambda : sys.stdin.readline().rstrip()
import copy
def dfs(n,block): #횟수, 블럭 위치
    global answer
    if n==5:
        for i in range(N):
            for j in range(N):
                answer=max(block[i][j],answer)
        return
    

    b=copy.deepcopy(block)
    #왼쪽
    for i in range(N):
        temp=[]
        for j in range(N): #0없애는 작업
            if b[i][j]!=0:
                temp.append(b[i][j])
        for k in range(len(temp)-1):
            if temp[k]==temp[k+1]:
                temp[k]*=2
                temp[k+1]=0
        t=[]
        for j in temp:
            if j!=0:
                t.append(j)

        for z in range(N):
            if z<len(t):
                b[i][z]=t[z]
            else:
                b[i][z]=0
    dfs(n+1,b)

    b=copy.deepcopy(block)
    #오른쪽
    for i in range(N):
        temp=[]
        for j in range(N): #0없애는 작업
            if b[i][j]!=0:
                temp.append(b[i][j])

        for k in range(len(temp)-1,0,-1):
            if temp[k]==temp[k-1]:
                temp[k]*=2
                temp[k-1]=0
        t=[]
        for j in temp:
            if j!=0:
                t.append(j)

        for z in range(N):
            if z<(N-len(t)):
                b[i][z]=0
            else:
                b[i][z]=t[z-(N-len(t))]
    dfs(n+1,b)

    b=copy.deepcopy(block)
    #위
    for i in range(N):
        temp=[]
        for j in range(N): #0없애는 작업
            if b[j][i]!=0:
                temp.append(b[j][i])

        for k in range(len(temp)-1):
            if temp[k]==temp[k+1]:
                temp[k]*=2
                temp[k+1]=0
        t=[]
        for j in temp:
            if j!=0:
                t.append(j)

        for z in range(N):
            if z<len(t):
                b[z][i]=t[z]
            else:
                b[z][i]=0
    dfs(n+1,b)

    b=copy.deepcopy(block)
    #아래
    for i in range(N):
        temp=[]
        for j in range(N): #0없애는 작업
            if b[j][i]!=0:
                temp.append(b[j][i])

        for k in range(len(temp)-1,0,-1):
            if temp[k]==temp[k-1]:
                temp[k]*=2
                temp[k-1]=0
        t=[]
        for j in temp:
            if j!=0:
                t.append(j)

        for z in range(N):
            if z<(N-len(t)):
                b[z][i]=0
            else:
                b[z][i]=t[z-(N-len(t))]
    dfs(n+1,b)

N=int(input())

block=[]

for i in range(N):
    temp=list(map(int,input().split()))
    block.append(temp)

answer=0
dfs(0,block)

print(answer)