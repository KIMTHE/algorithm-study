import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

meet=[]

for i in range(N):
    a,b = input().split()
    meet.append([int(a),int(b)])

meet=sorted(meet,key=lambda a:a[0])
meet=sorted(meet,key=lambda a:a[1])

last=0
count=0

for i,j in meet:
    if i>=last:
        count+=1
        last=j

print(count)