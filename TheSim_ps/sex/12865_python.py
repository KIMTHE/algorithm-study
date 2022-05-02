import sys
input=lambda : sys.stdin.readline().rstrip()

N,K=map(int,input().split())

back=[]
for i in range(N):
    back.append(list(map(int,input().split())))

back.sort(key=lambda x: -x[1])
answer=[[0]*(K+1) for i in range(N)]
K_value=K

for i in range(N): #갯수
    for j in range(K+1): #무게
        #물건을 넣지 못할 때
        if back[i][0]>j:
            answer[i][j]=answer[i-1][j]
        #물건을 넣을 때
        else:
            answer[i][j]=max(answer[i-1][j-back[i][0]]+back[i][1],answer[i-1][j]) #이전값+현재 넣는 가치, 이전값

print(answer[-1][-1])

