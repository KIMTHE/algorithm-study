import sys
input = lambda : sys.stdin.readline().rstrip()

def dfs(i,j,visit,n,v):
    global answer
    dir=[[1,0],[0,1],[0,-1]]
    
    if n==4:
        #print(visit,v)
        answer=max(answer,v)
        return

    for a,b in dir:

        ia=i+a
        jb=j+b

        if 0<=ia<N and 0<=jb<M and [ia,jb] not in visit:
                    visit.append([ia,jb])
                    n+=1
                    v+=value[ia][jb]
                    dfs(ia,jb,visit,n,v)
                    v-=value[ia][jb]
                    n-=1
                    visit.pop()
        if n==3:

            ia=visit[-2][0]+a
            jb=visit[-2][1]+b

            if 0<=ia<N and 0<=jb<M and [ia,jb] not in visit:
                    visit.append([ia,jb])
                    n+=1
                    v+=value[ia][jb]
                    dfs(ia,jb,visit,n,v)
                    v-=value[ia][jb]
                    n-=1
                    visit.pop()

    return



N,M=map(int,input().split())

value=[]
for i in range(N):
    temp=list(map(int,input().split()))
    value.append(temp)

answer=0
for i in range(N):
    for j in range(M):
        visit=[[i,j]]
        dfs(i,j,visit,1,value[i][j])

print(answer)