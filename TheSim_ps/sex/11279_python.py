from re import T
import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
num=[0]

def insert(x):
    num.append(x)
    i=len(num)-1
    
    while i>1:
        if num[i]>num[i//2]:
            num[i],num[i//2]=num[i//2],num[i]
            i=i//2
        else:
            break


def delete():
    print(num[1])

    num[1],num[-1]=num[-1],num[1]
    num.pop()

    i=1
    while T:
        left=i*2
        right=i*2+1
        value=i

        if left<len(num) and num[i]<num[left]:
            i=left
        if right<len(num) and num[i]<num[right]:
            i=right
        
        if value!=i:
            num[value],num[i]=num[i],num[value]

        else:
            break
        


for i in range(N):
    x=int(input())

    if x==0:
        if len(num)==1:
            print(0)
        else:
            delete()
    else:
        insert(x)