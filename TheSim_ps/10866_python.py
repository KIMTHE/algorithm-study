import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

stack=[]

for i in range(N):
    command=input()
    a=list(command.split(' '))
    
    if a[0]=="push_front":
        stack.insert(0,int(a[1]))
    elif a[0] == "push_back":
        stack.append(int(a[1]))
    elif command == "pop_front":
        if not stack: 
            print(-1)
            continue

        print(stack[0])
        stack.pop(0)
    elif command == "pop_back":
        if not stack: 
            print(-1)
            continue

        print(stack[-1])
        stack.pop()
        
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
