import math

def solution():
    MIN, MAX = map(int, input().split(' '))

    num = [True] * (MAX - MIN + 1)
    count = 0
    N = 1

    while N * N  <= MAX:
        N += 1
        square = N * N
        i = MIN // square

        while square * i <= MAX:
            idx = square * i - MIN

            if idx >= 0 and num[idx]:
                count += 1
                num[idx] = False
            i += 1
    print(len(num) - count)

solution()