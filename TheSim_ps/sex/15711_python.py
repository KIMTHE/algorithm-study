import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

sosu=[]
for i in range(2,2000000):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        sosu.append(i)

for i in range(N):
    check=0
    a,b=map(int,input().split())

    c=a+b
    
    if c<4:
        print("NO")
        continue
    elif c%2==0:
        print("YES")

    else:
        if (c-2)>2000000:
            for j in sosu:
                if (c-2)%j==0:
                    print("NO")
                    break
            else:
                print("YES")
                
        else:
            if (c-2) in sosu:
                print("YES")
            else:
                print("NO")
        
    

        