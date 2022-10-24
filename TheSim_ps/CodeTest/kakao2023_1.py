def solution(today, terms, privacies):
    answer = []

    dict_value={}
    for i in terms:
        a,b=i.split()
        dict_value[a]=int(b)
    
    today=today.split('.')
    today=int(today[0]+today[1]+today[2]) #today의 .제거
    
    count=1
    for i in privacies:
        date,p=i.split()
        
        y,m,d=map(int,date.split('.'))
        
        m+=dict_value[p]    
        if m>12: #12보다 크면 내년
            y+=int(m//12)
            if m%12==0:
                m=1
            else:
                m=int(m%12)
            
        if d==1: #이전달 마지막 날
            if m==1:
                y-=1
                m=12
            else:
                m-=1
            d=28
        else:
            d-=1

        y=str(y)
        m=str(m)
        d=str(d)
        if len(m)<2:
            m='0'+m
        if len(d)<2:
            d='0'+d

        value=int(y+m+d)
        
        if value<today:
            answer.append(count)
        count+=1

    return answer

solution("2022.05.19",["A 16", "B 6", "C 3"], ["2021.08.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])