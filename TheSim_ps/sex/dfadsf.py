def solution(dist):
    global visit
    global answer
    global value

    answer = []

    #for i in range(len(dist)):
    value=[]
    visit=[0]*len(dist)
    far=0
    find(0,dist,far)

    return answer

def find(N,dist,far): #첫번째 N값에 대한 행렬 만족
    global answer
    #global value
    global visit

    if visit[N]==0:
        visit[N]=1
        value.append(N)
    
    if len(value)==len(dist):
        answer.append(value[:])
    else:
        for i in range(len(dist)):
            
            if dist[value[-1]][i]+far==dist[N][i] and visit[i]==0: #현재 거리보다 작다면

                temp=far #임시 보관
                far+=dist[value[-1]][i]
                visit[i]=1
                value.append(i)
                find(N,dist,far)
                value.pop()
                far=temp
                visit[i]=0

print(solution([[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]))