import sys
input = lambda : sys.stdin.readline().rstrip()



while True:
    wrong=0 # 1이면 반례
    N=int(input())
    if N==0:
        break

    for i in range(2,N):
        
        if i%2==0:
            continue
        prime=0 # 소수인지 아닌지 확인
           
        sosu=N-i
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                prime=1
                break


        for j in range(2,int(sosu**0.5)+1):
            if sosu%j==0:
                prime=1
                break

        if prime!=1:
            print(str(N)+" = "+str(i)+" + "+str(sosu))
            wrong=1
            break
    if wrong!=1:
        print("Goldbach's conjecture is wrong.")
        
            
    