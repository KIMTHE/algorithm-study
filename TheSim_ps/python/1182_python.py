import sys
input = lambda : sys.stdin.readline().rstrip()


N=list(map(int,input().split(' '))) #정수의 개수N과 정수 S
integer = list(map(int,input().split(' '))) #정수 값 입력


count=0 # 부분수열 갯수
sum=0 #더한 값

def dfs(i,sum):
    global count

    if i>=N[0]:
        return

    sum+=integer[i]
    if N[1]==sum:
        count+=1
    dfs(i+1,sum-integer[i]) #값을 포함하지 않은 값
    dfs(i+1,sum)

dfs(0,0)

print(count)
