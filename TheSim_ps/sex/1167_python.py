import sys
input = lambda : sys.stdin.readline().rstrip()

def find(q,far_num,far_length): #트리에서 먼거리 찾기
    visit=[0]*(V+1)
    visit[far_num]=1
    while q:
        num,length=q.pop(0)
        
        if far_length<length: #거리가 더 멀다면 가장 먼 노드 값을 바꾼다
            far_length=length
            far_num=num

        for a,b in answer[num]: #해당 노드와 연결된 모든 노드에서 거리 찾기
            if b!=0 and visit[a]==0: #방문하지 않았다면
                q.append([a,b+length]) #노드값과 거리값 추가
                visit[a]=1 #방문 표시
    
    return far_num,far_length #거리가 제일 먼 노드와 거리값 리턴

V=int(input())
answer=[[] for i in range(V+1)]

for i in range(V):
    temp=list(map(int,input().split()))
    
    for j in range(1,len(temp)-1,2):
        answer[temp[0]].append([temp[j],temp[j+1]])

far_num=1
far_length=0

far_num,far_length=find([[1,0]],far_num,far_length) #첫번째 노드에서 가장 먼거리 찾기
far_num,far_length=find([[far_num,0]],far_num,far_length) #가장 먼 노드에서 가장 먼 거리찾기

print(far_length)