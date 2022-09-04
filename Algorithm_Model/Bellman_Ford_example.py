## Shortest Path - Bellman Ford Algorithm Example Code -- 이해 필요
## 특정 node -> 다른 모든 node로 가는 최단 경로 계산, 단 negative edge로 인한 negative cycle 발생 시 사용

# N개의 노드와 M개의 간선에 대해 간선 중 0의 cost와 (-)값의 cost를 갖는 간선이 존재할 때, 1번 node로부터 다른 모든 노드까지
# 가는 최단 경로를 계산하는 프로그램을 작성하라. (1 <= N <= 500, 1 <= M <= 6,000)

INF = int(1e9)

node_cnt, edge_cnt = map(int, input().split())
edges = []
distance = [INF] * (node_cnt + 1)

for _ in range(edge_cnt):
    a, b, c = map(int, input().split())         # 출발 노드(a) ~ 도착 노드(b) 까지의 걸리는 시간(c)
    edges.append((a, b, c))

def bellman_ford(start):
    distance[start] = 0

    for round in range(node_cnt):               # 모든 노드들에 대해 반복
        for idx in range(edge_cnt):             # 모든 간선들에 대해 반복
            before_node = edges[idx][0]         # 간선에 대한 정보 정의
            after_node = edges[idx][1]
            cost = edges[idx][2]

            if distance[before_node] != INF and distance[after_node] > distance[before_node] + cost:    # 거쳐 가는 경우가 더 짧다면
                distance[after_node] = distance[before_node] + cost     # distance table 갱신

                if round == node_cnt - 1:       # N번째 round에서도 갱신이 발생한다면
                    return True                 # 이 그래프는 (-) cycle을 포함
    return False

check_negative_cycle = bellman_ford(1)

if check_negative_cycle:
    print("This Graph has Negative Cycle")
else:
    for node in range(2, node_cnt + 1):
        if distance[node] == INF:
            print("Unreachable Node")
        else:
            print(distance[node])