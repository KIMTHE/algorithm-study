import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
card = list(map(int,input().split(' ')))
value=[[0]*2 for i in range(len(card))]

cost=[0]*N #카드 값 나눠서 가장 큰값저장
for i in range(N):
    cost[i]=card[i] #첫번재 카드

cost[1]=max(card[0]*2,card[1]) #두번째 카드

for i in range(2,N):
    for j in range(i):
        cost[i]=max(cost[i],cost[j]+cost[i-j-1])

print(cost[N-1])

