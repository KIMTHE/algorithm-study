import sys
input = lambda : sys.stdin.readline().rstrip()

def find(mid): #mid 무게값으로 이 다리를 건널 수 있는지?
    q=[]
    q.append(A)
    visit=[0]*(N+1)
    visit[A]=1
    while q:
        land=q.pop(0) #섬위치

        for i,j in street[land]: #i는 도착 위치, j는 크기
            if j>=mid and visit[i]==0: #이동 중량값이 mid보다 크거나 방문하지 않으면 실행
                if i==B: #B섬에 도착하면 mid 무게로 이동 가능하다는 뜻이므로 True 리턴
                    return True
                visit[i]=1
                q.append(i)

    return False #이동 불가이므로 false 리턴

N,M=map(int,input().split())
bridge=[]
street=[[] for i in range(N+1)] #섬이 이어져있는지 위치 확인

max_value=0
for i in range(M):
    bridge.append(list(map(int,input().split())))
    street[bridge[i][0]].append([bridge[i][1],bridge[i][2]]) #인덱스는 현재 섬, 들어가는 값은 [도착섬,무게] 입력
    street[bridge[i][1]].append([bridge[i][0],bridge[i][2]])

    max_value=max(max_value,bridge[i][2]) #최대값

A,B = map(int,input().split()) #공장이 있는 곳

start=1
end=max_value #최대 무게

while start<=end:
    mid=(start+end)//2
    
    if find(mid): #mid 무게로 이동 가능한지 확인 가능하다면 무게를 더 늘린다
        start=mid+1
    else:
        end=mid-1

print(end)
