def solution(numbers):
    answer = ''
    
    numbers = list(map(str,numbers))
    
    numbers.sort(key = lambda x:(x[0],x[1%len(x)],x[2%len(x)],x[3%len(x)]),reverse = True)
    
    for n in numbers: answer += n

    if int(answer) == 0 : answer = '0'
    
    return answer