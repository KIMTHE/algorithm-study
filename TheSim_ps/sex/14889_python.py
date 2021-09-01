import sys
input = lambda : sys.stdin.readline().rstrip()
import itertools

N=int(input())
soccer= [list(map(int, input().split())) for _ in range(N)]
num=[i for i in range(N)] 

a=[]
for team in list(itertools.combinations(num, N//2)):
    a.append(team)

answer=10000
for k in range(len(a)//2):
    v1=0 #a값
    v2=0 #b값   
    for i in (a[k]):
        for j in (a[k]):
            v1+=soccer[int(i)-1][int(j)-1]
            
    b=list(set(num)-set(a[k])) #나머지 수
    
    for i in b:
        for j in b:
            v2+=soccer[int(i)-1][int(j)-1]

    answer=min(answer,abs(v1-v2))
        
print(answer)