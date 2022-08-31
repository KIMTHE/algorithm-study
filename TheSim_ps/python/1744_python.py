import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
num=[]
for i in range(N):
    num.append(int(input()))

num.sort()
positive=[]
negative=num[:]
for i in range(N):
    if num[i]>0:
        positive=num[i:]
        negative=num[:i]
        break

answer=0
value_1=0
value_2=0
while positive:
    value_1=positive.pop()
    if positive:
        value_2=positive.pop()
        answer+=max(value_1*value_2,value_2+value_1)
    else:
        answer+=value_1

value_1=0
value_2=0
negative.sort(reverse=True)
while negative:
    value_1=negative.pop()
    if negative:
        value_2=negative.pop()
        answer+=max(value_1*value_2,value_2+value_1)
    else:
        answer+=value_1
    
print(answer)
    
    

