import sys
input = lambda : sys.stdin.readline().rstrip()

inf = 1000000

def pow(n,C): #거듭제곱
    if n==1:
        return C
    else:
        if n%2: #홀수이면
            temp=pow(n-1,C)
            return mat(temp,C)
        else: #짝수면
            temp=pow(n//2,C)
            return mat(temp,temp)

def mat(A,B): #행렬 계산
    temp=[[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j]+=(A[k][j]*B[i][k])
            temp[i][j]%=inf
    return temp


n=int(input())
A=[[1,1],[1,0]]
print(pow(n,A)[0][1])