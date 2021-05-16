from queue import PriorityQueue
 
def solution():
    pque = PriorityQueue()
    pque.put((-arr[0][1], arr[0][1]))
    for i in range(1, N):
        if pque.queue[-1][1] <= arr[i][0]:
            pque.get()
            pque.put((-arr[i][1], arr[i][1]))
        else:
            pque.put((-arr[i][1], arr[i][1]))
 
    print(pque.qsize())
    return
 
 
N = int(input())
arr = []
for _ in range(N):
    A, B = list(map(int, input().split()))
    arr.append([A, B])
 
arr.sort(key=lambda x: x[0])
solution()