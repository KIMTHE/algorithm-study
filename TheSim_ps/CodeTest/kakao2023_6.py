from collections import deque
import sys
sys.setrecursionlimit(10**4)

def find(a,b,degree,r,u,k,word,visit,n,m,x,y,word_temp):
    dir = [[1,0],[0,1],[-1,0],[0,-1]] # d, r, u, l
    global value

    if a==r and b==u and degree==k: #종료
        value.append(word)
        value.sort()
        return

    if degree>=k:
        return

    else:
        for i in range(len(dir)):
            ai=a+dir[i][0]
            bj=b+dir[i][1]

            if 1<=ai<=n and 1<=bj<=m:

                if i==0:
                    word+='d'
                elif i==1:
                    word+='r'
                elif i==2:
                    word+='u'
                else:
                    word+='l'
                if word not in word_temp or word>value[0]:
                    word_temp.add(word)
                    find(ai,bj,degree+1,r,u,k,word,visit,n,m,x,y,word_temp)

                    word=word[:-1]
                # visit[ai][bj]=0

def solution(n, m, x, y, r, c, k):
    answer = ''
    global value
    value=[]

    q=deque()
    q.append([x,y,0])
    visit= [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    word=''
    word_temp=set()
    find(x,y,0,r,c,k,word,visit,n,m,x,y,word_temp)

    
    if len(value)==0:
        answer="impossible"
    else:
        value.sort()
        answer=value[0]

    return answer

print(solution(3,4,2,3,3,1,5))
#print(solution(2,2,1,1,2,2,2))
#print(solution(3,3,1,2,3,3,4))