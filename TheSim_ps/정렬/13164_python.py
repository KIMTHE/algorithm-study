import sys
input = lambda : sys.stdin.readline().rstrip()

N=list(map(int,input().split())) #조
tall=list(map(int,input().split())) #키순

value=[] #키를 뺀값

for i in range(1,N[0]):
    value.append(tall[i]-tall[i-1])

value.sort()

sum=0 #값 합계

if N[0]==N[1]:
    sum=0
else:
    for i in range(N[0]-N[1]):
        sum+=value[i]


print(sum)