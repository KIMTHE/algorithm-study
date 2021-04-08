import sys
import math
from collections import deque 
from itertools import combinations, product
input = lambda : sys.stdin.readline().rstrip()

def testcase(n,nums) :

    check = 0
    for s in range(2,n+1) :
        if nums[s] == False or s%2 == 0 : continue

        e = n-s

        if nums[e] == True and e%2 != 0 :
            check = 1
            break        

    if check == 1:
        print(str(n),'=',str(s),'+',str(e))
    else : print("Goldbach's conjecture is wrong.")


inpu = []
while True:
    n = int(input())
    if n == 0: break

    inpu.append(n)

max_n = max(inpu)
nums = [True] * (max_n+1)
nums[1] = False

for i in range(2,int(math.sqrt(max_n))+1):
    if nums[i] == False : continue

    j = 2
    while i*j<=max_n :
        nums[i*j] = False
        j += 1


for n in inpu:
    testcase(n,nums)