import sys
input = lambda : sys.stdin.readline().rstrip()

computer=int(input()) #컴퓨터 수
network=int(input()) #연결된 수
virus=[[]*computer for i in range(computer)]
error=[0 for i in range(computer)] # 1일시 바이러스 감염

for i in range(network):
    a=list(map(int,input().split(' ')))
    virus[a[0]-1].append(a[1])
    virus[a[1]-1].append(a[0])

def dfs(i):
    error[i]=1
    for j in virus[i]:
        if error[j-1]!=1:
            dfs(j-1)
        

dfs(0)

count=0
for i in range(len(error)):
    if error[i]==1:
        count+=1

print(count-1)
