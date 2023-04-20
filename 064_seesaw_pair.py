## 문제 064. 시소 짝궁 --- 프로그래머스 Lv.2 연습 문제

from collections import Counter
from itertools import permutations


def solution(weights):
    answer = 0

    weight_count = Counter(weights)
    dist_combi = list(permutations([2, 3, 4], 2))

    for weight in weight_count.keys():
        if weight_count[weight] > 1:                # 해당 몸무게인 사람이 여러명인 경우(1:1)
            answer += weight_count[weight] * (weight_count[weight] - 1) // 2

        for a_dist, b_dist in dist_combi:           # dist 조합에 의해 가능한 몸무게를 탐색
            possible = weight * a_dist / b_dist
            if possible in weight_count.keys():     # 가능한 몸무게가 key값에 존재한다면
                answer += weight_count[weight] * weight_count[possible]

        weight_count[weight] = 0                    # 모든 경우의 수를 고려했으므로 0으로 초기화

    return answer