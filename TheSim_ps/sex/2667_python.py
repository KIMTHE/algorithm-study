import sys
input = lambda : sys.stdin.readline().rstrip()

def find(i,j,count):
    if house[i][j]==1 and visit[i][j]==0:
        visit[i][j]=1
        count+=1
        if i-1>=0 and visit[i-1][j]==0:
            if house[i-1][j]==1:
                
                count=find(i-1,j,count)

        if i+1<N and visit[i+1][j]==0:
            if house[i+1][j]==1:
                
                count=find(i+1,j,count)

        if j-1>=0 and visit[i][j-1]==0:
            if house[i][j-1]==1:
                
                count=find(i,j-1,count)

        if j+1<N and visit[i][j+1]==0:
            if house[i][j+1]==1:
                
                count=find(i,j+1,count)
    return count

N=int(input())

house=[]
for i in range(N):
    house.append(list(map(int,input())))

visit=[[0]*N for i in range(N)]

value=[]
for i in range(N):
    for j in range(N):
        count=0
        a=find(i,j,count)
        if a!=0:
            value.append(a)

print(len(value))
value.sort()
for i in value:
    print(i)
