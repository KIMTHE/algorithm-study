import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque
import copy

N,M = map(int,input().split())

cheeze = []
count=0 #시간
num=0 #마지막 치즈 수
for i in range(N):
    cheeze.append(input().split())

direct = [[1,0],[0,1],[-1,0],[0,-1]] #오,아,왼,위

q=deque()



while True:
    for i in range(N):
        if '1' in cheeze[i]:
            break
    else:
        break

    visit=[[0]*M for i in range(N)]
    c=copy.deepcopy(cheeze)
    q.append([0,0])
    while q:
        a,b=q.popleft()

        for i,j in direct:
            if a+i>=0 and a+i<N and b+j>=0 and b+j<M and cheeze[a+i][b+j]=='0' and visit[a+i][b+j]==0:
                q.append([a+i,b+j])
                visit[a+i][b+j]=1
            
            if a+i>=0 and a+i<N and b+j>=0 and b+j<M and cheeze[a+i][b+j]=='1'and visit[a+i][b+j]==0:
                cheeze[a+i][b+j]='0'
                visit[a+i][b+j]=1
    count+=1


print(count)
count=0
for i in range(N):
    for j in range(M):
        if c[i][j]=='1':
            count+=1
print(count)




"""
while True:
    for i in range(N):
        if '1' in cheeze[i]:
            break
    else:
        break

    count+=1

    for i in range(N): #세로 확인 왼쪽에서 오른쪽으로 
        for j in range(M):
            
            if cheeze[i][j]=='1' or cheeze[i][j]==count:
                cheeze[i][j]=count
                break
            for k in range(N):
                if i+k<N and (cheeze[i+k][j]=='1' or cheeze[i+k][j]==count):
                    cheeze[i+k][j]=count
                    break
            for k in range(N):
                if i-k>0 and (cheeze[i-k][j]=='1' or cheeze[i-k][j]==count):
                    cheeze[i-k][j]=count
                    break

    for i in range(N): #세로 확인 오른쪽에서 왼쪽
        for j in range(M-1,0,-1): #반대쪽 확인
            

            if cheeze[i][j]=='1' or cheeze[i][j]==count:
                cheeze[i][j]=count
                break
            for k in range(N):
                if i+k<N and (cheeze[i+k][j]=='1' or cheeze[i+k][j]==count):
                    cheeze[i+k][j]=count
                    break
            for k in range(N):       
                if i-k>0 and (cheeze[i-k][j]=='1'or cheeze[i-k][j]==count):
                    cheeze[i-k][j]=count
                    break

    for j in range(M): #가로 위에서 아래
        for i in range(N):
            

            if cheeze[i][j]=='1' or cheeze[i][j]==count:
                cheeze[i][j]=count
                break

            for k in range(M):
                if j+k<M and (cheeze[i][j+k]=='1' or cheeze[i][j+k]==count):
                    cheeze[i][j+k]=count
                    break
            for k in range(M):
                if j-k>0 and (cheeze[i][j-k]=='1' or cheeze[i][j-k]==count):
                    cheeze[i][j-k]=count
                    break

    for j in range(M): #가로 아래에서 위
        for i in range(N-1,0,-1):
            

            if cheeze[i][j]=='1' or cheeze[i][j]==count:
                cheeze[i][j]=count
                break
            for k in range(M):
                if j+k<M and (cheeze[i][j+k]=='1' or cheeze[i][j+k]==count):
                    cheeze[i][j+k]=count
                    break
            for k in range(M):
                if j-k>0 and (cheeze[i][j-k]=='1' or cheeze[i][j-k]==count):
                    cheeze[i][j-k]=count
                    break

for i in range(N):
    for j in range(M):
        if cheeze[i][j]==count:
            num+=1
    
print(count)
print(num)


value=[] #치즈 있는값만 찾기
for i in range(N):
    for j in range(M):
        if cheeze[i][j]==1:
            value.append([i,j])

while value:
    i,j=value.pop(0)
    for a,b in direct: #주위 치즈 찾기
        if cheeze[i+a][j+b]=='1':
            cheeze[i+a][j+b]=cheeze[i][j]+1
            value.append([i+a,j+b])
        
print(cheeze)
"""