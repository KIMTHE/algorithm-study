import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
num=list(map(int,input().split()))
ouput=num

num=set(num)
num=list(num)
num.sort()

value=[[0]*2 for i in range(len(num))]

for i in range(len(num)):
    value[i][0]=num[i]
    value[i][1]=i

dictionary={value[i][0]:i for i in range(len(num))}

for i in range(len(ouput)):
    print(dictionary[ouput[i]],end=' ')
