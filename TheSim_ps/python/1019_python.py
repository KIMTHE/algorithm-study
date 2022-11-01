import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
n_list=list(str(N))

answer=[0]*10

value=len(n_list) #총 길이 값
for i in range(value):
    n=int(n_list[i]) #해당 자릿수 정수값
    
    if i==0: #제일 앞자리수 값 계산
        for j in range(1,n): #1부터 n-1까지는 j0000~j9999까지 반복됨으로 해당 자리수만큼 더해진다
            answer[j]+=10**(value-1)
        answer[n]+=((N%(10**(value-1)))+1) #n값은 n0000~nxxxx값까지 더해진다
        
        
    elif i==value-1: #마지막 자리수
        for j in range(10): #앞에 시작한 자릿수만큼 반복된다.
            answer[j]+=(N//10)-1
        for j in range(1,10): #처음 시작할 때 1부터 9까지 값
            answer[j]+=1
        for j in range(n+1): #마지막에 n까지 반복된다.
            answer[j]+=1
        
    else: #중간 값
        #앞자리가 0인 경우 1~9까지 값
        multi_num=10**(value-(i+1)) #해당 자릿수 10제곱
        for j in range(1,10): #1부터 9까지 해당 자릿수만큼 더해준다.
            answer[j]+=multi_num

        #앞자리가 1이상인 경우 0~9까지 값
        for j in range(10): #0~9까지 앞자리 수 만큼 반복된다.
            answer[j]+=(int(N//10**(value-i))-1)*multi_num
        
        for j in range(n): #n-1까지 해당 자릿수만큼 반복된다.
            answer[j]+=multi_num
        #n값은 그 뒤에 값까지 반복된다.
        answer[n]+=((N%multi_num)+1)
        
print(*answer)
