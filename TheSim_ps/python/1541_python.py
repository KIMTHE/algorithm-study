import sys
input = lambda : sys.stdin.readline().rstrip()
                
cal=input()
cal=list(cal) #식을 리스트로 나누기
num=[]#숫자
ope=[]#연산자

temp="" #임시 저장값
for i in cal: #식을 하나씩 나눈 값중 숫자로 이루어진 값만 모아 하나의 숫자값을 만들고 
    #연산 값이 나오면 앞에 모은 숫자를 num에 넣고 연산은 ope에 넣어 숫자와 연산값을 따로 저장해준다.
    if i.isdigit():
        temp+=i
    else:
        num.append(temp)
        ope.append(i)
        temp=""    
num.append(temp) #마지막 숫자값은 따로 넣어준다.

count=0 #pop시 빈 리스트 값만큼 빼준다
for i in range(len(num)-1): #모든 항의 덧셈 계산
    if ope[i]=='+' and len(num)>1: #덧셈값이라면 계산
        i=i-count #pop해서 빠진만큼 빼준다
        num[i]=int(num[i])+int(num[i+1])
        num.pop(i+1) #덧셈을 하고 난 뒤 뒤의 값은 필요없으니 pop해준다
        count+=1 

for i in range(len(num)-1): #덧셈연산이 끝나고 뺄셈만 남았으니 차례대로 뺄셈 해준다.
    num[i+1]=int(num[i])-int(num[i+1])

print(int(num[-1])) #가장 마지막 값이 정답