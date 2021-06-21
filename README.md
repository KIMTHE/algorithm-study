# problem-solve

### `백준에서 풀이한 알고리즘 문제코드`
- 풀이하는데 어느정도 시간이 소비되었다면 기록한다.
- language : python
- 1 day, 1 solve!
- 1 month, 1 level up!

- [알고리즘 자료정리 링크 클릭](https://docs.google.com/document/d/1rKqgJJ8dncenY-cXzKlQ1RZSf4gjo-_wVMjV9rjE_iw/edit?usp=sharing, "구글 문서")

 ___

## **<solved.ac>**

|date|level_KIMTHE|level_simgyureol|
|--|--|--|
|2021-03-01|silver4|bronze3|
|2021-04-01|silver1|bronze1|
|2021-05-01|gold5|silver5|
|2021-06-01|gold4|silver1|
|2021-07-01|-|-|


___

## **<기타 팁>**
 

### 최대공약수)


python의 유클리드 호제법에 해당하는 함수가 존재한다.


    import math
    math.gcd(a,b)

### 소수판별)


에라토스테네스의 체 알고리즘을 이용하여 1부터 n까지의 소수를 판별한다.

    import math

    array = [True] * (n+1)
    array[1] = False # 1은 소수가 아님

    for i in range(2,int(math.sqrt(n))+1) :
        if array[i] == False : continue

        tmp = i*2
        while tmp <= n :
            array[tmp] = False # 소수의 배수는 소수가 아님
            tmp += i

### DP)


- 최장 증가 부분 수열(LIS, Longest Increasing Subsequence)

    index=i까지 최장증가부분수열의 길이을 구함, 시간복잡도 O(n^2)

        for i in range(n):
            DP[i] = 1  
        
            for j in range(i):
                if list[j] < list[i]:
                    DP[i] = max(DP[i],DP[j]+1)
    
