import sys
input = lambda : sys.stdin.readline().rstrip()

value=[]
while True:
    temp=input()
    if temp=='.':
        break
    
    else:
        value.append(temp)

for i in value:
    temp=list(i)
    stack=[]
    for j in temp:
        if j=='(' or j==')' or j=='[' or j==']':
            if j==')' and stack and stack[-1]=='(':
                stack.pop()
            elif j==']' and stack and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(j)
    if stack:
        print('no')
    else:
        print('yes')

     

