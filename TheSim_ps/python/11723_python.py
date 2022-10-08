# import sys
# input = lambda : sys.stdin.readline().rstrip()

# def add(x,num):
#     num=num|(1<<x)
#     return num

# def remove(x,num):
#     num=num&~(1<<x)
#     return num

# def check(x,num):
#     if(num&(1<<x)):
#         sys.stdout.write(1+'\n')
#     else:
#         sys.stdout.write(0+'\n')

# def toggle(x,num):
#     num=num^(1<<x)
#     return num

# def all(num):
#     num=num|((1<<21)-1)
#     return num

# def empty(num):
#     num=0
#     return num

# N=int(input())
# num=0
# for _ in range(N):
#     value=input().split()

#     if value[0]=='add':
#         num=add(int(value[1]),num)
#     elif value[0]=='check':
#         check(int(value[1]),num)
#     elif value[0]=='remove':
#         num=remove(int(value[1]),num)
#     elif value[0]=='toggle':
#         num=toggle(int(value[1]),num)
#     elif value[0]=='all':
#         num=all(num)
#     elif value[0]=='empty':
#         num=empty(num)


import sys
#pypy로 하면 print를 사용하면 메모리를 많이 사용함으로 sys.stdout.write를 사용해야 한다.
# https://www.acmicpc.net/blog/view/70
def add(x,num):
    num=num|(1<<x)
    return num

def remove(x,num):
    num=num&~(1<<x)
    return num

def check(x,num):
    if(num&(1<<x)):
        sys.stdout.write('1'+'\n')
    else:
        sys.stdout.write('0'+'\n')

def toggle(x,num):
    num=num^(1<<x)
    return num

def all(num):
    num=num|((1<<21)-1)
    return num

def empty(num):
    num=0
    return num

N=int(sys.stdin.readline().rstrip())
num=0
for _ in range(N):
    value=sys.stdin.readline().rstrip().split()
    if value[0]=='add':
        num=add(int(value[1]),num)
    elif value[0]=='check':
        check(int(value[1]),num)
    elif value[0]=='remove':
        num=remove(int(value[1]),num)
    elif value[0]=='toggle':
        num=toggle(int(value[1]),num)
    elif value[0]=='all':
        num=all(num)
    elif value[0]=='empty':
        num=empty(num)
