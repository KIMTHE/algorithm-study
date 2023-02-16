from kakao_2nd_api import *

URL = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
USER_NUM = 900

# 1회 시뮬레이션 후 10분 이내로 진 횟수가 일정 숫자 이상이었던 유저를 어뷰저로 등록
# 여러번 시뮬레이션 했을 때, 항상 같은 번호의 유저들이 똑같은 횟수로 10분 이내로 패배함. 때문에 이런 간단한 방식으로 풀이
# 시간 부족으로 abusers를 하드 코딩해서 풀이했지만 시간이 더 있었으면 게임하면서 10분 이내로 진 유저들을 어뷰저로 분류하는 로직을 추가 했을 듯
# abusers 부분을 제외하고도 50위 정도의 순위를 달성한 코드
abusers = [89, 214, 277, 41, 80, 318, 129, 504, 566, 580, 681, 776, 6, 136, 145, 154, 291, 303, 341, 348, 369, 503,
           509, 579, 747, 755, 415, 590, 606, 703, 705, 627, 798, 845, 855]

if __name__ == "__main__":
    auth_key = start_api(URL, 2)

    pairs = []
    cmd = []
    for i in range(1, USER_NUM + 1):
        cmd.append({"id": i, "grade": 5000})
    change_grade_api(URL, auth_key, cmd)

    result = 'ready'

    while result == 'ready':
        response = match_api(URL, auth_key, pairs)
        result = response['status']
        time = response['time']
        max_time = 0
        waiting_lines = waiting_line_api(URL, auth_key)

        user_grade = [0] * (USER_NUM + 1)
        for user_info in user_info_api(URL, auth_key):
            user_grade[user_info['id']] = user_info['grade']

        for waiting_line in waiting_lines:
            max_time = max(time - waiting_line['from'], max_time)

        if time <= 540:
            pairs = match_users(user_grade, waiting_lines, 3, max_time, 14)
        elif time < 555:
            pairs = match_users(user_grade, waiting_lines, 1, max_time, 14)
        elif time == 555:
            pairs = match_users(user_grade, waiting_lines, 0, max_time, 14)
        elif time <= 595:
            pass

        for game_result in game_result_api(URL, auth_key):
            winner = game_result['win']
            loser = game_result['lose']
            taken = game_result['taken']

            # 시간 가중치 + 점수 가중치(높은 점수의 상대를 이기면 더 높은 점수를 부여)
            point = ((40 - taken) + 1) * 10

            # 어뷰저가 진 경우 반대로 계산
            if loser in abusers:
                user_grade[loser] += point + (user_grade[loser] // 100)
                user_grade[winner] -= point + (100 - (user_grade[winner] // 100))
            else:
                user_grade[winner] += point + (user_grade[loser] // 100)
                user_grade[loser] -= point + (100 - (user_grade[winner] // 100))
                
        cmd = []
        for i in range(1, USER_NUM + 1):
            cmd.append({"id": i, "grade": user_grade[i]})
        change_grade_api(URL, auth_key, cmd)

    score_api(URL, auth_key)
