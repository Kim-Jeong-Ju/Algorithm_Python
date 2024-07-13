## 문제 101. 양궁 대회 --- 프로그래머스 Lv.2 연습 문제

from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_diff = 0

    for case in list(combinations_with_replacement(range(11), n)):
        rion = [0] * 11
        for score in case:
            rion[score] += 1

        rion = rion[::-1]
        apeach_score, rion_score = 0, 0

        # 어피치 & 라이언 점수 계산
        for idx in range(11):
            if rion[idx] > info[idx]:
                rion_score += 10 - idx
            elif info[idx]:
                apeach_score += 10 - idx

        # 라이언이 이겼고(점수차가 양수), 점수차가 이전 경우보다 크다면
        score_diff = rion_score - apeach_score
        if score_diff > max_diff:
            # 가장 낮은 점수를 더 많이 맞힌 경우가 result -> 뽑을 때 작은 것부터 뽑아서 자동 정렬
            max_diff = score_diff
            answer = rion

    return answer