import sys
input = lambda : sys.stdin.readline().rstrip()

N,K = map(int,input().split())
NUM=list(input())
value=K #최종 출력때 지우기 횟수 남았을 경우를 대비해서 값 보존
temp=[] #스택값
temp.append(NUM[0]) #처음 값 넣어준다
for i in range(1,N): #처음값을 넣었으니 그다음 인덱스 1부터 시작
    if temp[-1]<NUM[i]: #스택의 마지막 값이 NUM[i] 보다 작으면 
        while temp and K>0 and temp[-1]<NUM[i]: #스택에 값이 있고, 지우기 횟수가 남아있고, 값이 더 작은 경우
                temp.pop() # 스택값을 지운다
                K-=1 #지우기 횟수를 줄인다
        temp.append(NUM[i]) #그리고 다음값을 넣어준다
    else:
        temp.append(NUM[i]) #이 외에 스택의 마지막 값이 더 크거나 K값이 음수일 경우 다 추가해준다.

print(''.join(temp[:N-value])) #반복문이 모두 실행됬음에도 지우기 횟수가 남았을 경우를 대비해 N-value를 해준다.

