import sys
input = lambda : sys.stdin.readline().rstrip()

def find(x,value): #인덱스값과 현재 계산값
    global max_value
    global min_value
    dir=['+','-','*','/']
    if x==N:
        
        max_value=max(max_value,value)
        min_value=min(min_value,value)
    
    else:
        for i in range(len(cal)):
            if cal[i]:
                cal[i]-=1
                if i==0:
                    temp=value+num[x]
                elif i==1:
                    temp=value-num[x]
                elif i==2:
                    temp=value*num[x]
                elif i==3:
                    temp=value/num[x]
                # temp=eval(str(value)+dir[i]+str(num[x])) #eval함수를 사용하면 시간복잡도가 더 오래걸릴수 있다.
                find(x+1,int(temp)) #나눗셈을 할 때 -1//3은 0이 나와야되는데 -1이 나오므로 /로 해서 int로 정수값만 걸러낸다
                cal[i]+=1
                

N=int(input())
num=list(map(int,input().split()))
cal=list(map(int,input().split())) #+,-,*,//
max_value=-1000000001
min_value=1000000001

find(1,num[0])

print(max_value)
print(min_value)


