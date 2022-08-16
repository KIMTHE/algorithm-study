import sys
input = lambda : sys.stdin.readline().rstrip()

#백트레킹 M크기만큼의 배열 하나를 만들어서 수를 입력하고 다채워지면
# 해당 값이 있는지 확인하고 없으면 수열에 추가 
def find(arr):
    global answer
    if len(arr)==M:
        
        a=list(arr)
        answer.append(a)
        return
    
    for i in num:
        arr.append(i)
        find(arr)
        arr.pop()
    
N,M = map(int,input().split())
num=list(map(int,input().split()))

num = set(num)
num=list(num)


answer=[] #해답
arr=[]
find(arr)

answer.sort()
for a in answer:
    #b=" ".join(a)
    print(*a, sep=' ')
