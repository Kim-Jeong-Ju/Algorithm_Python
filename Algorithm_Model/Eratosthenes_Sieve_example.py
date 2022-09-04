## Eratosthenes' Sieve(에라토스테네스의 체) Algorithm Example Code
## 하나의 수가 소수인지 아닌지 판별하는 것이 아닌, 특정 범위 내의 모든 수를 소수인지 아닌지 판별하는 알고리즘

import math

n = int(input())                # 2~n 까지 존재하는 모든 수에 대한 소수 판별 수행
array = [True] * (n + 1)        # 소수이면 True, 소수가 아니면 False를 기록하는 list, n이 커질수록 공간복잡도 커짐

for a in range(2, int(math.sqrt(n)) + 1):       # 개선된 소수 판별 사용
    if array[a] == True:                        # 2~sqrt(n)까지의 수를 반복하며 소수이면
        b = 2
        while a * b <= n:
            array[a * b] = False
            b += 1

for i in range(2, n + 1):
    if array[i]:
        print(i, end=" ")