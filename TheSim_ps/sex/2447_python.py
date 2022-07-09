import sys
input = lambda : sys.stdin.readline().rstrip()

def find(N):
    if N==1:
        return ["*"]

    value=find(N//3)
    answer=[]
    #처음에 N이 3일 경우 * 값이 value에 저장된다. 
    #그러면 ***, * *, *** 값이 저장되고
    # 9일 경우에는 [ ***, * *, ***] 이 3개가 반복되며 두번째에 빈칸 곱하기 N//3을 더해 빈칸을 만들어준다.
    # 즉, 9일 경우에는 3일 경우에 패턴을 3번 반복 27일 경우에는 9의 패턴을 3번 반복한다.
    for i in value: #각 for문은 가로 패턴 하나의 값을 저장한다.
        answer.append(i*3) 
    for i in value: 
        answer.append(i+" "*(N//3)+i)
    for i in value:
        answer.append(i*3)
    return answer

N=int(input())

temp=find(N)

for i in temp:
    print(i)



    