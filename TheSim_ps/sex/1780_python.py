import sys
input = lambda : sys.stdin.readline().rstrip()

def find(paper,N):
    global A,B,C
    visit=0
    temp=paper[0][0]
    for i in range(len(paper)):
        if visit==1:
            break
        for j in range(len(paper)):
            if temp!=paper[i][j]:
                visit=1
                break
            else:
                temp=paper[i][j]
        
    if visit==0: #해당 범위내의 값이 전부 같은 값이라면 갯수 리턴
        if temp==-1:
            A+=1
        elif temp==0:
            B+=1
        else:
            C+=1
        return
    else: #아니라면 9개로 분할
        
        for i in range(1,4):
            for j in range(1,4):
                value=[]
                for k in range(N//3*(i-1),N//3*i):
                    temp=[]
                    for z in range(N//3*(j-1),N//3*j):
                        temp.append(paper[k][z])
                    value.append(temp)
                find(value,N//3)


N=int(input())

paper=[]
for i in range(N):
    paper.append(list(map(int,input().split())))
A=0 #-1
B=0 #0
C=0 #1
find(paper,N)

print(A)
print(B)
print(C)
