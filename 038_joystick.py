## 문제 038. 조이스틱 --- 프로그래머스 Lv.2 연습 문제

def convert(string):
    result = 0
    for alpha in string:
        if alpha != "A":
            result += min(ord(alpha) - 65, 91 - ord(alpha))

    return result


def solution(name):
    answer = 0
    answer += convert(name)

    if "A" not in name:
        answer += len(name) - 1
    else:
        a_info = []
        for a, alpha in enumerate(name):
            if alpha == "A" and not a_info:
                a_info.append([a, 1])
            elif alpha == "A" and a_info[-1][0] + a_info[-1][1] == a:
                a_info[-1][1] += 1
            elif alpha == "A" and a_info[-1][0] + a_info[-1][1] != a:
                a_info.append([a, 1])

        longest = sorted(a_info, reverse=True, key=lambda x: x[1])[0]
        long_idx, long_len = longest[0] - 1, longest[1]
        rest_len = len(name) - (longest[0] + long_len)
        if long_idx == -1:
            long_idx = 0

        last_not = 0
        for b, beta in enumerate(name[::-1]):
            if beta != "A":
                last_not = len(name) - 1 - b
                break

        answer += min(len(name) - 1, last_not, (2 * long_idx) + rest_len, long_idx + (2 * rest_len))

    return answer