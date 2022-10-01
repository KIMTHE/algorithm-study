# def dfs(delive,pick,cap,start,house,deliveries,pickups):

#     #if deliveries[house]!=0 or pickups[house]!=0: #택배 주거나 가져갈게 있다면 들려야한다.
        
#     while True: #택배상자가 가득 찰 동안 반복

#         if deliveries[house]==0 and pickups[house]==0: #집에 가져갈게 없다면 이전집
#             house-=1

#         if deliveries[house]!=0: 
#             if delive>=deliveries[house]: #택배가 남아 있다면 이전 집에 택배를 준다
#                 delive-=deliveries[house]
#                 deliveries[house]=0

#                 #해당 집에 수거할 상자가 있으면 수거해간다. 

#             else: #줄 택배가 없으면 창고로 돌아가면서 상자만 거둔다.
#                 deliveries[house]-=delive
#                 delive=0

#         if pickups[house]!=0: #택배 주거나 가져갈게 있다면 들려야한다.
#             if cap-(delive+pick)>=pickups[house]: #다 넣을 수 있다면 다 넣음
#                 pick+=pickups[house]
#                 pickups[house]=0
#             else: #다 못넣음
#                 pick=cap-(delive+pick)
#                 pickups[house]-=(cap-(delive+pick))
        
#         if deliveries[house]!=0 or pickups[house]!=0: #집에 가져갈게 없다면 이전집
#                 continue

def backtracking(start,end,cap,degree,deliveries,pickups):
    global answer
    if sum(deliveries)==0 and sum(pickups)==0: #모두 배달 햇으면

        answer=min(answer,degree)
        return 
    
    for i in range(cap):

        backtracking(end,end-1,cap,degree,deliveries,pickups) #창고라면 

        backtracking(end,0,cap,degree,deliveries,pickups) #다른집 더 들릴 수 없으면 바로 창고로 이동

        backtracking(end,end-1,cap,degree,deliveries,pickups) #다른집 더 들릴 수 있다면

def solution(cap, n, deliveries, pickups):
    answer = -1

    #시작할 때 택배상자가 1~cap개의 택배상자를 가져옴
    #마지막 집부터 갔다오는게 제일 빠르다. 마지막 집에서 볼일 다보기
    # 택배를 주던가 or 수거하던가

    #dfs(cap,0,n-1)

    for i in range(cap):
        


    return answer

solution(4,5,[1,0,3,1,2],[0,3,0,4,0])