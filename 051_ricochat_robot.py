## 문제 051. 리코쳇 로봇 --- 프로그래머스 Lv.2 연습 문제

import heapq
from collections import defaultdict

INF = int(1e4)


def array_expand(array):
    result = ["D" * (len(array[0]) + 2)]
    for row in array:
        result.append("D" + row + "D")
    result.append("D" * (len(array[0]) + 2))

    return result


def get_coords(array):
    can_move = []
    x_wall, y_wall = defaultdict(list), defaultdict(list)
    start, end = 0, 0

    for a in range(len(array)):
        for b in range(len(array[0])):
            if array[a][b] == "D":
                x_wall[a].append((a, b))
                y_wall[b].append((a, b))
                continue
            elif array[a][b] == "R":
                start = (a, b)
            elif array[a][b] == "G":
                end = (a, b)

            can_move.append((a, b))

    return can_move, x_wall, y_wall, start, end


def convert_graph(can_move, x_wall, y_wall):
    graph = defaultdict(list)
    for x, y in can_move:
        top_x, bot_x, left_y, right_y = INF, -1, -1, INF
        for a, b in x_wall[x]:
            if y > b: left_y = max(left_y, b)
            if y < b: right_y = min(right_y, b)
        for c, d in y_wall[y]:
            if x < c: top_x = min(top_x, c)
            if x > c: bot_x = max(bot_x, c)

        avails = [(top_x - 1, y), (bot_x + 1, y), (x, left_y + 1), (x, right_y - 1)]
        for avail in avails:
            if avail[0] == x and avail[1] == y: continue
            graph[(x, y)].append(avail)

    return graph


def dijkstra(graph, start):
    count = {coord: INF for coord in graph.keys()}
    count[start] = 0
    queue = []
    heapq.heappush(queue, (count[start], start))

    while queue:
        now_count, now_coord = heapq.heappop(queue)
        if count[now_coord] < now_count: continue
        for adj_coord in graph[now_coord]:
            adj_count = now_count + 1
            if count[adj_coord] > adj_count:
                count[adj_coord] = adj_count
                heapq.heappush(queue, (count[adj_coord], adj_coord))

    return count


def solution(board):
    answer = 0

    board = array_expand(board)
    can_move, x_wall, y_wall, start, end = get_coords(board)
    graph = convert_graph(can_move, x_wall, y_wall)
    count = dijkstra(graph, start)

    if count[end] != INF:
        answer = count[end]
    else:
        answer = -1

    return answer