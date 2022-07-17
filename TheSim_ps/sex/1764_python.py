import sys
input = lambda : sys.stdin.readline().rstrip()

N,M=map(int,input().split())

hear={}
for i in range(N):
    hear[input()]='1'

see={}
for i in range(M):
    see[input()]='1'

answer=[]
for i in hear.keys():
    if i in see:
        answer.append(i)

# set을 이용해서 answer=sorted(list(hear & see))로 해결할 수 있다.

print(len(answer))
answer.sort()
for i in answer:
    print(i)