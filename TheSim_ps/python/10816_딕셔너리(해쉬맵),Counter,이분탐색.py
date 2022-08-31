"""import sys #try exept와 dict를 이용해서 해결 키와 값을 이용 일반적인 이분법하면 시간초과
input = lambda : sys.stdin.readline().rstrip()
#https://infinitt.tistory.com/288 해설
N = int(input())
a=list(map(int,input().split()))
M = int(input())
b=list(map(int,input().split()))

dic=dict()

for i in a:
    try:
        dic[i]+=1
    except:
        dic[i]=1
for i in b:
    try:
        print(dic[i], end=" ")
    except:
        print(0,end=" ")

"""
#이분탐색  https://chancoding.tistory.com/45 해설
from sys import stdin
_ = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
_ = stdin.readline()
M = map(int,stdin.readline().split())

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        i, j = 1, 1
        while m-i >= start:
            if N[m-i] != N[m]:
                break
            else: i += 1
        while m+j <= end:
            if N[m+j] != N[m]:
                break
            else: j += 1
        return i + j - 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

n_dic = {}
for n in N:
    start = 0
    end = len(N) - 1
    if n not in n_dic:
        n_dic[n] = binary(n, N, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M ))

# Collections 라이브러리의 Counter 함수
from sys import stdin
from collections import Counter
_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

C = Counter(N)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))