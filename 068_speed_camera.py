## 문제 068. 단속 카메라 --- 프로그래머스 Lv.3 연습 문제

def solution(routes):
    answer = 0

    routes = sorted(routes, key=lambda x: x[1])
    now_cam = -30001

    for start, end in routes:
        if start <= now_cam:
            continue

        answer += 1
        now_cam = end

    return answer