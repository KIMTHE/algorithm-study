import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

rgb=[]
for i in range(N):
    a,b,c=map(int,input().split())
    rgb.append([a,b,c])

answer=[[0 for _ in range(3)] for _ in range(N)]
value=1000000
for k in range(3):
    answer[0][k]=rgb[0][k]
    if k==0:
        answer[1][0]=1000000
        answer[1][1]=rgb[1][1]+rgb[0][k]
        answer[1][2]=rgb[1][2]+rgb[0][k]
    
    elif k==1:
        answer[1][0]=rgb[1][0]+rgb[0][k]
        answer[1][1]=1000000
        answer[1][2]=rgb[1][2]+rgb[0][k]
        

    elif k==2:
        answer[1][0]=rgb[1][0]+rgb[0][k]
        answer[1][1]=rgb[1][1]+rgb[0][k]
        answer[1][2]=1000000
        
        
    for i in range(2,N):
        if i==(N-1): #마지막일 경우
            if k==0:
                answer[i][0]=1000000
                answer[i][1]=min(answer[i-1][0],answer[i-1][2])+rgb[i][1]
                answer[i][2]=min(answer[i-1][0],answer[i-1][1])+rgb[i][2]
            elif k==1:
                answer[i][0]=min(answer[i-1][1],answer[i-1][2])+rgb[i][0]
                answer[i][1]=1000000
                answer[i][2]=min(answer[i-1][0],answer[i-1][1])+rgb[i][2]

            elif k==2:
                answer[i][0]=min(answer[i-1][1],answer[i-1][2])+rgb[i][0]
                answer[i][1]=min(answer[i-1][0],answer[i-1][2])+rgb[i][1]
                answer[i][2]=1000000
            break
            
        
        answer[i][0]=min(answer[i-1][1],answer[i-1][2])+rgb[i][0]
        answer[i][1]=min(answer[i-1][0],answer[i-1][2])+rgb[i][1]
        answer[i][2]=min(answer[i-1][0],answer[i-1][1])+rgb[i][2]
        
    value=min(min(answer[N-1]),value)
        

print(value)
    