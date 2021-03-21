import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

stack=[]

for i in range(N):
    command=input()
    
    if command=="pop":
        if not stack: 
            print(-1)
            continue

        print(stack[0])
        stack.pop(0)
        

    elif command =="size":
        print(len(stack))

    elif command == "empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)

    elif command == "front":
        if not stack:
            print(-1)
            continue
        print(stack[0])
    
    elif command == "back":
        if not stack:
            print(-1)
            continue
        print(stack[-1])

    else:
        a,b=command.split(' ')
        stack.append(int(b))