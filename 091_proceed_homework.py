## 문제 091. 과제 진행하기 --- 프로그래머스 Lv.2 연습 문제

def solution(plans):
    answer = []

    Array = sorted([[aa, 60 * int(bb[:2]) + int(bb[3:]), int(cc)] for aa, bb, cc in plans], key=lambda x: x[1])
    Brray = []

    for idx in range(len(Array)):
        if idx < len(Array) - 1:
            before_name, before_time, before_long = Array[idx]
            after_name, after_time, after_long = Array[idx+1]

            if before_time + before_long <= after_time:
                answer.append(before_name)
                rest = after_time - (before_time + before_long)

                while rest != 0 and Brray:
                    wait_name, wait_time, wait_long = Brray.pop()
                    if rest >= wait_long:
                        rest -= wait_long
                        answer.append(wait_name)
                    else:
                        Brray.append([wait_name, wait_time, wait_long - rest])
                        rest = 0

            else:
                Array[idx][2] = before_long - (after_time - before_time)
                Brray.append(Array[idx])

        else:
            Brray.append(Array[idx])
            break

    while Brray:
        answer.append(Brray.pop()[0])

    return answer