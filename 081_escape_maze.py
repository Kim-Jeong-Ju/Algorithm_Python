## 문제 081. 미로 탈출 --- 프로그래머스 Lv.2 연습 문제

import math
from collections import deque


def route_bfs(node, row, col, maps, array):
    da = [0, -1, 1, 0]  # Left, Up, Down, Right 순서
    db = [-1, 0, 0, 1]
    queue = deque()
    queue.append((node[0], node[1], 0))  # Row, Col, Cost 순서

    while queue:
        a, b, before_cost = queue.popleft()
        for direct in range(4):
            aa, bb = a + da[direct], b + db[direct]
            if 0 <= aa < row and 0 <= bb < col and maps[aa][bb] != "X":
                after_cost = before_cost + 1
                if array[aa][bb] > after_cost:
                    array[aa][bb] = after_cost
                    queue.append((aa, bb, after_cost))

    return array


def solution(maps):
    answer = 0

    row, col = len(maps), len(maps[0])
    start, mid, end = [], [], []
    for x in range(row):
        for y in range(col):
            if maps[x][y] == "S": start = [x, y]
            elif maps[x][y] == "L": mid = [x, y]
            elif maps[x][y] == "E": end = [x, y]
            else: pass

    array1 = [[math.inf for _ in range(col)] for _ in range(row)]
    array1[start[0]][start[1]] = 0
    array1 = route_bfs(start, row, col, maps, array1)

    if array1[mid[0]][mid[1]] != math.inf:
        answer += array1[mid[0]][mid[1]]

        array2 = [[math.inf for _ in range(col)] for _ in range(row)]
        array2[mid[0]][mid[1]] = 0
        array2 = route_bfs(mid, row, col, maps, array2)

        if array2[end[0]][end[1]] != math.inf:
            answer += array2[end[0]][end[1]]
        else:
            answer = -1
    else:
        answer = -1

    return answer