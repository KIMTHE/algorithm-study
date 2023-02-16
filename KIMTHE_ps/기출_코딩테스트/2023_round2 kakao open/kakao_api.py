import requests #출처: https://github.com/psf/requests
from heapq import *

url = "https://68ecj67379.execute-api.ap-northeast-2.amazonaws.com/api"

#문제를 풀기 위한 key를 발급합니다.
def start_api(problem):
    header = {'X-Auth-Token': 'b6b046583af50ed4b57f85269becd882',
              'Content-Type': 'application/json'}

    data = {"problem": problem
            }

    response = requests.post(url+'/start', headers=header, json=data).json()
    return response["auth_key"]

#현재 날짜에 새로 들어온 예약 요청의 정보를 반환합니다.
def new_requests(key):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'}

    response = requests.get(url + '/new_requests', headers=header).json()
    return response["reservations_info"]


#특정 예약 요청에 대한 승낙 / 거절을 답변합니다.
def reply_api(key, reply_list):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'}

    data = {"replies": reply_list}

    response = requests.put(url + '/reply', headers=header, json=data).json()

    return response["day"]

#오늘 호텔에 체크인 하려는 손님들에게 객실 번호를 배정해 서버에 전달하고 1일이 진행됩니다.
def simulate_api(key, assign_list):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'} 

    data = {"room_assign": assign_list}

    response = requests.put(url + '/simulate', headers=header, json=data).json()

    #print("예약 승낙했지만 배정 실패: "+str(response["fail_count"]))
    return response["day"]

#획득한 점수를 반환합니다.
def score_api(key):
    header = {'Authorization': f'{key}',
              'Content-Type': 'application/json'}

    response = requests.get(url + '/score', headers=header).json()
    print(response)
    return response["score"]
