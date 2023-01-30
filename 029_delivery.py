## 문제 029. 배달 --- 프로그래머스 Lv.2 연습 문제

import heapq
INF = int(1e9)

def dijkstra(graph, start, dist):
    queue = []
    heapq.heappush(queue, (0, start))  # 길이(c), 도착지점(b) 순서
    dist[start] = 0

    while queue:
        now_dist, now = heapq.heappop(queue)

        if dist[now] < now_dist:
            continue

        for adj, adj_dist in graph[now]:
            new_dist = now_dist + adj_dist
            if dist[adj] > new_dist:
                dist[adj] = new_dist
                heapq.heappush(queue, (new_dist, adj))

    return dist


def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N)]
    dist = [INF for _ in range(N)]

    for info in road:
        a, b, c = info[0], info[1], info[2]
        graph[a - 1].append((b - 1, c))  # 도착지점(b), 길이(c) 순서
        graph[b - 1].append((a - 1, c))

    dist = dijkstra(graph, 0, dist)
    for cost in dist:
        if cost <= K:
            answer += 1

    return answer