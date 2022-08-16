import sys
input = lambda : sys.stdin.readline().rstrip()

N=input()
A = list(map(int,input().split()))

count=[0]*len(A)
count[0]=1

for i in range(1,len(A)):
    big=-1 #가장 큰값

    for j in range(i):
        if count[big]<=count[j]: # 카운트 값보다 작은지
            if A[i]>A[j]: #나보다 작은 값
                big=j
    if big!=-1:
        count[i]=count[big]+1
    else:
        count[i]=1
#print(count)
print(max(count))