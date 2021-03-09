import sys
import math
from collections import deque 
from itertools import combinations, product
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
perm = []
len_p = 0

def check_p(perm,len_p):
    max_part = len_p // 2

    for i in range(1,max_part+1):
        tmp1 = perm[len_p-i:len_p]
        tmp2 = perm[len_p-i-i:len_p-i]

        if tmp1 == tmp2:
            return False

    return True

def dfs(perm,len_p) : 
    global n

    if len_p == n:
        for i in perm: print(i,end='')
        return True

    perm.append(0)
    for i in range(1,4):
        perm[-1] = i

        if check_p(perm,len_p+1) == False: continue

        if dfs(perm,len_p+1) == False : perm.pop()
        else : return True

    return False


dfs(perm,len_p)
    
