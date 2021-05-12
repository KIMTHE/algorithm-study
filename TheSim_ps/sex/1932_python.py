import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
a=[]
value=[]
for i in range(N):
        Num=list(map(int,input().split(' ')))#값 입력
        a.append([])  #입력값 층별로 저장
        for j in range(len(Num)):
            a[i].append(Num[j])


for i in range(1,N):
    if i==1:
        a[1][0]+=a[0][0]
        a[1][1]+=a[0][0]
    else:
        for j in range(len(a[i])):
            if j==0: #맨 왼쪽
                a[i][j]+=a[i-1][j]
        
            elif j==len(a[i])-1: #맨 오른쪽
                a[i][j]+=a[i-1][j-1]

            elif a[i-1][j-1]>a[i-1][j]:
                a[i][j]+=a[i-1][j-1]
        
            else:
                a[i][j]+=a[i-1][j]
    
big=list(a[len(a)-1])
print(max(big))