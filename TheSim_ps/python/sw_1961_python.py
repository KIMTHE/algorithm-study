T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())

    num=[]
    for i in range(N):
        num.append(list(map(int,input().split())))
    
    num1=[]
    num2=[]
    num3=[]
    for i in range(N):
        temp=[]
        for j in range(N):
            temp.append(num[N-j-1][i])
        num1.append(temp)

        temp=[]
        for j in range(N):
            temp.append(num[N-i-1][N-j-1])
        num2.append(temp)

        temp=[]
        for j in range(N):
            temp.append(num[j][N-i-1])
        num3.append(temp)
    
    
    print("#"+str(test_case))
    for i in range(N):
        for j in range(N):
            print(num1[i][j],end="")
        print(end=" ")
        for j in range(N):
            print(num2[i][j],end="")
        print(end=" ")
        for j in range(N):
            print(num3[i][j],end="")
        if T-1!=test_case:
            print()
