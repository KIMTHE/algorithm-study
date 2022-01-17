import sys
input = lambda : sys.stdin.readline().rstrip()

N,M= map(int,input().split())
tree= list(map(int,input().split()))

tree.sort() #나무 길이 정렬
high=tree[-1] #제일 긴 나무 값
low=1 #최소 값 1


while low<=high: # low값이 high값을 넘는 순간이 최댓값이다
    height=0 #나무 길이
    midle = (low+high)//2 #중앙값
    for i in tree: #얻을 수 있는 나무 길이 
        if (i-midle)<0: #절단기보다 짧은 나무는 패스
            continue
        height+=(i-midle) #자른 나무 값 더하기
    
    if height>=M: #나무를 너무 많이 잘랐으므로 절단기 길이를 높인다
        low=midle+1 #중앙값에서 +1
    else: #절단기 길이를 낮춘다
        high =midle-1 #중앙 값에서 -1

print(high) #low값이 high값을 넘는 순간이 최댓값이므로 high값 출력
    