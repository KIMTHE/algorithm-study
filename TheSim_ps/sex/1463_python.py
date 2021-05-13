import sys
input = lambda : sys.stdin.readline().rstrip()

X = int(input())
count=0 #연산 사용 최솟값
result=[X]

while True:
    if X==1:
        break
    for i in range(len(result)):
        result.append(result[i]-1)
        if result[i]%3==0:
            result.append(result[i]/3)
        if result[i]%2==0:
            result.append(result[i]/2) 
        result = set(result)#중복제거
        result = list(result)

    count+=1
    if min(result)==1.0:
        break
   

print(count)