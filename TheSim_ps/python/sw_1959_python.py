T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())  
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    answer=0
    
    if N>M:  
        for i in range(N-M+1):
            temp=0
            for j in range(M):
                temp+=A[j+i]*B[j]
            answer=max(answer,temp)
    else:
        for i in range(M-N+1):
            temp=0
            for j in range(N):
                temp+=B[j+i]*A[j]
            answer=max(answer,temp)
            print(answer)
    print("#"+str(test_case)+" "+str(answer))