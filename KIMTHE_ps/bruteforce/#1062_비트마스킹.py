import sys, math, heapq,copy,itertools #수학연산, 우선순위큐, 순열조합
from collections import deque #queue를 구현하는 덱
from copy import deepcopy #깊은복사
from bisect import bisect_left,bisect_right #이진탐색
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = math.inf

n,k = map(int,input().split())
words = [input() for _ in range(n)]
set_cpn = [set(list(w))-set(list("antatica"))  for w in words] #단어를 필수문자 빼고 구성하는 문자 집합

bin_dict = {} #필수문자를 뺀 각 알파벳에 비트를 부여
for i,c in enumerate(list("bdefghjklmopqrsuvwxyz")):
    bin_dict[c] = 1 << i

if k < 5: # k가 5 미만이라면 어떤 단어도 만들 수 없음.
    print(0)
    exit(0)

bin_words = [] #필요한 알파벳에 따라서 각 문자를 비트로 변환
for cpn in set_cpn:
    tmp = 0
    for c in cpn: tmp |= bin_dict[c]

    bin_words.append(tmp)

#k개의 알파벳을 고르는 경우의수를 모두 구함 - 바로 비트로 변환
cases = list(itertools.combinations(bin_dict.values(),k-5))

answer = 0
for case in cases:
    case_bit = sum(case)
    tmp = 0

    for word_bit in bin_words:
        if word_bit == word_bit & case_bit:  #해당 단어를 만들수있는지 판별
            tmp+= 1

    answer = max(answer,tmp) #모든 경우중 최대값이 정답

print(answer)



