
def solution(a):
    answer = []
    
    for i in a:
        count=0
        left=0
        right=len(i)-1
        i=list(i)

        while True:
            if left>right:
                answer.append(True)
                break
            if count==1:
                answer.append(False)
                break

            value=i[left:right+1].count("a")  

            
            if i[left]=="a" or  i[right]=="a":
                if i[left]=="a":
                    left+=1
                elif i[right]=="a":
                    right-=1

            elif "a" in i[left:right+1] and "a" not in i[left:value+left] and "a" not in i[right-value+1:right+1]:
                    left+=value
                    right-=value
            else:
                count=1
    
    return answer
    

print(solution(["abab","bbaa","bababa","bbbabababbbaa"]))


