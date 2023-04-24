## 문제 066. 보석 쇼핑 --- 프로그래머스 Lv.3 연습 문제

from collections import defaultdict


def solution(gems):
    answer = []

    a_point, b_point, size = 0, 0, len(set(gems))
    check, intervals = defaultdict(int), []

    for idx in range(len(gems)):
        check[gems[idx]] += 1
        b_point = idx
        while len(check) == size:
            intervals.append([a_point + 1, b_point + 1])
            check[gems[a_point]] -= 1
            if check[gems[a_point]] == 0: del check[gems[a_point]]
            a_point += 1

    answer = sorted(intervals, key=lambda x: (x[1] - x[0], x[0]))[0]
    return answer