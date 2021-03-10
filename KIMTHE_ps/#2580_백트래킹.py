import sys
import math
from collections import deque 
from itertools import combinations, product
input = lambda : sys.stdin.readline().rstrip()

sdok = [list(map(int, input().split())) for _ in range(9)]

row = [set(i) for i in sdok]
col = []

for i in range(9):
    tmp = []
    for j in range(9):
        tmp.append(sdok[j][i])
    col.append(set(tmp))

blocks = [[] for _ in range(3)]   

for i in range(3):
    for j in range(3):
        tmp = []

        for k in range(i*3,i*3+3):
            for l in range(j*3,j*3+3):
                tmp.append(sdok[k][l])

        blocks[i].append(set(tmp))
blanks = []

for i in range(9):
    for j in range(9):
        if sdok[i][j] == 0:
            tmp = (i,j)
            blanks.append(tmp)

max = len(blanks)

def dfs(idx) :
    global sdok,blanks,row,col,blocks
    global max

    if idx == max : return True 

    x,y = blanks[idx]

    for i in range(1,10):
        if i in row[x]: continue
        if i in col[y]: continue
        if  i in blocks[x//3][y//3] : continue

        sdok[x][y] = i
        row[x].add(i)
        col[y].add(i)
        blocks[x//3][y//3].add(i)


        if dfs(idx+1) : return True
        else :
            sdok[x][y] = 0
            row[x].remove(i)
            col[y].remove(i)
            blocks[x//3][y//3].remove(i)

    
    return False
    

dfs(0)

for i in range(9):
    for j in range(9):
        print(sdok[i][j], end = ' ')
    print()
