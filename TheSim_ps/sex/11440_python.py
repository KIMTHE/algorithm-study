import sys
input = lambda : sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**5)
N=int(input())

"""def fpow(a,b):
    if b==0:
        return 1
    x=fpow(a,b//2)%1000000007
    if b%2==0:
        return x*x
    else:
        return x*x*a
"""

def fpow(adj,n):
    if n==1:
        return adj
    elif n%2:
        return multi(fpow(adj,n-1),adj)
    else:
        return fpow(multi(adj,adj),n//2)

def multi(a,b):
    temp=[[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum=0
            for k in range(2):
                sum+=a[i][k]*b[k][j]
            temp[i][j]=sum%1000000007
    return temp

adj=[[1,1],[1,0]]
start=[[1],[1]]
sum=0


for i in range(N+1):
    if i<3:
        sum+=1
    else:
        sum+=pow(multi(fpow(adj,i-2),start)[0][0],2)
        #print(pow(multi(fpow(adj,i-2),start)[0][0],2))
        
print(sum)
    