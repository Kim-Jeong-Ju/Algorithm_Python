## 문제 090. 두 원 사이의 정수 쌍 --- 프로그래머스 Lv.2 연습 문제

from math import sqrt, floor, ceil

def solution(r1, r2):
    answer = 0

    for poss_x in range(1, r2 + 1):
        max_y = floor(sqrt(r2 ** 2 - poss_x ** 2))
        min_y = ceil(sqrt(r1 ** 2 - poss_x ** 2)) if poss_x < r1 else 0
        answer += max_y - min_y + 1

    answer *= 4
    return answer