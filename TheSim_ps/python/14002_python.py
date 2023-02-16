import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
num=list(map(int,input().split()))

answer=[]
value=[[]for _ in range(N)]
value[0].append(num[0])
answer.append(num[0])
for i in range(1,N):
    temp=[]
    temp.append(num[i])
    for j in range(i):
        if num[i]>num[j]: #뒤에 수열로 붙일 수 잇을 경우
            if len(temp)<len(value[j])+1:
                temp=value[j][:]
                temp.append(num[i])
    value[i]=temp[:]
    if len(answer)<len(temp):
        answer=temp[:]

print(len(answer))
print(*answer)
            