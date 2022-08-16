import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
road=list(map(int,input().split())) #도로 길이
oil = list(map(int,input().split()))#기름값

value=0 #현재 기름값
i=0 #첫도시 기름값
value=oil[i] #첫번째 도시 기름 값
answer=0 #최종 값
num=0 #자동차 이동 거리
#num = road[0] # 첫번재 도시에서 두번째 도시 거리

while True:
    i+=1
    num+=road[i-1]

    if i==N-1:
        answer+= (num*value)
        break

    if value>oil[i]: #다음 도시 기름값이 더 싸다면
        
        answer+= (num*value) #이전 도시에서 다음 도시까지 산 기름값
        value=oil[i] #해당 도시에서 기름 구매
        num=0
    
        
print(answer)