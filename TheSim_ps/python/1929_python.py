import sys
input = lambda : sys.stdin.readline().rstrip()

N=list(map(int,input().split(' ')))

decimal=[]

for i in range(N[0],N[1]+1):
    prime=0
    if i==1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            prime=1
            break
    if prime!=1:
        decimal.append(i)
    

for i in range(len(decimal)):
    print(decimal[i])
