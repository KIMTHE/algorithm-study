import sys

arr = list(sys.stdin.readline().split())
N = arr[0]
K = int(arr[1])
M = len(N)
if M < 2: #자리수가 1개면 -1을 출력하고 종료
    print(-1)
    sys.exit()

N = list(map(int,N)) 
N1 = list(map(int,N)) # 최대값을 만들기 위한 리스트
N1.sort(reverse=True) # 최대값

result =[]

def change_index(arr,a,b):
    temp = arr[b]
    arr[b] = arr[a]
    arr[a] = temp
    return arr

def arrToNum(arr):
    arr.reverse()
    result = 0
    n = 0
    for i in arr:
        result += i*(10**n)
        n+=1
    return result
    
def change_dfs(depth, arr):
    if depth == K: #깊이가 K가 되면
        result.append(arrToNum(arr)) #arr를 정수로 바꿔서 결과에 넣어준다.
        return
        
    a = -1
    for i in range(M): #전체 자리에 대해
        if arr[i] != N1[i]: #최대값이 아닌 지점에 대해
            a = i #값을 기록하고
            break #멈춘다.
            
    if a == -1: #전부 최대값과 동일하면
        if M != len(set(arr)): #중복을 제거한 값과 전체 자릿수가 다르면
            print(arrToNum(arr)) # 그 값을 출력하고 종료
            sys.exit()
            
        else:
            arr = change_index(arr,M-1,M-2) #맨끝자리(M-1)와 그 다음 자리(M-2)를 바꾼다,
            
            if arr[0] == 0: #바꾸다가 첫째자리가 0이되면 종료
                print(-1)
                sys.exit()
                
            else:
                change_dfs(depth+1,arr)
                return
                
    b_index = []
    
    for i in range(a+1,M):
        if N1[a] == arr[i]: #최대값과 같은 자릿수를
            b_index.append(i) #b_index에 넣어준다.
            
    for i in b_index:
        arr1 = list(map(int,arr))
        change_dfs(depth+1, change_index(arr1,a,i))








change_dfs(0,N)

result_max = 0
for i in result:
    if i > result_max:
        result_max = i
print(result_max)