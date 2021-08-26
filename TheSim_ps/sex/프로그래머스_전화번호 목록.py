
a=5
b=5
def solution(N, number):
    answer = 0
    value=[set() for x in range(8)]

    for i in range(1,9):
        value[i-1].add(int(str(N)*i))
    
    for i in range(0,8):
        for j in range(i):
            for a in value[j]:
                for b in value[i-j-1]:
                    value[i].add(a+b)
                    value[i].add(a-b)
                    value[i].add(a*b)
                    if b!=0:
                        value[i].add(a//b)
    
        if number in value[i]:
            return i+1

    return -1
    
print(solution(a,b))


