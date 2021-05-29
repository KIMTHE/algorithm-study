import sys
input = lambda : sys.stdin.readline().rstrip()

N=list(map(int,input().split()))

num=[]
for i in range(N[0]):
    num.append(int(input()))

for i in range(N[1]):
    a=num
    M=list(map(int,input().split()))
    
    print(min(a[M[0]-1:M[1]]),end=' ')
    print(max(a[M[0]-1:M[1]]))

    https://www.acmicpc.net/blog/view/9
    //세그먼트 트리 이용해서 만들기