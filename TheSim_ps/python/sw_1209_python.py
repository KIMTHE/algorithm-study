#T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 10 + 1):
    num=[]

    N=int(input())
    for i in range(100):
        num.append(list(map(int,input().split())))

    answer=-2147483648
    l_diagonal=0 #왼쪽 대각선
    r_diagonal=0 #오른쪽 대각선
    for i in range(100):
        total=0
        for j in range(100):
            total+=num[i][j]
        answer=max(answer,total)

        total=0
        for j in range(100):
            total+=num[j][i]
        answer=max(answer,total)
    
        l_diagonal+=num[i][i]
        r_diagonal+=num[i][99-i]

    answer=max(l_diagonal,answer)
    answer=max(r_diagonal,answer)

    print("#"+str(test_case)+" "+str(answer))

        
    