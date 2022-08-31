import sys
input = lambda : sys.stdin.readline().rstrip()

def hanoi(N,start,end): #start에서 end로 가는 경우의 수, N개의 수는 a에 있음
    if N==1:
        a=[[start,end]]
        return a

    value=[]
    #하노이는 1,2,3개의 판이 있으므로 총 6개이다
    #그래서 6개에서 시작과 도착부분을 빼면 중간 지점이 나온다.
    #예를 들어 1->3 으로가려면
    # 이전 단계의 1->2 + 1->3 + 이전단계의 2->3을 더해야 한다.
    value.extend(hanoi(N-1,start,6-start-end)) 
    value.append([start,end])
    value.extend(hanoi(N-1,6-start-end,end))
    return value

N=int(input())

answer=(hanoi(N,1,3))
print(len(answer))
for i,j in answer:
    print(i,j)