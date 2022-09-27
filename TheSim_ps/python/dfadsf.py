
from bisect import bisect_left

array = [5, 2, 1, 4, 3, 5,2,3]
dp = [1]
x = [array[0]]

for i in range(1, len(array)):
    if array[i] > x[-1]: # 현재 값이 x 배열의 마지막 값보다 클 경우
        x.append(array[i]) # x 배열에 현재 값을 추가해 주고
        dp.append(dp[-1] + 1) # 증가 부분 수열의 길이를 1 증가시킨다.
    else: # 그렇지 않을 경우
        idx = bisect_left(x, array[i]) # 현재 값이 x 배열의 몇 번째 인덱스에 들어갈 수 있는지를 찾아서
        x[idx] = array[i] # x 배열의 idx 위치에 현재 값을 넣어준다.