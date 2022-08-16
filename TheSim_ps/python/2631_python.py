import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

child=[]
for i in range(N):
    child.append(int(input()))

count=[0]*N

for i in range(N):
    for j in range(i):
        if child[i]>child[j]:
            count[i]=max(count[i],count[j]+1)
        
print(N-(max(count)+1))

