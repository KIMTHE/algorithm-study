import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5) #재귀 재한 해제

def find(N): #N값에 대한 가장 거리가 먼 값까지의 노드를 answer에 저장
    global answer #answer 리스트

    if visit[N-1]==1: #방문 했다면 마지막 값에 도달했다가 돌아온 것이므로 
        if len(stack)-1>len(answer):#해당 값 이전값까지 비교
            answer=stack[:-1]
        return
    visit[N-1]=1 #방문 표시
    
    for i in bridg_map[N-1]: #N값에 연결된 값들 확인
        stack.append(i) #stack에 추가
        find(i) #재귀 함수
        stack.pop() #마지막을 찍고 돌아온 것이므로 마지막값을 빼준다
    return

N=int(input())

bridg_map=[[]for i in range(N)]

for i in range(N-1):
    a,b= map(int,input().split())
    bridg_map[a-1].append(b)
    bridg_map[b-1].append(a)

value=[]
value.append(1) #아무값이나 넣어도 된다. 첫번째값 추가
visit=[0]*N
visit[0]=1 #첫번째 노드 방문

while value: # 아무값이나 넣어서 가장 멀리 있는 값을 찾은 후 찾은 값에서 먼 값을 찾는다
    q=value.pop(0)

    for i in bridg_map[q-1]:
        if visit[i-1]==0:
            value.append(i)
            visit[i-1]=1
            big=i #가장 마지막에 나온 값이 가장 먼 값이다

stack=[]
stack.append(big) #가장 먼값 추가
visit=[0]*N
answer=[] #먼값에서 먼값의 방문한 노드들의 값 저장
find(big) # 먼값에서 먼값을 찾아서 해당 값에 중간 값이 최적의 장소이다

firebase=answer[(len(answer))//2] #최적의 장소

stack=[]
stack.append(firebase)
visit=[0]*N
answer=[]
find(firebase) #최적의 장소에서 가장 먼 값 검색

print(len(answer)-1) # 출발 장소도 포함됨으로 -1


    