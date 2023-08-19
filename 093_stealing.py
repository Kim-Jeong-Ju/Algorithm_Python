## 문제 093. 도둑질 --- 프로그래머스 Lv.4 연습 문제

def solution(money):
    answer = 0

    Array = [0] + money[:-1]
    Brray = [0] + money[1:]
    for idx in range(2, len(money)):
        Array[idx] = max(Array[idx - 1], Array[idx - 2] + Array[idx])
        Brray[idx] = max(Brray[idx - 1], Brray[idx - 2] + Brray[idx])

    answer = max(Array[-1], Brray[-1])
    return answer