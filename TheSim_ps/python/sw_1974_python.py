T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sudoku=[]
    for i in range(9):
        sudoku.append(list(map(int,input().split())))
    
    
    check=1
    for j in range(9):
        num=[0]*10
        for i in range(9):
            num[sudoku[i][j]]+=1
            if num[sudoku[i][j]]>3:
                check=0
                break
            num[sudoku[j][i]]+=1
            if num[sudoku[j][i]]>3:
                check=0
                break
            num[sudoku[(i)//3][(i)%3]]+=1
            if num[sudoku[(i)//3][(i)%3]]>3:
                check=0
                break
    
    print("#"+str(test_case)+" "+str(check))
