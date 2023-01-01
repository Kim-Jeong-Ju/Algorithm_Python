## 문제 024. 쿼드압축 후 갯수 세기 - 프로그래머스 Lv.2 연습 문제

def is_stop(array):
    crit = array[0][0]
    for a in range(len(array)):
        for b in range(len(array[0])):
            if array[a][b] != crit:
                return False
            else:
                pass
    return True


def recursive(array, zeros, ones):
    if len(array) == 1 and len(array[0]) == 1:
        if array[0][0] == 0:
            zeros += 1
        else:
            ones += 1
        return zeros, ones

    else:
        if is_stop(array):
            if array[0][0] == 0:
                zeros += 1
            else:
                ones += 1
            return zeros, ones
        else:
            half = len(array) // 2
            Array = []
            for row in array[:half]:
                Array.append(row[:half])
            Brray = []
            for row in array[:half]:
                Brray.append(row[half:])
            Crray = []
            for row in array[half:]:
                Crray.append(row[:half])
            Drray = []
            for row in array[half:]:
                Drray.append(row[half:])

            a_zeros, a_ones = recursive(Array, zeros, ones)
            b_zeros, b_ones = recursive(Brray, zeros, ones)
            c_zeros, c_ones = recursive(Crray, zeros, ones)
            d_zeros, d_ones = recursive(Drray, zeros, ones)

            total_zeros = a_zeros + b_zeros + c_zeros + d_zeros
            total_ones = a_ones + b_ones + c_ones + d_ones
            return total_zeros, total_ones


def solution(array):
    answer = []
    zeros, ones = recursive(array, 0, 0)
    answer = [zeros, ones]

    return answer