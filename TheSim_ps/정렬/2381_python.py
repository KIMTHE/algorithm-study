import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

a=[]

for i in range(N):
    a.append(list(map(int,input().split())))

b=sorted(a,key=lambda x:((x[0]+x[1])))
c=sorted(a,key=lambda x:((x[0]-x[1])))


big=0

big=max(((b[-1][0]+b[-1][1])-(b[0][0]+b[0][1])),((c[-1][0]-c[-1][1])-(c[0][0]-c[0][1])))

print(big)    