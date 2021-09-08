import sys
from math import sqrt
input=sys.stdin.readline

t=int(input())

# 골드 바흐의 추측: 2보다 큰 모든 짝수는 두개의 소수의 합으로 표시할 수 있다
# 따라서 3부터의 홀수만 체크해주면 된다.
mm=2000001
prime=[0]*mm # 0이면 소수
prime[1]=1 # 1은 소수가 아님
for i in range(2,int(sqrt(mm))+1):
    if prime[i]==0:
        for j in range(i+i,mm,i):
            prime[j]=1 # 소수 아님 체크

# 소수인 애들만 담아준다 (나중에 홀수-2인 수가 소수인지 판별할 때 쓴다)
q=[]
for i in range(2,mm):
    if prime[i]==0:
        q.append(i)

# 소수인지 
def is_prime(x):
# 소수인 애들로 나뉘게 되면 소수가 아닌 수이다.
    for i in range(0,len(q)):
        if q[i]*q[i]>x: break
        if x%q[i]==0: return 0
    return 1
for _ in range(t):
    x,y=map(int,input().split())
    x+=y
    if x<4: print('NO')
    elif x%2==0: print('YES')
    else:
    # 홀수-2
        x-=2
        # print(x,is_prime(x))
        if is_prime(x): print('YES')
        else: print('NO')