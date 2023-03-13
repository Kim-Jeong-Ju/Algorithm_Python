## 문제 043. 셔틀 버스 --- 프로그래머스 Lv.3 연습 문제

def solution(n, t, maxi, timetable):
    answer = ''

    bus_times = [540]
    for _ in range(n - 1):
        bus_times.append(bus_times[-1] + t)
    in_crews = [[] for _ in range(n)]
    timetable = [(int(time[:2]) * 60) + int(time[3:]) for time in sorted(timetable)]

    last_idx = -1
    for a, bus_time in enumerate(bus_times):
        if a == 0:
            for b in range(maxi):
                if b >= len(timetable): break

                if timetable[b] <= bus_time:
                    in_crews[a].append(b)
                    last_idx = b
        else:
            for c in range(last_idx + 1, maxi + last_idx + 1):
                if c >= len(timetable): break

                if timetable[c] <= bus_time:
                    in_crews[a].append(c)
                    last_idx = c

    if len(in_crews[-1]) < maxi:
        time = 540 + ((n - 1) * t)
    else:
        time = timetable[in_crews[-1][maxi - 1]] - 1

    hour, minute = str(time // 60).zfill(2), str(time % 60).zfill(2)
    answer = hour + ":" + minute

    return answer