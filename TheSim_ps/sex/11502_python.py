import sys
input = lambda : sys.stdin.readline().rstrip()

def find(i,sosu):
    for a in sosu:
        for b in sosu:
            for c in sosu:
                if a+b+c==i:
                    print(a,b,c)
                    return 
    print(0)

N= int(input())
Num=[]
for i in range(N):
    Num.append(int(input()))

sosu=[]
for i in range(2,1000): #소수 구하기 

    no=0 #1일시 소수아님
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            no=1
            break
    if no==0:
        sosu.append(i)


for i in range(N):
   find(Num[i],sosu)



