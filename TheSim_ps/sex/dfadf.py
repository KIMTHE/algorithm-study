def find(card1, card2): 
    answer=0

    user1=[] #받은 카드 저장
    user2=[]     

    for i,j in zip(card1,card2):
        # 두 플레이어 카드 비교
        # for a in i:
        #     if a in j: #카드가 있다면
        #         answer+=1
        #         break
        value= i+j
        for a in value:
            if value.count(a)>=2:
                answer+=1
                break

        else: #직전에 받은 카드 비교
            visit=0 #중복 여부
            if user1:
                for a in i:
                    if a in user1[-1]:
                        visit+=1
                    if visit==2:
                        answer+=1
                        break
                else:
                    visit=0 #중복 여부
                    for a in j:
                        if a in user2[-1]:
                            visit+=1
                        if visit==2:
                            answer+=1
                            break
        user1.append(i)
        user2.append(j)

    print(answer)
                    
            

    return answer

#한 라운드에서 두 플레이어가 받은 카드 10장중 중복
# 한 플레이어 직전에 받은 카드 5장과 이번에 2개 이상 중복

card1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[13, 21, 24, 29, 50], [1, 12, 20, 21, 32], [16, 26, 34, 46, 52], [9, 11, 16, 16, 21], [3, 8, 10, 16, 20]]
card2 = [[5, 7, 9, 11, 13], [11, 13, 15, 17, 19],[5, 10, 15, 41, 49], [6, 14, 15, 19, 46], [5, 42, 43, 51, 52], [5, 6, 11, 13, 45], [5, 9, 11, 13, 45]]
find(card1,card2) 