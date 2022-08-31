import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input()) #테스트케이스 수

for i in range(N):
    num = int(input()) #학생수
    student = list(map(int,input().split())) #학생 팀
    visit = [0] * num #방문 안햇으면 0 했으면 2

    up=0 # 팀이 만들어진 인원 수

    for j in range(num):

        if visit[j]!=0: #방문 했으면 다음 값
            continue

        count=[] #팀을 이루는지 확인
        count.append(j) #첫번째값 추가

        while True:
           
            visit[count[-1]]=2 #제일 마지막 사람 방문 표시

            if visit[student[count[-1]]-1]==2: #연관된 다음 사람 방문했다면 실행
                if student[count[-1]]-1 in count: # 연관된 다음사람이 팀안에 있다면 사이클이 있는 것
                    up+=len(count)-count.index(student[count[-1]]-1) #연관된 다음사람의 index값을 구해 그 이후부터는 팀이므로 전체값에서 index값까지 빼면 팀을 이룬 사람의 수가 up에 더해진다
                break   
                
            count.append(student[count[-1]]-1) #방문하지 않았다면 count에 추가해서 팀을 이루는지 확인
           

    print(num-up) # 전체값에서 팀을 이룬사람값 빼서 팀이 없는 사람 출력



"""
        if up==-1:
             for k in count:
                if visit[k]==0: #팀이 이루어질수 없으므로 1값
                    visit[k]=1
        else:
            for k in count[up:]:
                visit[k]=2
            for k in count[:up]:
                visit[k]=1

    for b in visit:
        if b!=2:
            team+=1
    print(team)
"""








"""
    student.insert(0,'Y')

    team_num=0
    check=0

    for j in range(1,num+1):

        check=0
        team_num=j
        team=[j]
        count=0 #팀이 없는 학생 수

        if student[j]=='Y' or student[j]=='N': #이미 팀이 있거나 팀을 만들 수 없음
            continue
        
        while True:
            
            if student[team[-1]] == 'Y' or student[team[-1]] == 'N': #제일 마지막값에 이어지는 값 확인
                #for k in team: #팀이 될수 없으므로 N으로 입력
                #    student[k] = 'N'
                check=1
                break
            #team[-1]은 1, student[1] = 2, student[2] = 3
            #team[-1]은 5, student[5] = 3, student[3] = Y
            elif student[team[-1]]==student[student[team[-1]]] or student[student[team[-1]]]=='Y':
                if student[team[-1]]==team_num:
                    student[student[team[-1]]]='Y'
                    break

                student[student[team[-1]]]='Y'
                #for k in team: #팀이 될수 없으므로 N으로 입력
                #    student[k] = 'N'
                check=1
                break

            elif student[team[-1]]==team_num:
                #for k in team: #팀이 될수 있으므로 Y
                #    student[k] = 'Y'
                check=2
                break
            
            else:
                if student[team[-1]] in team:
                    check=3
                    break

                team.append(student[team[-1]])

        if check==1:
            for k in team: #팀이 될수 없으므로 N으로 입력
               student[k] = 'N'
        if check==2:
            for k in team: #팀이 될수 있으므로 Y로 입력
               student[k] = 'Y'
        if check==3:
            a= team.index(student[team[-1]])
            for k in team[:a]: #팀이 될수 없으므로 N으로 입력
                        student[k] = 'N'
            for k in team[a:]: #팀이 될수 있으므로 Y로 입력
                        student[k] = 'Y'


    for a in student:
            if a=='N':
                count+=1
    print(count)
"""
    

