import sys
input = lambda : sys.stdin.readline().rstrip()

N=list(map(int,input().split()))

circle=[]
for i in range(N[0]):
    circle.append(i+1)

i=0
count=0
answer=[]
while circle:
    if i>=len(circle):
        i=0

    if count==(N[1]-1):
        answer.append(str(circle.pop(i)))
        count=0
        continue
    
    i+=1
    count+=1

print("<", ", ".join(answer), ">", sep='')
