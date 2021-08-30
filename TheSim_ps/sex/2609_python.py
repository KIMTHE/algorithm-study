import sys
input = lambda : sys.stdin.readline().rstrip()

a = list(map(int,input().split()))
a.sort()

b=a[0]
c=a[1]

while True:
    if c%b==0:
        print(b)
        print((a[0]//b)*(a[1]//b)*b)
        break
    c=c%b

    if b%c==0:
        print(c)
        print((a[0]//c)*(a[1]//c)*c)
        break
    b=b%c
    
