import sys
input = lambda : sys.stdin.readline().rstrip()

div=1000000000

def find(n,c): #현재값과 카운트값
    global count

    if count[n][c]:
        return (count[n][c])

    if c==N:
        if n==9 or n==0:
            count[n][c]=1
            return 1
        else:
            count[n][c]=2
            return 2 

    if n==0:
        count[n][c]=(find(n+1,c+1)%div)
        
    elif n==9:
        count[n][c]=(find(n-1,c+1)%div)
        
    else:
        count[n][c]=((find(n-1,c+1)%div+find(n+1,c+1)%div))

    return (count[n][c])


N=int(input())
N-=1
if N==0:
    print(9)
else:
    count=[[0]*(N+1) for _ in range(10)]
    #[a][b] 숫자a가 b번째일 경우 경우의 수

    for i in range(1,10):
        find(i,1)

    answer=0
    for i in range(1,10): 
        answer+=(count[i][1])



    print(answer%div)
