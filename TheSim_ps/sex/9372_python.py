import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

for i in range(N):
    count=0 #비행기 종류 수

    test=list(map(int,input().split()))
    airport=[[]*(test[0]+1) for i in range(test[0]+1)]
    for j in range(test[1]):
        a=(list(map(int,input().split())))
        airport[a[0]].append(a[1])
        airport[a[1]].append(a[0])
    

    que=[1]
    visit=[0]*(test[0]+1)
    while que:
        a=que.pop(0)
        if visit[a]==1:
            continue
        count+=1
        visit[a]=1
        for i in airport[a]:
            if visit[i]==0:
                que.append(i)
                
    print(count-1)    
         

    