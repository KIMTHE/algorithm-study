import sys
input = lambda : sys.stdin.readline().rstrip()

N=list(map(int,input().split()))

S={}
for i in range(N[0]):
    a=input()
    S[a]=''


M=[]
for i in range(N[1]):
    M.append(input())

count=0
for i in range(N[1]):
        if M[i] in S:
            count+=1

print(count)