import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

chu=list(map(int,input().split()))
chu.sort()

sum=1

for i in range(N):
    if i< N-1:
        sum+=chu[i]

        if chu[0]!=1:
            print(1)
            break

        if sum<chu[i+1]:
            print(sum)
            break
      
    elif i == N-1:
        if sum<chu[N-1]:
            print(sum)
            break
        elif sum>=chu[N-1]:
            print(sum+chu[N-1])
