import sys
input = lambda : sys.stdin.readline().rstrip()


N=list(map(int,input().split()))
left=list(input())
right=list(input())

switch=[[0]*3 for i in range(N[0])]

for i in range(N[0]):
    switch[i][0]=left[i]
    switch[i][1]=right[i]

place=0 #현재 위치
que=[]
que.append(place)
que.append(0)

visit=[[0]*2 for i in range(N[0])]

time=1
last=0

end=0

while que:
 count=time
 time=0

 for i in range(count):
    a=que.pop(0) #위치
    b=que.pop(0) #왼쪽 오른쪽

    if last>N[0]:
        print(0)
        end=1
        break

    if (a+N[1])>=N[0] or a+1>=N[0]:
        print(1)
        end=1
        break

    if visit[a+1][b]==0:    
     if switch[a+1][b]=='1':
      if a+1>last:
        que.append(a+1)
        que.append(b)
        visit[a+1][b]=1

        time+=1

    if a-1>=0:
     if visit[a-1][b]==0:
        if switch[a-1][b]=='1':
         if a-1>last:    
            que.append(a-1)
            que.append(b)
            visit[a-1][b]=1

            time+=1

    if b==1:
     if visit[a+N[1]][0]==0:      
        if switch[a+N[1]][0]=='1':
         if a+N[1]>last:
            que.append(a+N[1])
            que.append(0)
            visit[a+N[1]][0]=1

            time+=1

    else:
     if visit[a+N[1]][1]==0:    
        if switch[a+N[1]][1]=='1':
         if a+N[1]>last:
            que.append(a+N[1])
            que.append(1)
            visit[a+N[1]][1]=1

            time+=1
    
    if not que:
        print(0)
        break

 if end==1:
     break

 last+=1

 