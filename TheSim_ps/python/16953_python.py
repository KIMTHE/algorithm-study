import sys
input = lambda : sys.stdin.readline().rstrip()

N = list(map(int,input().split()))

i=[]
i.append(N[0])
count=[]
count.append(0)

while True:
    if len(i)==0:
        print(-1)
        break

    a=i.pop(0)
    c=count.pop(0)

    if a==N[1]:
        print(c+1)
        break
    if a>N[1]*2 or a>N[1]*10+1:
        print(-1)
        break   

    if a*2<=N[1]:
        i.append(a*2)
        count.append(c+1)
    if a*10+1<=N[1]:
        i.append(a*10+1)
        count.append(c+1) 
