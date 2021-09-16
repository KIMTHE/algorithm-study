a,b=map(int,input().split())

value=[0]*(b-a+1)
count=0
N=1

while N*N<=b:
    N+=1
    c=a//(N*N)
    while (N*N)*c<=b:
        if ((N*N)*c)-a>=0 and value[((N*N)*c)-a]==0:
            value[((N*N)*c)-a]=1
            count+=1
        c+=1  

print(len(value)-count)
 