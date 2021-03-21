import sys
input = lambda : sys.stdin.readline().rstrip()

#스택 이용

N=input()
cut=list(N)
put=[] #커서 이동시 문자 분열

M=int(input())

for i in range(M):
    command = input()

    if command == "L":
        if not cut:
            continue 
        put.append(cut.pop()) 
    elif command == "D":
        if not put:
            continue
        cut.append(put.pop())
    elif command == "B":
        if not cut:
            continue
        cut.pop()
    else:
        a,b=command.split(' ')
        cut.append(b)
        
cut.extend(put[::-1])
print(''.join(cut))


"""N=input() #리스트 이용
cut=list(N)
print(N)

M=int(input())

mouse = len(cut) #커서의 위치

for i in range(M):
    command = input()

    if command == "L":
        if mouse==0:
            continue
        mouse-=1
      
    elif command == "D":
        if command == len(cut):
           continue
        mouse+=1
       

    elif command == "B":
        if mouse==0:
            continue

        cut.pop(mouse-1)
        mouse-=1

    else:
        a,b=command.split(' ')
        cut.insert(mouse,b)
        mouse+=1

print(''.join(cut))"""