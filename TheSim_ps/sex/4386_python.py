import sys
import math
input = lambda : sys.stdin.readline().rstrip()

def union(a,b): #a,b 결합
    a=find(a)
    b=find(b)

    p[b]=a

def find(a): #a의 연결된 값 찾기
    if p[a]==a:
        return a
    else:
        return find(p[a])

N=int(input())

star=[]

global p
p=[] #union find
for i in range(N): #위치 입력
    star.append(list(map(float,input().split())))
    p.append(i)

value=[]
for i in range(N):
    for j in range(i,N): #점들 사이의 거리 계산, 중복 방지를 위해 i값부터 찾음
        a=(star[j][0]-star[i][0]) #x2-x1
        b=(star[j][1]-star[i][1]) #y2-y1
        c=math.sqrt((a**2)+(b**2))
        if c!=0: #0은 자기 자신이므로 이를 제외한 값,좌표값을 저장
            value.append([c,i,j])

value.sort() #거리가 작은 순부터 정렬

answer=0
for a,b,c in value:
    if find(b)!=find(c): #두 좌표가 연결되어 있지 않으면 값을 더해준다
        answer+=a
        union(b,c) # 두 좌표를 합쳐준다

print(round(answer,2)) #최종 더한 값에서 두자리 수까지반올림으로 출력



