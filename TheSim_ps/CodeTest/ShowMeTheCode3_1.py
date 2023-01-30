import sys
input = lambda : sys.stdin.readline().rstrip()

N=int(input())
rock=list(map(int,input().split()))


num=[[0,0]]*N

for i in range(N):
    if rock[i]==1:
        num[i][0]=1
    else:
        num[i][1]=1

answer=[0]*N
t=0 #1인지 2인지 체크
for i in range(N):
    

m=0
for i in answer:
    m=max(m,abs(i))
print(answer)
print(m+t)



# for i in range(N):
#     if rock[i]==1:
#         num[i]=1
#     else:
#         num[i]=-1

# answer=[0]*N
# t=0 #1인지 2인지 체크
# for i in range(N):

#     if abs(answer[i-1]+num[i])>abs(num[i]):
#         if (answer[i-1]+num[i])<0: #음수일 경우
#             t=2
#         else:
#             t=1
#         answer[i]=(answer[i-1]+num[i])
#     elif abs(answer[i-1]+num[i])==abs(num[i]):
#         answer[i]=0
#         t+=1
#     else:
#         if rock[i]==2:
#             t=2
#         else:
#             t=1
#         answer[i]=num[i]

# m=0
# for i in answer:
#     m=max(m,abs(i))
# print(answer)
# print(m+t)

