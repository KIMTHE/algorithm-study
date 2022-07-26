import sys
input = lambda : sys.stdin.readline().rstrip()

N,M = map(int,(input().split()))
num=list(map(int,input().split()))

value=[0]*(N+1) #구간합
count=0 #구간 갯수, 최종 정답
for i in range(1,N+1): #0부터i번째까지 구간합 구하기
    value[i]=num[i-1]+value[i-1]

answer=[[] for _ in range(M)] #M값의 나미저 갯수만큼 크기 할당
for i in range(N+1): #나머지가 같은 값끼리 나눠서 저장
    answer[value[i]%M].append(value[i])

for i in range(M): #같은 나머지 끼리 구간합을 구하면 M으로 나눠떨어진다
    for j in range(len(answer[i])): # 구간합의 갯수 구하기
        count+=j

# value=[0]*(N+1) #구간합
# count=0 #구간 갯수, 최종 정답
# answer=[0]*M #같은 나머지 값을 추가하는 것이 아닌 갯수만 센다
# for i in range(N+1): 
#     value[i]=num[i-1]+value[i-1] #누적합 구하기
#     answer[value[i]%M]+=1 #누적합의 나머지 갯수를 동시에 구하기

# for i in range(M): #조합 공식을 사용해서 나머지 갯수에서 2개의 i,j를 선택하는 경우의 수 nC2를 공식으로 나타내면
#     count+=(answer[i]*(answer[i]-1))//2 #n*(n-1)//2가 된다.

print(count)



