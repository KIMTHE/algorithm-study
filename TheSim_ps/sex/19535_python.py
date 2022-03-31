import sys
input = lambda : sys.stdin.readline().rstrip()

def find(M): #ㄷ 구하기 함수
    global d_num # ㄷ 총 갯수

    for i in tree[M-1]: # M노드에 연결된 값 전부 비교
        if M<i: # 중복을 제거 하기 위해 M보다 큰 값만 비교
            d_num+=((len(tree[M-1])-1)*(len(tree[i-1])-1)) #M노드의 자식과 M노드와 연결된 값 자식 노드를 곱하면 4개의 연결이 이루어진다

N=int(input())

tree=[[]for i in range(N)]

for i in range(N-1):
    a,b=map(int,input().split())
    tree[a-1].append(b)
    tree[b-1].append(a)

g_num=0 #ㅈ의 총 갯수
d_num=0 #ㄷ의 총 갯수

for i in range(N):#ㅈ 구하기
    a=len(tree[i])
    if a>=3: #aC3의 조합 공식을 이용 a개중 3개를 선택하는 경우의 수
        g_num+=(a*(a-1)*(a-2))//6
    
for i in range(1,N+1): #ㄷ구하기
    find(i)

if d_num>g_num*3:
    print('D')
elif d_num<g_num*3:
    print('G')
else:
    print('DUDUDUNGA')
