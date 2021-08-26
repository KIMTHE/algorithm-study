import sys
input = lambda : sys.stdin.readline().rstrip()

def find(chess,full,N):
    count=0

    if N==full: #모든 말을 채웠을 경우
        return 1
    
    for i in range(N):
        chess[full]=(i)

        for j in range(full):
            if chess[full]==chess[j] or (chess[full]-(full-j))==chess[j] or (chess[full]+(full-j))==chess[j]:
                break
        else:
            count+=find(chess,full+1,N)
    
    return count

N=input()
N=int(N)
count=0
chess=[0]*N

print(find(chess,0,N))


