T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    point=list(map(int,input().split()))

    count=[0]*101

    for i in point:
        count[i]+=1

    answer=0
    m=0

    for i in range(101):
        if m<=count[i]:
            m=count[i]
            answer=i
    
    print("#"+str(n)+" "+str(answer))
