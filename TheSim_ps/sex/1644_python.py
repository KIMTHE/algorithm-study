import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

num=[]

for i in range(2,N+1):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        num.append(i)

count=0
start=0
end=0

while  end<=len(num): #투포인트 알고리즘
    
    if N==sum(num[start:end]):
        count+=1
        end+=1
    elif N> sum(num[start:end]):
        end+=1
    elif N<sum(num[start:end]):
        start+=1

"""
for i in range(len(num)): #일반 반복문
    value=0 #더한 값
    for j in range(i,len(num)):
        value+=num[j]
        if value==N:
            count+=1
            break
        elif value>N:
            break
"""
print(count)
