import sys
from collections import deque 
from itertools import combinations, product
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

chess = [0]*(n+1)
result = 0

def check_queen(row,col):
    global chess

    for i in range(1,row):
        if chess[i] == col or abs(i-row) == abs(chess[i]-col):
            return False

    chess[row]  = col
    return True

row = 1
col = 1

while True:
    back = 1
    
    for j in range(col,n+1):

        if check_queen(row,j):
            if row == n : 
                result += 1
            else:
                row += 1
                col = 1
                back = 0
                break
        
    if row == 1:
        break
    if back == 1:
        row -= 1
        col = chess[row]+1

print(result)