import sys
input = lambda : sys.stdin.readline().rstrip()

value = [[1,0],[0,1],[1,1]]

def find(a):
    if a>=len(value):
        for i in range(len(value),a+1):
            value.append([value[i-1][0]+value[i-2][0],value[i-1][1]+value[i-2][1]])

    print(value[a][0],value[a][1])


N=int(input())
for i in range(N):
    num=int(input())
    find(num)