import sys
input = lambda : sys.stdin.readline().rstrip()

def find():
    check=0
    for z in range(9):
        if 0 not in N[z]:
            check+=1

    if check==9:
        for a in range(9): #스도쿠 값 비교 세로
            for b in range(9): #가로
                print(N[a][b],end=' ')
            print()
        exit()

    #for j in range(q,9): #스도쿠 값 비교 세로
       #for k in range(w,9): #가로
    for j,k in value:  
        if N[j][k]==0:
                for i in range(1,10):
                    a=k//3 #가로
                    b=j//3 #세로
                    check=0
                    if i in N[j]: #가로 
                        check=1
                    if check==0: 
                        for q in range(b*3,(b+1)*3): #3*3
                                for w in range(a*3,(a+1)*3):
                                    if i == N[q][w]:
                                        check=1
                                        break
                                    
                    if check==0:
                        for w in range(9): #세로
                                if i == N[w][k]:
                                    check=1
                                    break
                                
                        
                    if check==0:
                        N[j][k]=i
                        find()
                        N[j][k]=0         
                else:
                    return                     
                            
              
N=[]
for i in range(9):
    N.append(list(map(int,input().split())))
value=[]
for j in range(9): #스도쿠 값 비교 세로
    for k in range(9): #가로
        if N[j][k]==0:
            value.append([j,k])    
find()
    
    