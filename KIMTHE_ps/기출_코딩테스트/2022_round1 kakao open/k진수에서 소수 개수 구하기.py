import sys, math, heapq,copy,itertools #수학연산, 우선순위큐, 순열조합
from collections import deque #queue를 구현하는 덱
from copy import deepcopy #깊은복사
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

def solution(n, k):
    
    #k진수로 변환
    knum = []
    while n>0:
        knum.append(str(n%k))
        n = n//k
    knum.reverse()
    knum = ''.join(knum)

    #조건에 맞는 숫자
    number = []
    tmp = ""
    for n in knum:
        if n!='0':
            tmp += n
        
        elif n=='0' and tmp!="1" and tmp!="":
            number.append(int(tmp))
            tmp = ""
            
        else:
            tmp = ""
            
    if tmp!="1" and tmp!="":
        number.append(int(tmp,10))
    
    if len(number) == 0:
        return 0
    
    number.sort()
    number.reverse()
    end = int(max(number)**0.5)
    answer = 0
    print(number)
    #제곱근 이용한 소수판별
    for i in range(2,end+1):
        next_num = []
        
        for n in number:
            if i>int(n**0.5) : 
                answer += 1
                continue
                
            elif n%i == 0:
                continue
                
            else :
                next_num.append(n)
            
        number = next_num
    
    return answer+len(number)


