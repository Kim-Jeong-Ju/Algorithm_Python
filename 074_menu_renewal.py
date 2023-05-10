## 문제 074. 메뉴 리뉴얼 --- 프로그래머스 Lv.2 연습 문제

from itertools import combinations

def solution(orders, course):
    answer = []
    cur_dict = {}
    orders = ["".join(sorted(order)) for order in orders]
    check_size = [len(order) for order in orders]
    min_size = min(min(check_size), min(course))
    max_size = max(check_size)

    for size in range(min_size, max_size + 1):
        for order in orders:
            if len(order) > size:
                combis = list(combinations(order, size))
                for combi in combis:
                    cur_dict["".join(combi)] = 0
            elif len(order) == size:
                cur_dict[order] = 0
            else:
                pass

    for name in cur_dict.keys():
        count = 0
        for order in orders:
            is_okay = True
            for alpha in name:
                if alpha in order:
                    pass
                else:
                    is_okay = False
            if is_okay:
                count += 1
            else:
                pass
        cur_dict[name] = count

    cur_dict = {key: value for key, value in cur_dict.items() if value != 1}
    for size in course:
        maxi = 0
        for key in cur_dict.keys():
            if len(key) == size:
                if cur_dict[key] >= maxi: maxi = cur_dict[key]
        if maxi == 0:
            pass
        else:
            for key, value in cur_dict.items():
                if value == maxi and len(key) == size: answer.append(key)

    answer.sort()
    return answer