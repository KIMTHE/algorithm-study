import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N=int(input()) #테스트 케이스 갯수

for i in range(N):
    A,B = map(int,input().split()) #시작값, 끝값

    answer=['0']*10000 #0~9999까지의 계산값
    visit=[0]*10000 #방문여부
    answer[A]='1' #시작값은 처음이니 '1'표시
    visit[A]=1 #시작값은 처음 시작하니 방문표시
    num=deque()
    num.append(A) #num은 계산값
    
    while True:
            value=num.popleft() #계산할 값을 value에 저장

            #D 계산
            if value*2>9999: #2배가 9999보다 크면 10000나머지값
                D_value=(value*2)%10000
            else: #아니면 그냥 *2
                D_value=(value*2)
            
            if value!=D_value and visit[D_value]==0: #계산결과값이 처음값과 같지않거나 방문하지 않았을 경우
                visit[D_value]=1 #방문표시
                answer[D_value]=answer[value]+'D' #계산이전값에 계산기 값에 +D값을 결과값에 저장
                num.append(D_value) #num에 결과값 추가
                
            if D_value==B: #결과값이 최종값이랑 같다면 출력
                A=list(answer[B])
                print("".join(A[1:]))#처음 시작값에 1을 표시했으므로 1을 제외한 나머지값들 출력
                break

            #S
            if value==0: #D와 동일
                S_value=9999
            else:
                S_value=value-1

            if value!=S_value and visit[S_value]==0:
                visit[S_value]=1
                answer[S_value]=answer[value]+'S'
                num.append(S_value)
        
            if S_value==B:
                A=list(answer[B])
                print("".join(A[1:]))
                break
            
            #L
            front=value%1000
            back=value//1000
            L_value=front*10+back #이 식을 이용해 L값을 계산 나머지는 동일

            if value!=L_value and visit[L_value]==0: 
                visit[L_value]=1
                answer[L_value]=answer[int(value)]+'L'
                num.append(L_value)
            
            if L_value==B:
                A=list(answer[B])
                print("".join(A[1:]))
                break
    
            #R
            front=value%10
            back=value//10
            R_value=front*1000+back

            if value!=R_value and visit[R_value]==0:
                visit[R_value]=1
                answer[R_value]=answer[int(value)]+'R'
                num.append(R_value)
        
            if R_value==B:
                A=list(answer[B])
                print("".join(A[1:]))
                break
    