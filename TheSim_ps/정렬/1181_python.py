import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
S=[]

for i in range(N):
   S.append(input())

S=list(set(S))

S.sort(key=lambda x:(len(x),x))

for i in range(len(S)):
    print(S[i]) 