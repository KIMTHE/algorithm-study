import sys
input = lambda : sys.stdin.readline().rstrip()

N=list(map(int,input().split()))

coin=[]
for i in range(N[0]):
    coin.append(int(input()))

coin.sort()

value=[0]*(N[1]+1) #모든 값을 비교
value[0]=1 # 첫번째는 1

for i in coin:
    for j in range(i,N[1]+1):
        value[j]+=value[j-i]

print(value[N[1]])
  

    