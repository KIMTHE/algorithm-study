import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

c=[0]*10001 #메모리 초과로 입력수가 10000까지 이므로 10001까지
for i in range(N):
    b=int(input())
    c[b]+=1 #중복된 값은 인덱스 값을 증가
    
for i in range(10001):      
    if c[i]!=0:
        for a in range(c[i]):
            sys.stdout.write(str(i)) #pypy를 사용할때는 sys.stdout.write를 사용해야 메모리 초과가 안됨 
            sys.stdout.write('\n') #python를 사용할 때는 print(i)사용 가능


