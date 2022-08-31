import sys
input = lambda : sys.stdin.readline().rstrip()

N,K=input().split()
N=int(N)
K=int(K)
temp=list(map(int,input().split()))
output=[0]*N

output[K-1]=sum(temp[:K])

big=output[K-1]
for i in range(K,N):
    output[i]+=output[i-1]
    output[i]+=temp[i]
    output[i]-=temp[i-K]
    
    big=max(output[i],big)

print(output)
print(big)
