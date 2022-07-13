def solution(n, horizontal):
    answer = [[]]
    
    clean=[[0]*n for i in range(n)]
    
    yeol=[[0,1],[-1,0]] #수평
    hang=[[1,0],[0,-1]] #수직

    count=1
    clean[0][0]=count
    q=[0,0] #현재 위치
    for i in range(2,n+1):
        if horizontal: #수평
            count+=1
            clean[q[0]+0][q[1]+1]=count #처음에 오른쪽로 한칸
            q=[q[0]+0,q[1]+1]
            for a,b in hang:
                while True: #오른쪽 위로 움직이기
                    if q[0]+a==i or q[1]+b==i or q[0]+a<0 or q[1]+b<0:
                        horizontal=False
                        break
                    if 0<=q[0]+a<n and 0<= q[1]+b<n:
                        count+=1
                        clean[q[0]+a][q[1]+b]=count
                        q=[q[0]+a,q[1]+b]

        else:
            count+=1
            clean[q[0]+1][q[1]+0]=count #처음에 아래로 한칸
            q=[q[0]+1,q[1]+0]
            for a,b in yeol:

                while True: #오른쪽 위로 움직이기
                    if q[0]+a==i or q[1]+b==i or q[0]+a<0 or q[1]+b<0:
                        horizontal=True
                        break
                    if 0<=q[0]+a<n and 0<= q[1]+b<n:
                        count+=1
                        clean[q[0]+a][q[1]+b]=count
                        q=[q[0]+a,q[1]+b]

    return answer

print(solution(4,True))