import sys
input = lambda : sys.stdin.readline().rstrip()


N=int(input())
num=[0] #숫자가 들어간 배열

def insert_sort(x):
    num.append(x)

    i=len(num)-1
    while i>1:
        if num[i]<num[i//2]:
            num[i],num[i//2]=num[i//2],num[i] # 값 교환
            i=i//2
        else:
            break

    
def delete_sort():
    num[1],num[-1]=num[-1],num[1]
    print(num[-1])
    num.pop()

    i=1
    
    while True:
        value=i
        left=i*2
        right=(i*2)+1
        if left<len(num) and num[i]>num[left]:
            i=left
        if right<len(num) and num[i]>num[right]:
            i=right
        
        if i!=value: #작은 값을 왼쪽으로
            num[i],num[value]=num[value],num[i]
            
        else:
            break

for i in range(N):
    x=int(input())
    
    if x==0:
        if len(num)==1:
            print(0)
        else:
            delete_sort()

    else:
        insert_sort(x)
    
    #print(num)