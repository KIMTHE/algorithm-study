import sys
input = lambda : sys.stdin.readline().rstrip()

def Recursive(C,n):
    if n==1:
        return C
    if n%2==0:
        y= Recursive(C,n//2)
        value=[]
        for i in range(N):
            temp_2=[]
            for j in range(N):
                temp=0
                for k in range(N):
                    temp=((y[i][k]*y[k][j])+temp)
                temp%=1000
                temp_2.append(temp)
            value.append(temp_2)

        return value

    else:
        y= Recursive(C,(n-1)//2)
        value=[]
        for i in range(N):
            temp_2=[]
            for j in range(N):
                
                temp=0
                for k in range(N):
                    temp=((y[i][k]*y[k][j])+temp)
                temp%=1000
                temp_2.append(temp)
            value.append(temp_2)
        
        value_2=[]
        for i in range(N):
            temp_2=[]
            for j in range(N):
                temp=0
                for k in range(N):
                    temp=((value[i][k]*C[k][j])+temp)
                temp%=1000
                temp_2.append(temp)
            value_2.append(temp_2)

        return value_2


N,B = map(int,input().split())
A=[]
for i in range(N):
    A.append(list(map(int,input().split())))

answer=Recursive(A,B)

for i in answer:
    for j in range(len(i)):
        print(i[j]%1000)