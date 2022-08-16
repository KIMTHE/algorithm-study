import sys
input = lambda : sys.stdin.readline().rstrip()

value=[0]*68

def koong(n):

    if value[n]!=0:
        return value[n]

    if n<2:
        value[n]=1
        return 1
    elif n==2:
        value[n]=2
        return 2
    elif n==3:
        value[n]=4
        return 4
    elif n>3:
        value[n]=koong(n-1)+koong(n-2)+koong(n-3)+koong(n-4)
        return value[n]
    

t=int(input())

for i in range(t):
    n=int(input())
    print(koong(n))

