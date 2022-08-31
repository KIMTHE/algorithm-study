import sys
input = lambda : sys.stdin.readline().rstrip()

#f(n) = f(n-1)+f(n-2)

N=int(input())

temp=[0]*(N+1)

#재귀함수로 풀 경우 성능이 좋지 않아 통과하지 못한다.
for i in range(1,N+1):
    if i==1:
        temp[1]=1
    elif i==2:
        temp[i]=2
    
    else:
        temp[i]=temp[i-1]%15746+temp[i-2]%15746


print(temp[N]%15746)