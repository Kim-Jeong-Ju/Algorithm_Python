## 문제 044. 합승 택시 요금 --- 프로그래머스 Lv.3 연습 문제

INF = int(1e8)

def solution(n, s, a, b, fares):
    answer = 0

    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for fare in fares:
        aa, bb, cost = map(int, fare)
        graph[aa][bb] = cost
        graph[bb][aa] = cost

    for num in range(1, n + 1):
        graph[num][num] = 0

    for K in range(1, n + 1):
        for A in range(1, n + 1):
            for B in range(1, n + 1):
                graph[A][B] = min(graph[A][B], graph[A][K] + graph[K][B])

    answer = min(graph[s][k] + graph[k][a] + graph[k][b] for k in range(1, n + 1))
    return answer