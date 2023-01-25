## 문제 028. 행렬 테두리 회전하기 - 프로그래머스 Lv.2 연습 문제

def min_take(array, rows, cols, a, b, c, d):
    mini = rows * cols
    for A in range(a+1, c+1):       # left side
        if mini >= array[A][b]: mini = array[A][b]
    for B in range(a, c):           # right side
        if mini >= array[B][d]: mini = array[B][d]
    for C in range(b, d):           # up side
        if mini >= array[a][C]: mini = array[a][C]
    for D in range(b+1, d+1):       # down side
        if mini >= array[c][D]: mini = array[c][D]

    return mini


def align(array, a, b, c, d):
    temp = array[a][b]
    for aa in range(a+1, c+1):                  # left side
        array[aa-1][b] = array[aa][b]
    for bb in range(b+1, d+1):                  # down side
        array[c][bb-1] = array[c][bb]
    for cc in range(c-1, a-1, -1):              # right side
        array[cc+1][d] = array[cc][d]
    for dd in range(d-1, b-1, -1):              # up side
        array[a][dd+1] = array[a][dd]
    array[a][b+1] = temp

    return array


def solution(rows, cols, queries):
    answer = []

    if len(queries) == 1:
        x, y = queries[0][0], queries[0][1]
        value = ((x - 1) * cols) + y
        answer.append(value)
    else:
        array = [[a for a in range((b * cols) + 1, (b + 1) * cols + 1)] for b in range(rows)]
        for query in queries:
            a, b, c, d = query[0]-1, query[1]-1, query[2]-1, query[3]-1
            answer.append(min_take(array, rows, cols, a, b, c, d))
            array = align(array, a, b, c, d)

    return answer