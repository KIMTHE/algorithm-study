import sys
input = sys.stdin.readline

def find(i): #i는 열 j는 행을 의미
    if i==N: #마지막 열까지 Q가 다 찼으므로 경우의 수 +1
        global count
        count+=1
        return

    else:
        for j in range(N): #모든 행을 반복
            if not (a[j] or b[i+j] or c[i-j+N-1]): #세로줄이나 대각선에 값이 없으면 Q를 둘 수 있다
                a[j] = b[i+j] =  c[i-j+N-1] = True #Q를 뒀으니 있다는 True 표시
                find(i+1) # 다음 열에 Q 위치 찾기
                a[j] = b[i+j] =  c[i-j+N-1] = False # 원하는 값이 없으므로 Q를 둔 표시를 지운다
    return    


N=int(input()) #체스 판의 크기

visit=[0]*N #Q를 두는 위치 저장 같은 열에는 둘 수 없으므로 행만 생각한다
count=0 # 경우의 수
a,b,c = [False]*N,[False]*(2*N-1),[False]*(2*N-1) #미리 세로줄, 대각선의 배열을 만들어둠
find(0)
print(count)
