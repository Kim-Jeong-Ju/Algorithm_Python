## 문제 067. 가장 먼 노드 --- 프로그래머스 Lv.3 연습 문제

import heapq
INF = 20000

def dijkstra(graph, count, start):
    queue = []
    heapq.heappush(queue, (0, start))
    count[start] = 0

    while queue:
        now_dist, now_node = heapq.heappop(queue)
        if count[now_node] < now_dist:
            continue

        for adj_node in graph[now_node]:
            temp_dist = count[now_node] + 1
            if count[adj_node] > temp_dist:
                count[adj_node] = temp_dist
                heapq.heappush(queue, (temp_dist, adj_node))

    return count


def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n + 1)]
    for info in edge:
        start, end = info
        graph[start].append(end)
        graph[end].append(start)

    count = {node + 1: INF for node in range(n)}
    count = dijkstra(graph, count, 1)
    count_temp = sorted(count.values(), reverse=True)

    maxi = count_temp[0]
    for value in count_temp:
        if maxi == value:
            answer += 1
        else:
            break

    return answer