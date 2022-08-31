import sys
input = lambda : sys.stdin.readline().rstrip()

N= int(input())

for i in range(N):
    reverse=False #뒤집혔는지 체크 false면 안뒤집힘
    front=0 #앞에 숫자 지우기
    rear=0 #뒤에 숫자 지우기

    p=input() #R(뒤집기),D(버리기) 입력
    p=list(p)

    num=int(input())#배열에 들어갈 숫자 갯수
    
    if(num == 0):
        array = input()
        array = []
    else:
        array = list(map(int, input()[1:-1].split(',')))
  
    for j in range(len(p)):
        if p[j]=='R':
            if reverse==False:
                reverse=True
            else:
                reverse=False  
        elif p[j]=='D':
            if reverse==True:
                    rear+=1
            elif reverse==False:
                    front+=1

    if(front+rear<=len(array)):
        if reverse==False:
         array=array[front:len(array) - rear]
         print(str(array).replace(' ', ''))
        else:
            array=array[::-1][rear:len(array) - front]
            print(str(array).replace(' ', ''))
    else:
        print("error")
   