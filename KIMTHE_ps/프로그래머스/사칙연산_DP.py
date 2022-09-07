import sys, math, heapq,copy,itertools #수학연산, 우선순위큐, 순열조합
from collections import deque #queue를 구현하는 덱
from copy import deepcopy #깊은복사
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

def solution(arr):
    pre_max = 0 #이전 '-'까지 최대값
    pre_min = 0 #이전 '-'까지 최소값
    tmp_sum = 0 # '+' 만날때마다, 임시 합 
    
    #거꾸로 탐색
    for i in range(len(arr)-1,0,-2):
        oper = arr[i-1]
        num = int(arr[i])
        
        if oper == '+' :
            tmp_sum += num
            continue
            
        # 최소값 구하기
        case1 = -1 * (num + tmp_sum + pre_max) #'-'가 식 전체에 영향
        case2 = -1 * (num + tmp_sum) + pre_min #'-'가 이전 '-'까지 영향
        case3 = -1 * num + tmp_sum + pre_min #'-'가 앞에 숫자에만 영향
        min_case = [case1,case2,case3]
    
        # 최대값 구하기
        case1 = -1 * (num + tmp_sum + pre_min) #'-'가 식 전체에 영향
        case2 = -1 * (num + tmp_sum) + pre_max #'-'가 이전 '-'까지 영향
        case3 = -1 * num + tmp_sum + pre_max #'-'가 앞에 숫자에만 영향
        max_case = [case1,case2,case3]
        
        tmp_sum = 0
        pre_min = min(min_case)
        pre_max = max(max_case)
    
    return int(arr[0])+pre_max+tmp_sum


