## 문제 077. 입국 심사 --- 프로그래머스 Lv.3 연습 문제

def binary_search(left, right, n, times):
    result = -1
    while left <= right:
        mid = (left + right) // 2
        count = sum([mid // time for time in times])

        if count >= n:
            if result == -1: result = mid
            else: result = min(result, mid)
            right = mid - 1
        else:
            left = mid + 1

    return result


def solution(n, times):
    answer = 0
    times.sort()

    left, right = 0, times[-1] * n
    answer = binary_search(left, right, n, times)

    return answer