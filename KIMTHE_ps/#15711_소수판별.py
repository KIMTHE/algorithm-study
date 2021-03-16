import sys, math, heapq 
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = int(1e9) #10억 

T = int(input())
testcase = []

for _ in range(T):
    a,b = map(int,input().split()) 
    testcase.append(a+b)

#a+b의 최대값 : 4 0000 0000 0000 -> 메모리초과
# 여기에 제곱근을 하면 : 200 0000
# 소수판별 알고리즘에서, 그 수의 제곱근까지만 나누어보면 된다.
# 에라토스테네스의 체 알고리즘에서 200만까지 검사

max_n = 2000000

nums = [True]*(max_n+1)
nums[1] = False

for i in range(2,int(math.sqrt(max_n))+1):
    if nums[i] == False : continue

    j = 2
    while i*j <= max_n :
        nums[i*j] = False 
        j += 1


#a+b가 짝수이면, 골드바흐의 정리에 의해 YES
#홀수이면, 2+n으로 나뉘고, n이 소수인지, 소수판별 알고리즘 사용
for n in testcase:

    if n < 4:
        print('NO')
        continue

    elif n >= 4 and n%2 == 0:
        print('YES')
        continue

    elif n%2 != 0 :
        n -= 2


    m = int(math.sqrt(n))
    if m>2000000 : m = 2000000

    check = 1
    for i in range(2,m+1) :
        if nums[i] == True :
            if n % i == 0 :
                check = 0
                break
    
    if check == 1: print('YES')
    else : print('NO')
