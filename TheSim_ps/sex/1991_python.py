import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

node={i:[] for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

for i in range(N):
    a=list(map(str,input().split()))
    node[a[0]]+=[a[1],a[2]]

def front(node,i):
    output=[i]
    result=''
    while output:
        a=output.pop()
        result+=a

        if node[a][1]!='.':
            output.append(node[a][1])
        if node[a][0]!='.':
            output.append(node[a][0])
    return result


def mid(node,i):
    output=[i]
    result=''
    
    while output:
        if node[output[-1]][0]!='.' and node[output[-1]][0] not in result:
            output.append(node[output[-1]][0])

        else:
            a=output.pop()
            result+=a
            if node[a][1]!='.':
                output.append(node[a][1])
    return result
        
def behind(node,i):
    output=[i]
    result=''

    while output:
        if node[output[-1]][0]!='.' and node[output[-1]][0] not in result:
            output.append(node[output[-1]][0])
        elif node[output[-1]][1]!='.' and node[output[-1]][1] not in result:
            output.append(node[output[-1]][1])
        else:
            a=output.pop()
            result+=a

    return result
        
print(front(node,'A'))
print(mid(node,'A'))
print(behind(node,'A'))


"""
N=int(input())

node=[0]*28

def front(i):
    if i>27:
        return
    if node[i]!=0:  
        print(node[i],end='')
    front(i*2)
    front(i*2+1)

def mid(i):
    if i>27:
        return

    mid(i*2)
    if node[i]!=0:
        print(node[i],end='')
    mid(i*2+1)

def last(i):
    if i>27:
        return

    last(i*2)
    last(i*2+1)
    if node[i]!=0:
        print(node[i],end='')
    
front(1)
print()
mid(1)
print()
last(1)

"""  
"""
a=list(map(str,input().split()))
node[1]=a[0]
if a[1]!='.':
    node[2]=a[1]
if a[2]!='.':
    node[3]=a[2]
b=['.','.','.']
for i in range(N-1):
    a=list(map(str,input().split()))
    prime=0 #값이 있는지 없는 지 확인
    
    for j in range(len(node)):
        if (j*2)>27:
            break
        if node[j]==a[0]:
            prime=1
            if a[1]!='.':
                if b[0]==a[1]:
                    if b[1]!='.':
                        node[(j*2)*2]=b[1]
                    if b[2]!='.':    
                        node[(j*2)*2+1]=b[2]
                        b=['.','.','.']
                node[j*2]=a[1]
            if a[2]!='.':
                if b[0]==a[2]:
                    if b[1]!='.':
                        node[(j*2)*2]=b[1]
                    if b[2]!='.':    
                        node[(j*2)*2+1]=b[2]
                        b=['.','.','.']
                node[j*2+1]=a[2]
    if prime==0:
        b=a
print(node)
"""