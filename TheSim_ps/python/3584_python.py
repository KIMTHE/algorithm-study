import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

for i in range(N):
    M=int(input())
    node=[[]*(M+1) for i in range(M+1)]
    for j in range(M-1):
        a=list(map(int,input().split()))
        node[a[0]].append(a[1])
    
    output=list(map(int,input().split()))
    
    k=0
    a=output[0]
    test1=[] #조상 조사
    test1.append(a)
    while True:
        if k>M:
            break
        if a in node[k]:
            test1.append(k)
            a=k
            k=0
            continue
        k+=1
    
    k=0
    a=output[1]
    test2=[] #조상 조사
    test2.append(a)
    while True:
        if k>M:
            break
        if a in node[k]:
            test2.append(k)
            a=k
            k=0
            continue
        k+=1
    
    reversed(test1)
    reversed(test2)

    a=len(test1)-1
    b=len(test2)-1
    while test1[a]==test2[b]:
        a-=1
        b-=1
    
    print(test1[a+1])