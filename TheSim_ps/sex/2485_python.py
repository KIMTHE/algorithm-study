import sys
input = lambda : sys.stdin.readline().rstrip()

def gcd(a,b):
    if b: 
        return gcd(b, a%b)  
    return a
    
N=int(input())
tree=[]
for i in range(N):
    tree.append(int(input()))

count=0
distance=[] #최소 간격 구하기

for i in range(1,len(tree)):
        distance.append(tree[i]-tree[i-1])

a=distance[0]
for i in range(1,len(distance)): #최대공약수 구하기
    
    a=gcd(a,distance[i])


for i in distance:
    count+=i//a-1
    
    
print(count)




