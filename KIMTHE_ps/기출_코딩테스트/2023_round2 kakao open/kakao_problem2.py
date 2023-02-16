from kakao_api import *
import heapq

scenario = 2
end_day = 1000
floor_cnt = 10
room_cnt = 200

down_limit = 2 
day_limit = 60
up_limit = 20

if __name__ == "__main__":
    auth_key = start_api(scenario)

    hotel_now = [[0 for _ in range(room_cnt+1)] for _ in range(floor_cnt+1)] #오늘 호텔 상황 (체크아웃 날짜)
    hotel_rv = [[[] for _ in range(room_cnt+1)] for _ in range(floor_cnt+1)] #각 객실 확정예약 상황 (체크인,체크아웃), 최소힙
    rv_list = [] #확정예약 리스트 (체크인,체크아웃,id,amount,층,객실), 최소힙
    floor_record = [(0,f) for f in range(1,floor_cnt+1)] #각 층이 사용된 횟수, 최소힙
    room_record = [[(0,r) for r in range(1,room_cnt+1)] for _ in range(floor_cnt+1)] #각 (시작)객실이 사용된 횟수, 최소힙

    rv_P1_list = [] #우선순위 1 예약 리스트 (-amount,체크인,-체크아웃,id) , 최소힙
    rv_P2_list = [] #우선순위 2 예약 리스트 (답변기한,amount,체크인,체크아웃,id) , 최소힙
    rv_P3_list = [] #우선순위 3 예약 리스트 (답변기한,amount,체크인,체크아웃,id) , 최소힙
    rv_P4_list = [] #우선순위 4 예약 리스트 (답변기한,amount,체크인,체크아웃,id) , 최소힙
    rv_P5_list = [] #우선순위 5 예약 리스트 (답변기한,amount,체크인,체크아웃,id) , 최소힙

    def check_room_pos(f,rs,re,check_in,check_out):
        #각 객실의 예약 체크
        if rs < 1 or re > room_cnt: return False

        for r in range(rs,re+1):
            if hotel_now[f][r] > check_in:
                return False

            for rv_in,rv_out in hotel_rv[f][r]:
                if (check_in==rv_in) or (check_in<rv_in and check_out>rv_in) or (check_in<rv_out and check_out>rv_in):
                    return False

        return True

    def make_rv(check_in,check_out,id,amount,f,r):
        #예약 수행
        heapq.heappush(rv_list,(check_in,check_out,id,amount,f,r))

        for ri in range(r,r+amount):
            heapq.heappush(hotel_rv[f][ri],(check_in,check_out))

    def make_room_number(f,r):
        r = str(r)

        if len(r) == 1: r = "00"+r
        elif len(r) == 2: r = "0"+r

        return int(str(f)+r)


    day = 1
    while day <= end_day:
        reservation_list = new_requests(auth_key)

        #예약 답변 기간 : trade-off
    
        for reservation in reservation_list:
            id = reservation["id"]
            amount = reservation["amount"]
            check_in = reservation["check_in_date"]
            check_out = reservation["check_out_date"]
            dead = min(day+14,check_in-1)

            if dead-day < 3: heapq.heappush(rv_P1_list,(-amount,check_in,-check_out,dead,id))
            elif dead-day < 6: heapq.heappush(rv_P2_list,(dead,amount,check_in,check_out,id))
            elif dead-day < 9: heapq.heappush(rv_P3_list,(dead,amount,check_in,check_out,id))
            elif dead-day < 12: heapq.heappush(rv_P4_list,(dead,amount,check_in,check_out,id))
            elif dead-day < 15: heapq.heappush(rv_P5_list,(dead,amount,check_in,check_out,id))

        #다중 레벨 큐
        while len(rv_P5_list) > 0 and rv_P5_list[0][0]-day < 12:
            heapq.heappush(rv_P4_list,heapq.heappop(rv_P5_list))

        while len(rv_P4_list) > 0 and rv_P4_list[0][0]-day < 9:
            heapq.heappush(rv_P3_list,heapq.heappop(rv_P4_list))

        while len(rv_P3_list) > 0 and rv_P3_list[0][0]-day < 6:
            heapq.heappush(rv_P2_list,heapq.heappop(rv_P3_list))

        while len(rv_P2_list) > 0 and rv_P2_list[0][0]-day < 3:
            dead,amount,check_in,check_out,id = heapq.heappop(rv_P2_list)
            heapq.heappush(rv_P1_list,(-amount,check_in,-check_out,dead,id))

        reply_list = []
        add_P1_list = []

        while rv_P1_list:
            amount,check_in,check_out,dead,id = heapq.heappop(rv_P1_list)
            amount = -amount
            check_out = -check_out
            
            #가장 덜 사용된 객실 탐색
            add_floor_list = []
            add_room_list = []
            
            while floor_record:
                #가장 덜 사용된 층

                if amount <= down_limit and check_out-check_in>day_limit: 
                    reply = "refused"
                    break
                
                floor_use,floor = heapq.heappop(floor_record)
                is_floor_pos = False

                while room_record[floor]:
                    #가장 덜 사용된 객실
                    room_use,room = heapq.heappop(room_record[floor])

                    is_room_pos = check_room_pos(floor,room,room+amount-1,check_in,check_out)

                    if is_room_pos == True:
                        add_room_list.append((room_use+1,room))
                        is_floor_pos = True
                        break
                    else:
                        add_room_list.append((room_use,room))

                for add_room in add_room_list: #힙 복구
                    heapq.heappush(room_record[floor],add_room)
                add_room_list = []

                if is_floor_pos == False:
                    add_floor_list.append((floor_use,floor))
                    reply = "refused"
                elif is_floor_pos == True: #마땅한 객실이 존재
                    add_floor_list.append((floor_use+1,floor))
                    reply = "accepted"
                    make_rv(check_in,check_out,id,amount,floor,room)
                    break
                    
            for add_floor in add_floor_list: #힙 복구
                heapq.heappush(floor_record,add_floor)

            if amount >= up_limit and day<dead and is_floor_pos == False: 
                add_P1_list.append((-amount,check_in,-check_out,dead,id))
                continue

            reply_list.append({"id":id, "reply":reply})
            print(str(id)+" "+reply)

        print(str(reply_api(auth_key,reply_list))+"일 "+str(len(reply_list))+"개 예약 답변완료")

        for add_P1 in add_P1_list: #힙 복구
            heapq.heappush(rv_P1_list,add_P1)
          
        #체크인 수행
        assign_list = []

        while len(rv_list) > 0 and rv_list[0][0] == day:
            check_in,check_out,id,amount,f,r = heapq.heappop(rv_list)
            assign_list.append({"id":id, "room_number":make_room_number(f,r)})

            for ri in range(r,r+amount):
                hotel_now[f][ri] = check_out
                heapq.heappop(hotel_rv[f][ri])


        day = int(simulate_api(auth_key,assign_list))
            

    #정확성: 객실 이용률 비례, 목표치만 되면 됨
    #효율성: 예약 답변이 빠를수록 높음
    #패널티: 승낙하고 객실배정실패 > 거절한 예약요청 객실수 > 예약요청 거절수
    score_api(auth_key)