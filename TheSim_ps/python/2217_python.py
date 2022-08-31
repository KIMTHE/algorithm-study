import sys
input = lambda : sys.stdin.readline().rstrip()

N= int(input())

rope=[]
for i in range(N):
    rope.append(int(input()))

rope.sort()

value=[]
for i in range(len(rope)):
    value.append(rope[i]*(len(rope)-i))

print(max(value))

# w= (로프 감당 무게)*k(로프 갯수)  (5,10,15)*2  15/3=5  