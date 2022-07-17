import sys
input = lambda : sys.stdin.readline().rstrip()

def gcd(a,b): #유클리드 호제법 최대공약수 구하기
    while b>0:
        temp=a
        a=b
        b=temp%b
    return a

N=int(input())
M=[]
for i in range(N):
   M.append(int(input()))
# 값 M로 같은 나머지가 나오면 A,B,C는 이러한 식이 나온다.
# A%M = A-(A/M)*M  , B%M = B-(B/M)*M, C%M = C-(C/M)*M
# A%M과 B%M은 같은 나머지 값이므로 A-(A/M)*M = B-(B/M)*M 이다.
# 그러면 A-B = M*(A/M-B/M) 이 된다. 그렇다면 여기서 공통된 M이 있는데 이는 공약수가 있다는 뜻이다.
# 그러므로 A,B,C... 에서 최대 공약수를 M을 찾고 M의 약수를 찾으면 정답이 나온다.

answer=[]
for i in range(1,len(M)):
    answer.append(M[i]-M[i-1]) #A-B의 값을 구함

tmp=answer[0]
for i in range(1,len(answer)): #A-B, B-C... 의 값 최대공약수 구하기
    tmp=gcd(tmp,answer[i])

for i in range(2,tmp+1): #최대공약수의 약수 출력
    if tmp%i==0:
        print(i,end=' ')