
import sys
input = lambda : sys.stdin.readline().rstrip()

chu = int(input()) #추의 갯수
chu_weight = list(map(int,input().split()))
marble = int(input())
marble_weight = list(map(int,input().split()))

## dp를 이용해서 푼 방법

# def find(w,num):
#     if num+1>=chu:
#         return

#     if answer[num][w]:
#         return

#     answer[num][w]=1

    

#     find(w+chu_weight[num-1],num+1)  
#     find(abs(w-chu_weight[num-1]),num+1)
#     find(w,num+1)

# #추의 갯수만큼
# answer=[[0]*(501*chu) for i in range(chu+1)]

# find(chu_weight[0],0)

# for i in marble_weight:
#     if answer[chu-1][i]==1:
#         print("Y",end=" ")
#     else:
#         print("N",end=" ")


# 내가 푼 문제

# q=[]
# q.append(chu_weight[0])
# for i in range(1,chu):

#     p=q[:]
#     p.append(chu_weight[i])
#     while q:
#         v=q.pop()
        
#         if v+chu_weight[i] not in p:
#             p.append(v+chu_weight[i])
#         if v-chu_weight[i] not in p:
#             p.append(v-chu_weight[i])

#     q=p[:]

# answer=[]
# for i in q:
#     answer.append(abs(i))


# for i in marble_weight:
#     if i in answer:
#         print("Y",end=" ")
#     else:
#         print("N",end=" ")


