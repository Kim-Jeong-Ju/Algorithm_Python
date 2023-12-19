## 문제 098. 붕대 감기 --- 프로그래머스 PCCP 기출문제 1번

def solution(bandage, health, attacks):
    answer = health

    last_time = 0
    for attack in attacks:
        diff = attack[0] - last_time - 1
        if diff < bandage[0]:
            answer += diff * bandage[1]
        elif diff >= bandage[0]:
            div, mod = divmod(diff, bandage[0])
            answer += (diff * bandage[1]) + (diff // bandage[0] * bandage[2])

        last_time = attack[0]
        if answer > health: answer = health

        if answer > attack[1]:
            answer -= attack[1]
        else:
            answer = -1
            break

    return answer