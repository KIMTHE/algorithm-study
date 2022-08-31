import sys
input = lambda : sys.stdin.readline().rstrip()

N=list(map(int,input().split()))

connect=[[0]*(N[0]+1) for i in range(N[0]+1)] #연결 리스트

for i in range(N[1]):
    A=list(map(int,input().split()))
    connect[A[0]][A[1]]=A[1]
    connect[A[1]][A[0]]=A[0]

dfs_output=[]
bfs_output=[]
visit=[0]*(N[0]+1)

stack=[]#연결된 값 넣는 스택 리스트\
def DFS(v):
    global dfs_output
    global visit
  
    visit[v]=1
    dfs_output.append(v)
    
    
    for i in range(1,N[0]+1):
        if visit[i]==0 and connect[v][i]!=0:
            DFS(i)


visit2=[0]*(N[0]+1)
#queue=[] #연결된 값을 넣는 큐 리스트

def BFS(v):
    global bfs_output
    global visit2
    
    if len(bfs_output)>=N[0]:
        return
    queue=[v]
    visit2[v]=1
    while(queue):
     
        v=queue[0]
        bfs_output.append(v)
        del queue[0]
                 
        for i in range(1,N[0]+1):
            if visit2[i]==0 and connect[v][i]!=0:
             queue.append(i)
             visit2[i]=1
   
        


DFS(N[2]) #시작 V값
BFS(N[2]) 

for i in range(len(dfs_output)):
    print(dfs_output[i],end=" ")

print()
for i in range(len(bfs_output)):
    print(bfs_output[i],end=" ")
