## 문제 047. 기둥과 보 설치 --- 프로그래머스 Lv.3 연습 문제

def arch_check(state):
    for x, y, type in state:
        if type == 0:  # 기둥 설치 - 바닥 or 기둥 위에 or 보의 한쪽 끝 위에
            if y == 0 or [x, y - 1, 0] in state or [x, y, 1] in state or [x - 1, y, 1] in state:
                pass
            else:
                return False
        else:  # 보 설치 - 양쪽에 보 or 양쪽 중 하나는 기둥 위에
            if y > 0 and (([x - 1, y, 1] in state and [x + 1, y, 1] in state) or [x, y - 1, 0] in state or [x + 1, y - 1, 0] in state):
                pass
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []

    for info in build_frame:
        x, y, type, add_or_del = map(int, info)

        if type == 0:       # 기둥 설치/삭제의 경우
            if x < 0 or x > n or y < 0 or y >= n:
                continue
        else:               # 보 설치/삭제의 경우
            if x < 0 or x >= n or y < 0 or y > n:
                continue

        if add_or_del == 1:     # 구조물 설치하는 경우
            answer.append([x, y, type])
            if not arch_check(answer):
                answer.remove([x, y, type])
        else:                   # 구조물 삭제하는 경우
            answer.remove([x, y, type])
            if not arch_check(answer):
                answer.append([x, y, type])

    answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return answer