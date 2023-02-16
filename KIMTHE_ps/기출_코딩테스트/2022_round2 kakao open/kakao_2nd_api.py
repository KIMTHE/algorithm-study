import requests #https://github.com/psf/requests
from heapq import *


#post header+parameter
def start_api(url, problem):
    header = {'X-Auth-Token': '15018013c92b7f5d1da1a0abd0443f38',
              'Content-Type': 'application/json'}

    data = {"problem": f'{problem}'
            }

    response = requests.post(url+'/start', headers=header, json=data).json()
    return response["auth_key"]

#대기 중인 유저들의 정보를 받음
def waiting_line_api(url, key):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'}

    response = requests.get(url + '/waiting_line', headers=header).json()
    return response["waiting_line"]

#이번 턴에 끝난 게임 결과 정보를 받음
def game_result_api(url, key):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'}

    response = requests.get(url + '/game_result', headers=header).json()
    return response["game_result"]


def user_info_api(url, key):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'}

    response = requests.get(url + '/user_info', headers=header).json()
    return response["user_info"]

#대기열에서 대기 중인 유저들을 매칭시켜 줄 수 있으며, 
# 동시에 다음 턴으로 넘어간다(1분 진행)
#매칭시킬 유저가 없더라도, Match API를 이용해 아무도 매칭시키지 않음을 전달해야 한다.
#put header+parameter
def match_api(url, key, match_list):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'}

    data = {"pairs": match_list}

    response = requests.put(url + '/match', headers=header, json=data).json()
    print(response)
    return response
    
#게임 결과 정보를 참고하여, 특정 유저의 등급을 수정
#put header+parameter
def change_grade_api(url, key, command):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'}

    data = {"commands": command}

    response = requests.put(url + '/change_grade', headers=header, json=data).json()
    return response


def score_api(url, key):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'}

    response = requests.get(url + '/score', headers=header).json()
    print(response)
    return response["score"]


def match_users(user_grade, waiting_lines, wait_limit, max_time, max_time_limit):
    heap = []
    pairs = []
    if len(waiting_lines) > wait_limit or max_time > max_time_limit:
        for waiting_line in waiting_lines:
            user_id = waiting_line['id']
            user_from = waiting_line['from']
            heappush(heap, (-user_grade[user_id], user_from, user_id))
        while len(heap) > 1:
            user1 = heappop(heap)
            user2 = heappop(heap)
            pairs.append([user1[2], user2[2]])

    return pairs
