import sys
input = lambda : sys.stdin.readline().rstrip()

def find(num):
    
    if answer[num]!=-1:
        return answer[num]

    answer[num]=0
    if rule[num]:
        big=0
        for i in rule[num]:
            big=max(find(i),big)
        answer[num]+=big
        answer[num]+=time[num-1]
    else: #이전에 지어야할 건물이 없으면 자기 시간만 계산
        answer[num]=time[num-1]

    return answer[num]

T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    time=list(map(int,input().split()))
    rule=[[] for  i in range(N+1)] #규칙

    for j in range(K):
        a,b=map(int,input().split())
        rule[b].append(a)

    W=int(input())

    answer=[-1]*(N+1) #최종 걸리는 시간 
    
    print(find(W))

    