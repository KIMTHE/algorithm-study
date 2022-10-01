from collections import deque

def solution(maps):
    answer = 0

    ground=[]
    for i in maps:
        ground.append(list(i))
    visit=[[0 for _ in range(len(ground[0]))] for _ in range(len(ground))]
 

    dir=[[1,0],[0,1],[-1,0],[0,-1]]
    answer_dic={}
    for i in range(len(ground)):
        for j in range(len(ground[i])):
            if ground[i][j]!='.' and visit[i][j]==0:
                
                q=deque()
                q.append([i,j])
                dic={} #딕셔너리 값
                dic.clear()
                dic[ground[i][j]]=1
                visit[i][j]=1
                while q:
                    i,j=q.popleft()
                    
                    for a,b in dir:
                        ia=i+a
                        jb=j+b

                        if 0<=ia<len(ground) and 0<=jb<len(ground[0]) and visit[ia][jb]==0 and ground[ia][jb]!='.':
                            visit[ia][jb]=1
                            q.append([ia,jb])
                            alpa=ground[ia][jb] #나라 이름
                            if alpa in dic: #값이 있다면 나라 세력 +1
                                dic[alpa]=dic[alpa]+1
                            else: #나라 값 넣기
                                dic[alpa]=1
                
                value=[]
                temp=0
                for k in dic.keys():
                    value.append([dic[k],k])
                
                value.sort(key= lambda x: (x[0],x[1]),reverse=True)
                
                temp=value[0][0]

                for k in range(len(value)):
                    if value[k][0]==value[0][0]: #같으면 점령 안당함
                        if value[k][1] in answer_dic:
                                answer_dic[value[k][1]]=answer_dic[value[k][1]]+value[k][0]
                        else: #나라 값 넣기
                            answer_dic[value[k][1]]=value[k][0]
                    else:#작은 나라면 점령함
                        answer_dic[value[0][1]]=answer_dic[value[0][1]]+value[k][0]

            
    for k in answer_dic.keys():
        answer=max(answer,answer_dic[k])

    return answer

print(solution(["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]))