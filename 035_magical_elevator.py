## 문제 035. 마법의 엘리베이터 --- 프로그래머스 Lv.2 연습 문제

def solution(storey):
    answer = 0

    if len(str(storey)) == 1:
        bot, top = 0, 10
    else:
        bot = int(str(int(str(storey)[0])) + ("0" * (len(str(storey)) - 1)))
        top = int(str(int(str(storey)[0]) + 1) + ("0" * (len(str(storey)) - 1)))

    while storey != bot and storey != top:
        idx = -1
        for a, alpha in enumerate(str(storey)[::-1]):
            if alpha != "0":
                idx = a
                break

        now_num = int(str(storey)[len(str(storey)) - 1 - idx])
        if now_num > 5:
            storey += (10 - now_num) * (10 ** idx)
            answer += 10 - now_num
        elif now_num < 5:
            storey -= now_num * (10 ** idx)
            answer += now_num
        else:
            front_num = int(str(storey)[len(str(storey)) - 2 - idx])
            if front_num >= 5:
                storey += 5 * (10 ** idx)
                answer += 5
            else:
                storey -= 5 * (10 ** idx)
                answer += 5

    if int(str(storey)[0]) > 5:
        answer += 11 - int(str(storey)[0])
    else:
        answer += int(str(storey)[0])

    return answer