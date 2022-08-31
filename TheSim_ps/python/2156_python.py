import sys
input = lambda : sys.stdin.readline().rstrip()


N=int(input()) #포도주 갯수
grape=[]
for i in range(N): #포도주 양 입력
    grape.append(int(input()))

value=[0]*N #포도주 더한 값 저장 리스트
value[0]=grape[0] #첫번째 값은 첫번째 포도주양 저장
if N>=2: #두번째는 첫번째+두번째가 가장 큰값이므로 저장
    value[1]= grape[0]+grape[1] 
if N>=3: #세번째는 첫번째 또는 두번째 값과 더한값 또는 첫번째 두번째를 더한값중 큰값을 저장
    value[2]=max(grape[1]+grape[2],grape[0]+grape[2],grape[0]+grape[1])

for A in range(3,N): #점차 더해가면서 최종값 출력
#현재값과 이전값과 3번째전에 모든 값을 더한값, 현재값과 두번째전에 모든 값을 더한 값, 이전 모든값을 더한 값중 가장 큰 값 찾음
    value[A]=max(value[A-3]+grape[A-1]+grape[A],value[A-2]+grape[A],value[A-1])

print(max(value)) #가장 큰 값 출력
#print(value)