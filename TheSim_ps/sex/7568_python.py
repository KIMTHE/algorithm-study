import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
answer=[1 for i in range(N)]
lis=[]
for i in range(N):
    a=(list(map(int,input().split())))
    a.append(i)
    lis.append(a)

lis.sort(key=lambda x: -x[0])

for i in range(1,N):
    temp=0
    for j in range(i):
        if lis[i][1]<lis[j][1] and lis[i][0]<lis[j][0]: #나보다 덩치큰사람
                temp+=1
    answer[lis[i][2]]=temp+1
            
        
for i in answer:
    print(i,end=' ')