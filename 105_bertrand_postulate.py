## 문제 105. 베르트랑 공준 --- 백준 No.4948

import math


def affirm_prime(Array, mini, maxi):
    for a in range(2, int(math.sqrt(maxi)) + 1):
        if Array[a] == True:
            b = 2
            while a * b <= maxi:
                Array[a * b] = False
                b += 1

    return Array[mini+1:].count(True)

while True:
    num = int(input())
    if num == 0: break
    else:
        mini = num
        maxi = 2 * num
        Array = [True] * (maxi + 1)

        print(affirm_prime(Array, mini, maxi))