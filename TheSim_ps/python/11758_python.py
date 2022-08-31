import sys
input = lambda : sys.stdin.readline().rstrip()

N=[]
for i in range(3):
    N.append(list(map(int,input().split())))

a=(N[1][0]-N[0][0])*(N[2][1]-N[0][1])-(N[2][0]-N[0][0])*(N[1][1]-N[0][1])

if a<0:
    print(-1)
elif a>0:
    print(1)
else:
    print(0)