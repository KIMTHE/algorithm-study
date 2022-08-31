import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
A=list(map(int,input().split()))
A.reverse() #뒤에서 부터확인

answer=[-1]
big=[A[0]]

for i in range(1,len(A)): #입력값을 뒤에서 두번재 부터 확인한다. 맨 뒤의 값은 무조건 -1이므로 -1을 미리 넣고 시작한다.
    while big and A[i]>=big[-1]: #big값이 있고, big의 가장 위의 값이 현재 값보다 작거나 같으면 큰값이 나올 때까지 pop한다.
        big.pop()
    
    if len(big)==0: #만약 전부다 pop해서 값이 없으면 더 큰수는 없는 것이므로 정답리스트에 -1을 넣어준다.
        answer.append(-1)
    else: #값이 있으면 큰값을 찾은 것이므로 해당 값을 정답 리스트에 넣어준다.
        answer.append(big[-1])
    big.append(A[i]) #그리고 big 스택에 현재 값을 넣어준다.

answer.reverse() #뒤에서부터 확인햇으므로 다시 뒤집어서 출력해준다.

# for i in answer:
#     print(i,end=' ')
print(*answer) #*을 붙이면 공백을 기준으로 원소들만 나열된다.
