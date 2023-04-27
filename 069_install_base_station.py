## 문제 069. 기지국 설치 --- 프로그래머스 Lv.3 연습 문제

def solution(N, stations, W):
    answer = 0

    array = []
    stations = [[station - W, station + W] for station in stations]

    if len(stations) == 1:
        left, right = stations[0]
        if left > 1: array.append(left - 1)
        if N - right >= 1: array.append(N - right)
    else:
        for idx, [left, right] in enumerate(stations):
            if idx == 0:
                if left > 1: array.append(left - 1)
            elif idx == len(stations) - 1:
                if left - stations[idx - 1][1] > 1: array.append(left - stations[idx - 1][1] - 1)
                if N - right >= 1: array.append(N - right)
            else:
                if left - stations[idx - 1][1] > 1: array.append(left - stations[idx - 1][1] - 1)

    for value in array:
        div, mod = divmod(value, 2 * W + 1)
        if mod == 0:
            answer += div
        else:
            answer += div + 1

    return answer