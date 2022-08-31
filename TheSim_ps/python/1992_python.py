import sys
input = lambda : sys.stdin.readline().rstrip()


def iterator(x1,y1,x2,y2): #분할 함수
    
    check=confirm(x1,y1,x2,y2)

    if check: #하나의 값이 되면
        return check
    
    else: #분할 해야 할 때
        a=iterator(x1,y1,(x1+x2)//2,(y1+y2)//2) #왼쪽위
        b=iterator((x1+x2)//2,y1,x2,(y1+y2)//2) #오른쪽위
        c=iterator(x1,(y1+y2)//2,(x1+x2)//2,y2) #왼쪽아래
        d=iterator((x1+x2)//2,(y1+y2)//2,x2,y2) #오른쪽아래
        return "("+a+b+c+d+")"

def confirm(x1,y1,x2,y2): #모두 0or 1로 되어 있는지 확인 함수
    temp=tree[y1][x1]
    check=True
    for i in range(y1,y2):
        if check:
            for j in range(x1,x2):
                if temp!=tree[i][j]:
                    check=False
                    break
        else:
            break
    
    if check:
        return temp
    else:
        return False


N=int(input())

tree=[]
for i in range(N):
    temp=list((input()))
    tree.append(temp)

print(iterator(0,0,N,N))
