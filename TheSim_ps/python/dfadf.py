from itertools import permutations

def find(dist,weak):
    global answer


    for i in range(len(weak)//2):       
            for friends in permutations(dist):
                
                count=1
                position=weak[i]
                
                for j in friends:
                    position+=j

                    if position < weak[i+len(weak)//2-1]:
                        count+=1
                        
                        for k in range(i+1,i+len(weak)//2):
                            if weak[k] > position:
                                position=weak[k]
                                break
                    else:
                        answer=min(answer,count)
                        break
    return answer

            
def solution(n, weak, dist):
    global answer
    answer = 1000
    dist.sort(reverse=True)

    for i in range(len(weak)):
        weak.append(weak[i]+n)
 

    find(dist,weak)
                
    if answer==1000:
        return -1
    
    return answer

n=12
weak=[1,5,6,10]
dist=[1,2,3,4]

# n = 30
# weak = [0, 3,11,21]
# dist = [10,4]

# n= 12
# weak= [1, 3, 4, 9, 10]
# dist= [3, 5, 7]

n = 200
weak = [0, 10, 50, 80, 120, 160]
dist = [1, 10, 5, 40, 30]

print(solution(n,weak,dist))