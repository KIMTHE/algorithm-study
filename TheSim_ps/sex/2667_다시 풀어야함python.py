import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())

house=[]

for i in range(N):
    a=input()
    a=list(a)
    house.append(a)

def find(start,end,value): #2차원 리스트 시작과 끝점 입력
    
    go(start,end)
    

    if house[start][end]!='0':
        house[start][end]=value

        find(start+1,end,value) #아래
        find(start,end+1,value)#오른쪽
        find(start,end-1,value)#왼쪽


def go(start,end):
    if house[start][end] == '0': #0일시 빈집이므로 다음집 탐색
        end+=1

        if end==N: #제일 오른쪽이면 아랫집
            if start==N: #제일 밑에 집이면 종료
                return
            end=0
            start+=1
        go(start,end)
    else:
        return house[start][end]

find(0,0,2)

print(house)