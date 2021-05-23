#다익스트라
import sys
input = lambda : sys.stdin.readline().rstrip()

def find(x):
   if x==line[x]:
      return x
   line[x]=find(line[x])
   return line[x]

N=int(input())
M=int(input())

line=[0]*(N+1) #연결되어 있는지 확인
for i in range(N+1): #각점에 해당되는 인덱스값
    line[i]=i

value=[[0]*3 for i in range(M)]

for i in range(M):
    a=list(map(int,input().split()))
    value[i][0]=a[0]
    value[i][1]=a[1]
    value[i][2]=a[2]

value=sorted(value,key=lambda x: x[2])

sum=0
for n in range(M):
    if find(line[value[n][0]])==find(line[value[n][1]]):
        continue
    else:
        x,y=find(value[n][0]),find(value[n][1])
        line[x]=y
        sum+=value[n][2]

print(sum)   
    
