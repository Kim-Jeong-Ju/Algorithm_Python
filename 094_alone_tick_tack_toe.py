## 문제 094. 혼자서 하는 틱택토 --- 프로그래머스 Lv.2 연습 문제

from itertools import combinations

def array_check(array):
    o_bingo, o_cnt, o_locs = 0, 0, []
    x_bingo, x_cnt, x_locs = 0, 0, []

    for row in range(3):
        for col in range(3):
            if array[row][col] == 'O':
                o_cnt += 1
                o_locs.append((row, col))
            elif array[row][col] == 'X':
                x_cnt += 1
                x_locs.append((row, col))

    for aa, bb, cc in combinations(o_locs, 3):
        if aa[0] == bb[0] == cc[0] and aa[1] - bb[1] == bb[1] - cc[1] == -1:
            o_bingo += 1
        elif aa[0] - bb[0] == bb[0] - cc[0] == -1 and aa[1] == bb[1] == cc[1]:
            o_bingo += 1
        elif aa[0] - bb[0] == bb[0] - cc[0] == -1 and aa[1] - bb[1] == bb[1] - cc[1] == -1:
            o_bingo += 1
        elif aa[0] - bb[0] == bb[0] - cc[0] == -1 and aa[1] - bb[1] == bb[1] - cc[1] == 1:
            o_bingo += 1

    for dd, ee, ff in combinations(x_locs, 3):
        if dd[0] == ee[0] == ff[0] and dd[1] - ee[1] == ee[1] - ff[1] == -1:
            x_bingo += 1
        elif dd[0] - ee[0] == ee[0] - ff[0] == -1 and dd[1] == ee[1] == ff[1]:
            x_bingo += 1
        elif dd[0] - ee[0] == ee[0] - ff[0] == -1 and dd[1] - ee[1] == ee[1] - ff[1] == -1:
            x_bingo += 1
        elif dd[0] - ee[0] == ee[0] - ff[0] == -1 and dd[1] - ee[1] == ee[1] - ff[1] == 1:
            x_bingo += 1

    return o_bingo, o_cnt, x_bingo, x_cnt


def solution(board):
    answer = 1

    o_bingo, o_cnt, x_bingo, x_cnt = array_check(board)
    Acase = o_bingo == 0 and x_bingo == 0
    if Acase and 0 <= o_cnt - x_cnt <= 1: return answer

    Bcase = o_bingo == 1 and x_bingo == 0
    if Bcase and o_cnt >= 3 and o_cnt - x_cnt == 1 : return answer

    Ccase = o_bingo == 0 and x_bingo == 1
    if Ccase and o_cnt == x_cnt: return answer

    Dcase = o_bingo == 2 and x_bingo == 0
    if Dcase and o_cnt == 5 and x_cnt == 4: return answer

    answer = 0
    return answer