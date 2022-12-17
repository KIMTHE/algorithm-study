def solution(s, times):
    answer = []

    day=list(map(int,s.split(":")))
    year=day[0] #년
    month=day[1] #월
    d=day[2] #일
    h=day[3] #시
    m=day[4] #분
    s=day[5] #초

    check=1 #1일1저금 체크 
    temp=d
    answer_day=1 #저금 일수 체크

    for i in times:
        t=list(map(int,i.split(":")))
        t_d=t[0] #일
        t_h=t[1] #시
        t_m=t[2] #분
        t_s=t[3] #초

        answer_day+=t_d #저금 일수 계산
        d+=t_d
        h+=t_h
        m+=t_m
        s+=t_s
        
        if s>=60:
            s-=60
            m+=1
        if m>=60:
            m-=60
            h+=1
        if h>=24:
            h-=24
            d+=1
            answer_day+=1 #저금 일수 계산
        if d>=31:
            month+=d//30
            d%=30
            if d%30==0:
                month-=1
                d=30
                
        if month>=13:
            month-=12
            year+=1
        

        if t_d<=1: #1일 1저금 체크
            if d-temp>1:
                check=0
        else: 
            check=0
        temp=d


    answer=[check,answer_day]

    return answer

a=solution("2021:04:12:16:08:35",["01:06:30:00", "01:01:12:00", "00:00:09:25"])
print(a)