## Shortest Path - Floyd Warshall Algorithm Example Code
## 모든 node -> 다른 모든 node로 가는 최단 경로 계산

INF = int(1e9)
node, edge = map(int, input().split())
graph = [[INF] * (node + 1) for _ in range(node + 1)]

for _ in range(edge):
    a, b, c = map(int, input().split())
    graph[a][b] = c                         # 출발 node(a)에서 도착 node(b)로 가는 거리(c)

for index in range(1, node + 1):
    graph[index][index] = 0                 # 자기 자신으로 가는 경우의 최단 거리 = 0으로 초기화

for k in range(1, node + 1):                # 3중 반복문을 통해 점화식(DP)으로 최단 거리 갱신
    for a in range(1, node + 1):
        for b in range(1, node + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, node + 1):
    for b in range(1, node + 1):
        if graph[a][b] == INF:
            print("INFINITE distance", end=" ")
        else:
            print(graph[a][b], end=" ")