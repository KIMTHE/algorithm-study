import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
H=list(map(int,input().split()))

count=[0]*(1000000+1)

answer=0
for i in H:
    if count[i]>0:
        count[i]-=1
        count[i-1]+=1
    else:
        answer+=1
        count[i-1]+=1


print(answer+1)


""""
count=[]
for i in H:
    if i not in count:
        count.append(i-1)
    else:
        count[count.index(i)]=(i-1)


print(len(count))

"""