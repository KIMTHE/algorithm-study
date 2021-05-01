import sys
input = lambda : sys.stdin.readline().rstrip()
import queue

q=[]

Num=input()

output=[] #최종 출력


for i in range(int(Num)):
    N=input() # 테스트케이스 첫째줄
    a=list(N.split(' '))
    for j in range(1):
        b=input() # 둘째줄 우선순위
        c=b.split(' ') #c에 배분
        for k in range(len(c)):
            a.append(c[k])

        main=a[int(a[1])+2] #선택된 값 저장
        a[int(a[1])+2]=-1 #선택된값 -1로 특별 저장
        
        for k in range(len(c)):         
            q.append(a[k+2]) # 우선순위 q에 순차적으로 저장

        count=0 #나간 순번

        while(len(q)):
            index= q.pop(0)
            tt=0
            if(index==-1):
                    for z in range (len(q)):
                        if(int(main)<int(q[z])):
                            q.append(index)
                            tt=1
                            break
                    if(tt!=1):
                        
                        count+=1
                        output.append(count)
                        
            else:
                for z in range (len(q)):
                    if(int(index)<int(q[z])):
                            q.append(index)
                            tt=1
                            break
                if(tt!=1):
                    if(int(index)<int(main)):
                        count-=1
                    count+=1
                    

for i in range(len(output)):
    print(output[i])