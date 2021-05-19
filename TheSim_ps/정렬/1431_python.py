import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

serial=[] #시리얼 번호

for i in range(N):
    num=0 #정수값
    a=input()#시리얼 번호 입력
    b=list(a) #시리얼 번호를 구분
    for j in b:
        if j.isdigit(): #정수인지 확인
            num+=int(j)
        
    serial.append((a,num))

serial=sorted(serial,key=lambda x:(len(x[0]),x[1],x[0])) #길이별로 정렬

for i in range(N):
    print(serial[i][0])    