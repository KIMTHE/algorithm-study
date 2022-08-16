import sys
input = lambda : sys.stdin.readline().rstrip()

A=input()
B=input()

A=list(A)
B=list(B)

output=[[0]*(len(A)+1)for i in range(len(B)+1)]


for i in range(len(A)):
    for j in range(len(B)):
        if A[i]==B[j]:
            output[j+1][i+1]=output[j][i]+1
        else:
            output[j+1][i+1]=max(output[j][i+1],output[j+1][i])

print(output[-1][-1])

#for i in range(len(A)+1):
 #   for j in range(len(B)+1):
  #     print(output[j][i],end=' ')
   # print()