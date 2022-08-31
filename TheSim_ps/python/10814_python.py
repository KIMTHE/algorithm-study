import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

person=[]
for i in range(N):
    temp=[]
    temp.extend(list(input().split()))
    temp.append(str(i))
    person.append(temp)

person.sort(key=lambda x:(int(x[0]),int(x[2])))

for i in person:
    print(i[0],i[1])
