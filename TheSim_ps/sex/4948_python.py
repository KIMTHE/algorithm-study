import sys
input = lambda : sys.stdin.readline().rstrip()

while True:
    N=int(input())

    if N == 0:
        break
    
    count=0

    for i in range(N+1,(2*N)+1):
        
        prime=0 #1일시 소수 아님
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                prime=1
                break
        if prime==0:
            count+=1
    print(count)
