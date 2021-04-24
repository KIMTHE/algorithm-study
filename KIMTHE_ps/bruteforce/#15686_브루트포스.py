import sys
import math
from collections import deque 
from itertools import combinations, product
input = lambda : sys.stdin.readline().rstrip()

n,m = map(int,input().split())
city = []
chks = []
houses = []

#치킨집 조합과 집사이의 거리구하기
def distance(chks,house):
    dis = float('inf')

    x2,y2 = house

    for chk in chks:
        x1,y1 = chk
        
        tmp_dis = abs(x1-x2)+abs(y1-y2)

        if dis > tmp_dis : dis = tmp_dis


    return dis

for i in range(n):
    tmp = list(map(int,input().split()))
    city.append(tmp)

    for j in range(n):
        tmp = (i,j)
        if city[i][j] == 1: houses.append(tmp)
        elif city[i][j] == 2 : chks.append(tmp)

result = float('inf')

chks_cases = list(combinations(chks,m))

for chk_case in chks_cases:
    dis_tmp = 0
    for house in houses:
        dis_tmp += distance(chk_case,house)

    if result > dis_tmp : result = dis_tmp

print(result)
        