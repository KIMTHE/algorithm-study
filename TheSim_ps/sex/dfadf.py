#LIS를 유지하기 위해 숫자가 들어갈 위치를 이분탐색으로 찾는 함수
def binarysearch(left, right, target):
	#LIS 배열에 들어갈 target=arr[i]의 위치를 이분탐색으로 찾기
    while left<right:
        mid=(left+right)//2
		
        if lis[mid]<target:
            left=mid+1
        else:
            right=mid
    return right


arr= [2,1,3,5,4]
lis= [] 
lis.append(arr[0])

for value in arr:
    if lis[-1]<value: 
        lis.append(value)
    else:
        idx=binarysearch(0,len(lis)-1,value)
        lis[idx]=value
    
print(len(lis))
