## 문제 036. 무인도 여행 --- 프로그래머스 Lv.2 연습 문제

import sys
sys.setrecursionlimit(10 ** 5)

def dfs(array, row, col, summation):
    array[row][col] = "X"
    move_row = [-1, 1, 0, 0]
    move_col = [0, 0, -1, 1]

    for i in range(4):
        after_row = row + move_row[i]
        after_col = col + move_col[i]
        if 0 <= after_row < len(array) and 0 <= after_col < len(array[0]) and array[after_row][after_col] != "X":
            summation += int(array[after_row][after_col])
            summation = dfs(array, after_row, after_col, summation)

    return summation


def solution(maps):
    answer = []
    maps = [list(map) for map in maps]
    row_size, col_size = len(maps), len(maps[0])

    for a in range(row_size):
        for b in range(col_size):
            if 0 <= a < row_size and 0 <= b < col_size and maps[a][b] != "X":
                summation = dfs(maps, a, b, int(maps[a][b]))
                if summation != 0:
                    answer.append(summation)

    if len(answer) == 0:
        answer = [-1]
    else:
        answer.sort()

    return answer