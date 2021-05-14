import sys
input = lambda : sys.stdin.readline().rstrip()

N,K=input().split()
N=int(N)
K=int(K)

time=0 # 찾은 시간

value=[]

#def find(N):
while True: 
    #global time
    time+=1
    prime=0 #1이면 값 찾음

    for i in range(len(value)):
        if value[i]==K:
            prime=1
            break
        elif value[i]>100000:
            prime=1

    if prime==1:
        break

    value.append(N-1)
    value.append(N*2)
    value.append(N+1)
    

#find(N)

print(time)


"""while True:
    if N>K:
        N-=1
        time+=1

    elif N==K:
        break

    else:
   """     