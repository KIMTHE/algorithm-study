import sys, math, heapq #수학연산의 math, 우선순위큐에 사용되는 heapq
from collections import deque #queue를 구현하는 덱
from itertools import combinations, product #조합,순열
input = lambda : sys.stdin.readline().rstrip() #입력속도빠르게
INF = int(1e9) #10억 

n,m = map(int,input().split())
tree = list(map(int,input().split()))
max_tree = max(tree)
min_cut = max_tree-m
if min_cut <0 : min_cut = -1

max_cut = min_cut

def b_s(start,end):
    global max_cut

    mid = (start+end)//2

    if start > end : return

    tmp = 0
    for t in tree:
        if t > mid : tmp+= t-mid

    if tmp>=m:
        if mid > max_cut : max_cut = mid
        b_s(mid+1,end)

    else:
        b_s(start,mid-1)

    
b_s(min_cut+1,max_tree)
print(max_cut)