import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

road=[]
temp=[]
for i in range(N):
    a=list(map(int,input().split()))
    road.append(a)
    temp.append(a)

value=True
for z in range(N):
    for i in range(N):
        for j in range(N):
            if i!=z and j!=z and road[i][z]!=0 and road[z][j]!=0:
                if road[i][j]==road[i][z]+road[z][j]:
                    road[i][j]=0
                elif road[i][j]>road[i][z]+road[z][j] and road[i][z]!=0 and road[z][j]!=0:
                   
                    value=False


answer=0
if value==False:
    answer=-1
else:
    for i in range(N):
        for j in range(i,N):
            answer+=road[i][j]
print(answer)    
