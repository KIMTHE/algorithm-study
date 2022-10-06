import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque
import itertools

def find(x1,y1): #x1,y1에서부터 더러운 곳 까지의 모든 거리

    q=deque()
    q.append([x1,y1])
    visit=[[0 for _ in range(w)] for _ in range(h)]
    dir=[[0,1],[1,0],[0,-1],[-1,0]]
    while q:
        x,y=q.popleft()

        for a,b in dir:
            xa=x+a
            yb=y+b

            if 0<=xa<h and 0<=yb<w and room[xa][yb]!='x' and visit[xa][yb]==0:
                visit[xa][yb]=visit[x][y]+1
                q.append([xa,yb])

    return visit #모든 거리 반환

while True:
    w,h = map(int,input().split())
    if w==0 and h==0:
        break
    
    room=[]
    dirty=[] #더러운 방 찾기
    cleaner=[] #청소기
    for i in range(h):
        value=list(input())
        room.append(value)
        for j in range(w):
            if room[i][j]=='*':
                dirty.append([i,j])
            if room[i][j]=='o':
                cleaner.append(i)
                cleaner.append(j)
    
    visit_temp=find(cleaner[0],cleaner[1]) #시작점에서 각 점마다 거리
    visit_clean=[0]*len(dirty)

    possible=True #도달 불가능한 곳이 있을 경우 False

    for i in range(len(dirty)):
        temp=visit_temp[dirty[i][0]][dirty[i][1]]
        if temp==0: #값이 0이면 도달 불가능 함으로 -1출력후 종료
            print(-1)
            possible=False
            break
        visit_clean[i]=temp

    if possible: 
        visit_dirty=[[0 for _ in range(len(dirty))] for _ in range(len(dirty))] #각 더러운 곳 사이의 거리 구하기

        for i in range(len(dirty)-1): #더러운 칸 끼리의 거리 구하기
            visit=find(dirty[i][0],dirty[i][1]) 
            #i에서 j로 j에서 i의 값은 같으므로 모두 구할 필요 없이 반만 구해도 된다.
            for j in range(i+1,len(dirty)):
                visit_dirty[i][j]=visit[dirty[j][0]][dirty[j][1]]
                visit_dirty[j][i]=visit_dirty[i][j]

        answer=1000000 #최종 답 구하기

        for li in itertools.permutations(range(len(visit_dirty))): #더러운 칸의 인덱스 값으로 순열을 구한다.
            temp=visit_clean[li[0]] #청소기로 부터 처음 도달하는 값
            start=li[0] 
            for idx in range(1,len(li)):
                end=li[idx]
                temp+=visit_dirty[start][end] #더러운 칸 마다 시작은 start 도달은 end
                start=end
            answer=min(answer,temp) 
        print(answer)
