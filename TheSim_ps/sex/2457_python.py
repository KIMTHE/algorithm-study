import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

flower=[]
for i in range(N):
    a=list(map(int,input().split()))
    flower.append([(a[0]*100+a[1]),(a[2]*100+a[3])])

flower.sort(key= lambda x : (x[0],x[1]))

answer=[]
answer.append(flower[0])

for i in range(1,N):
    start,end=flower[i]
    pre_s,pre_e=answer[-1]

    if pre_e>=1201:
        break

    if start>=301 and pre_e<start: #더이상 이어지는 꽃이 없을 경우
            answer=[]
            break
            
    if end>pre_e:
        for j in range(len(answer)-1): # 더 긴시간 피는 꽃이 있으면 그 꽃으로 교체
            if answer[j][1]>=start:
                answer=answer[:j+1]  
                answer.append(flower[i])
                break
        else: # 다음 꽃 추가
            
            if start<=301: #3월 미만일 경우 가장 길게 피는 꽃 선택
                answer=[]
                answer.append(flower[i])

            else:
                answer.append(flower[i])
                
    if end>=1201:
        break

if answer:
    if answer[-1][1]<1201:
        answer=[]
    if answer[0][0]>301:
        answer=[]

print(len(answer))
            
        


