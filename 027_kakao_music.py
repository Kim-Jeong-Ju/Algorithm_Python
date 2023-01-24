## 문제 027. 방금 그 곡 - 프로그래머스 Lv.2 연습 문제

def calc_time(start, end):
    start_hour, start_min = int(start[:2]), int(start[3:])
    start_time = (start_hour * 60) + start_min
    end_hour, end_min = int(end[:2]), int(end[3:])
    end_time = (end_hour * 60) + end_min

    return end_time - start_time


def compose(total_time, melody):
    melody_list = [melody[0]]
    for a in range(1, len(melody)):
        if melody[a] != "#":        # 직전 문자 그대로인 경우
            melody_list.append(melody[a])
        else:                       # 직전 문자에 #이 붙는 경우
            change = melody_list.pop().lower()
            melody_list.append(change)
    melody = "".join(melody_list)

    if total_time < len(melody):            # 멜로디를 잘라야 함
        result = melody[:total_time]
    elif total_time == len(melody):         # 그대로 출력
        result = melody
    else:                                   # 멜로디를 늘려야함
        iteration = total_time // len(melody)
        add = total_time % len(melody)
        result = melody * iteration + melody[:add]

    return result


def final_select(array):
    array = sorted(array, key=lambda x: (-x[1], x[2]))
    return array[0][0]


def solution(m, musicinfos):
    answer = ''
    crit_list = [m[0]]
    for a in range(1, len(m)):
        if m[a] != "#":         # 직전 문자 그대로인 경우
            crit_list.append(m[a])
        else:                   # 직전 문자에 #이 붙는 경우
            change = crit_list.pop().lower()
            crit_list.append(change)
    m = "".join(crit_list)
    array = []

    for idx, info in enumerate(musicinfos):
        start, end, name, melody = info.split(",")
        total_time = calc_time(start, end)              # 총 재생 시간
        total_music = compose(total_time, melody)       # 총 재생 시간동안 흘러나온 음악

        if m in total_music: array.append((name, total_time, idx))

    if not array: answer = "(None)"
    elif len(array) == 1: answer = array[0][0]
    else: answer = final_select(array)

    return answer