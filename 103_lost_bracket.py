## 문제 103. 유연근무제 --- 프로그래머스 Lv.1 연습 문제

def solution(schedules, timelogs, startday):
    answer = 0

    for sched, timelog in zip(schedules, timelogs):
        after, before = startday, startday
        sched = int(str(sched)[0]) * 60 + int(str(sched)[1:]) if len(str(sched)) <= 3 else int(str(sched)[:2]) * 60 + int(str(sched)[2:])
        flag = True

        for attend in timelog:
            if after % 7 == 6 or after % 7 == 0: after += 1
            else:
                attend = int(str(attend)[0]) * 60 + int(str(attend)[1:]) if len(str(attend)) <= 3 else int(str(attend)[:2]) * 60 + int(str(attend)[2:])
                if attend <= sched + 10: after += 1
                else:
                    after = before
                    flag = False
                    break

        if flag == True: answer += 1

    return answer