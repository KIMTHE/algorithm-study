import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
count = 0
stack = []
result = []
no_message=True

for i in range(0,n):
    x = int(input())

    while count < x:
      count += 1
      stack.append(count)
      result.append("+")

    if stack[-1]==x:
        stack.pop()
        result.append("-")
    else:
        no_message = False
        break #a clean exit without any errors / problems

if no_message==False:
    print("NO")
else:
    print("\n".join(result))
       
