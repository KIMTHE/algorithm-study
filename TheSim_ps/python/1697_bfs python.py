import sys
input = lambda : sys.stdin.readline().rstrip()

N,K=input().split()
N=int(N)
K=int(K)


visit=[0]*100001 #모든 위치 방문했는지 확인
find=[] #위치찾기
time=[] #시간

time.append(0) 
find.append(N)

while True: 
     
    i=find.pop(0)
    t=time.pop(0)

    if visit[i] !=1:
        visit[i]=1

        if i-1>=0:
            find.append(i-1) 
            time.append(t+1)
        if 2*i<=100000:
            find.append(i*2)  
            time.append(t+1)
        if i+1<=100000:
            find.append(i+1)    
            time.append(t+1)

    if i==K:
       print(t)
       break     



