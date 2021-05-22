import sys
input=sys.stdin.readline

def find(x):
   if x==parent[x]:
      return x
   parent[x]=find(parent[x])
   return parent[x]

def union(x,y):
   x,y=find(x),find(y)
   parent[x]=y

n=int(input())
m=int(input())
arr=[list(map(int,input().split())) for _ in range(m)]
arr=sorted(arr,key=lambda k: k[2])
parent =[i for i in range(0,n+2)]
ans=0
for a in arr:
   start,end,weight=a
   #cycle 확인
   if find(start)==find(end):
      continue
   else:
      ans+=weight
      union(start,end)
print(ans)