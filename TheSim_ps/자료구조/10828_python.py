import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

stack=[]

for i in range(N):
    command=input()
    
    if command=="pop":
        if not stack: #스택에 값이 없을 때 이렇게 확인
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

    elif command == "top":
        if not stack:
            print(-1)
            continue
        print(stack[-1])

    else:
        a,b=command.split(' ')
        stack.append(int(b))