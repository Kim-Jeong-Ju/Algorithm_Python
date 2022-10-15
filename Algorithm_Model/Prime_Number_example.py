## Prime Number Algorithm Example Code

import math

n = int(input())

def normal_is_prime(num):           # 일반적인 소수 판별법 : 시간복잡도 = O(N)
    for x in range(2, num):
        if num % x == 0:
            return True
    return False

print(f"일반적인 소수 판별법 : {normal_is_prime(n)}")




def advanced_is_prime(num):         # 개선된 소수 판별법 : 제곱근의 정수형 숫자까지만 반복, 시간복잡도 = O(sqrt(N))
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return True
    return False

print(f"개선된 소수 판별법 : {advanced_is_prime(n)}")