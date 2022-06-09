import sys
input = lambda : sys.stdin.readline().rstrip()

def find(q,far_num,far_length):
    visit=[0]*(V+1)
    visit[far_num]=1
    while q:
        num,length=q.pop(0)
        
        if far_length<length:
            far_length=length
            far_num=num

        for a,b in answer[num]:
            if b!=0 and visit[a]==0:
                q.append([a,b+length])
                visit[a]=1
    
    return far_num,far_length

V=int(input())
answer=[[] for i in range(V+1)]

for i in range(V):
    temp=list(map(int,input().split()))
    
    for j in range(1,len(temp)-1,2):
        answer[temp[0]].append([temp[j],temp[j+1]])

far_num=1
far_length=0

far_num,far_length=find([[1,0]],far_num,far_length)
far_num,far_length=find([[far_num,0]],far_num,far_length)

print(far_length)