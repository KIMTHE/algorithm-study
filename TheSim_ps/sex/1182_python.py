import sys
input = lambda : sys.stdin.readline().rstrip()


N=list(map(int,input().split(' '))) #정수의 개수N과 정수 S
integer = list(map(int,input().split(' '))) #정수 값 입력

count=0 #부분 수열 갯수
result=0

if N[1]==0:
    a=1

def dfs(start,depth):
    
    global result
    global integer
    global N
    global a
    global count
    S=N[1]

    if a==1:
     a=0
     count-=1
    else:
        if result==S:
         count+=1
         return

    for i in range(start,len(integer)):
        result+=integer[i]
        dfs(i+1,depth+1)

   
    
dfs(0,0)

print(count)