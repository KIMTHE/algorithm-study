import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(5000)

N=list(map(int,input().split()))

mirro=[[0]*(N[1]+1) for i in range(N[0]+1)]
for i in range(1,N[0]+1):
	a=input()
	a=list(a)
	for j in range(len(a)):
		mirro[i][j+1]=int(a[j])

visit=[[0]*(N[1]+1) for i in range(N[0]+1)]

que=[1,1]
visit[1][1]=1
while que:
 start=que.pop(0)
 end=que.pop(0)
 if 0<=start<N[0]: 
    if visit[start+1][end]==0: #아래
        if mirro[start+1][end]!=0:
            visit[start+1][end]=1
            que.append(start+1)
            que.append(end)
            mirro[start+1][end]=mirro[start][end]+1
 if 0<=end<N[1]:
    if visit[start][end+1]==0:   #오른쪽    
        if mirro[start][end+1]!=0:
            visit[start][end+1]=1
            que.append(start)
            que.append(end+1)
            mirro[start][end+1]=mirro[start][end]+1
 if 0<=start<=N[0]:
    if visit[start-1][end]==0:   #위
        if mirro[start-1][end]!=0:
            visit[start-1][end]=1
            que.append(start-1)
            que.append(end)
            mirro[start-1][end]=mirro[start][end]+1
 if 0<end<=N[1]:
    if visit[start][end-1]==0:   #왼쪽   
        if mirro[start][end-1]!=0:
            visit[start][end-1]=1
            que.append(start)
            que.append(end-1)
            mirro[start][end-1]=mirro[start][end]+1


print(mirro[N[0]][N[1]])
