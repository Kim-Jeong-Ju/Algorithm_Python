## 문제 088. 연속 펄스 부분 수열의 합 --- 프로그래머스 Lv.3 연습 문제

def solution(sequence):
    answer = 0

    Array = [Anum if Aidx % 2 == 0 else -Anum for Aidx, Anum in enumerate(sequence)]
    Brray = [Bnum if Bidx % 2 != 0 else -Bnum for Bidx, Bnum in enumerate(sequence)]

    global_max = 0
    Atemp, Btemp = 0, 0
    for a_num in Array:
        Atemp += a_num
        if Atemp < 0: Atemp = 0
        global_max = max(global_max, Atemp)
    for b_num in Brray:
        Btemp += b_num
        if Btemp < 0: Btemp = 0
        global_max = max(global_max, Btemp)

    answer = global_max
    return answer