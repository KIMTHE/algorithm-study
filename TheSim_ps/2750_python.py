"""import sys
input = lambda : sys.stdin.readline().rstrip()


N=int(input())

num=[]
for i in range(N):
    num.append(int(input()))

for i in range(N):
    for j in range(N-1-i):
        if num[j]>num[j+1]:
            temp=num[j]
            num[j]=num[j+1]
            num[j+1]=temp 

for i in range(N):
    print(num[i])"""

import sys
input = lambda : sys.stdin.readline().rstrip()

def quick(start,end):
    if(start>=end):
        return

    key=start
    i=start+1
    j=end

    while(i<=j):
        while(i<=end and num[i]<=num[key]):
            i+=1
        while(j>start and num[j]>= num[key]):
            j-=1
        if(i>j):
            temp=num[j]
            num[j]=num[key]
            num[key]=temp
        else:
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
    quick(start,j-1)
    quick(j+1,end)

N=int(input())

num=[]
for i in range(N):
    num.append(int(input()))


quick(0,N-1)

for i in range(N):
    print(num[i])