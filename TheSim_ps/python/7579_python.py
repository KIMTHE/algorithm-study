import sys
input = lambda : sys.stdin.readline().rstrip()

N,M = map(int,input().split())

activate=list(map(int,input().split())) #활성화
disable=list(map(int,input().split())) #비활성화

ans=sum(disable)+1 #비용은 전체비용합 + 1
answer = [[0 for _ in range(N)] for _ in range(ans)]
#answer[j][i]는 i번째 app의 j비용일때 최대 바이트수

#각 인덱스마다 해당 비용의 최대 바이트 수를 저장한다.
for i in range(N): #전체 인덱스 수
    for j in range(ans): # 전체 비용 수
        if  disable[i]<=j: #비용이 같거나 작으면 들어갈 수 있음
            #이전 인덱스의 바이트값, 이전 인덱스에서 나의 비용만큼 다른 바이트를 뺀 최댓값 + 나의 바이트 값
            # 즉, 현재 바이트 값을 넣지 않은 값, 넣은 값을 비교해서 더 큰 값을 넣는다. 
            answer[j][i]= max(answer[j][i-1], answer[j-disable[i]][i-1]+activate[i])
        else: #비용이 더 크면 들어갈수 없으므로 이전 바이트 값을 넣는다.
             answer[j][i]=answer[j][i-1]

for i in range(len(answer)):
    if M <= max(answer[i]): #비용 순으로 순회하여 해당 비용에 원하는 값을 얻었으면 해당 비용 출력
        print(i)
        break
