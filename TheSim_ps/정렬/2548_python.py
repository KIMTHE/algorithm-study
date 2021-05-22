import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
nature=list(map(int,input().split()))

nature.sort()

output=[0]*N

for i in range(len(nature)):
    for j in range(len(nature)):
        output[i]+=abs(nature[i]-nature[j])

mini=sorted(output)

for i in range(N):
    if output[i]==mini[0]:
        print(nature[i])
        break
