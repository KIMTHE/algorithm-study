import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

num=[]

for i in range(N):
    temp=int(input())

    if temp==0:
        num.pop()
    else:
        num.append(temp)

print(sum(num))