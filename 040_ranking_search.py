## 문제 039. 순위 검색 --- 프로그래머스 Lv.2 연습 문제

import copy
from itertools import combinations
from bisect import bisect_left


def solution(infos, queries):
    answer = []

    crit = {}
    for info in infos:
        info = list(map(str, info.split()))
        score = int(info.pop())

        for pick in range(5):
            for combi in combinations([0, 1, 2, 3], pick):
                origin = copy.deepcopy(info)
                for a in combi:
                    origin[a] = "-"
                new_key = "".join(origin)
                if new_key in crit.keys():
                    crit[new_key].append(score)
                else:
                    crit[new_key] = [score]

    for value in crit.values():
        value.sort()

    for query in queries:
        query = list(map(str, query.replace(" and ", " ").split()))
        query_score = int(query.pop())
        query_key = "".join(query)

        if query_key in crit.keys():
            idx = bisect_left(crit[query_key], query_score)
            count = len(crit[query_key]) - idx
            answer.append(count)
        else:
            answer.append(0)

    return answer