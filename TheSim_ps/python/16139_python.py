import sys
input = lambda : sys.stdin.readline().rstrip()

S=input()
N=int(input())

answer=[[0]*26 for _ in range(len(S)+1)]

for i in range(len(S)):
    answer[i]=answer[i-1][:]
    answer[i][ord(S[i])-97]+=1

for i in range(N):
    value=list(input().split())
    a=ord(value[0])-97
    l=int(value[1])-1
    r=int(value[2])
    print(answer[r][a]-answer[l][a])
    

    
    