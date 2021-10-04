import sys
input = lambda : sys.stdin.readline().rstrip()

def find(i):

    if i==0: return hap[0]
    if i<0: return 0
    
    if hap[i]!=0:
        return hap[i]
    
    hap[i]=max(stair[i]+stair[i-1]+find(i-3),stair[i]+find(i-2))
    
    return hap[i]



N=int(input())
stair=[]
for i in range(N):
    stair.append(int(input()))

hap=[0]*N
hap[0]=stair[0]



print(find(N-1))
