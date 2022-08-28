## 문제 018. 전보

# 서로 연결되어 있는 N개의 도시들에 대해, C라는 도시에서 최대한 많은 다른 도시들에 전보를 보내고자 할 때,
# 전보를 받게 되는 도시의 수와 각각 전보를 받기까지 걸린 시간을 구하는 프로그램을 작성하라.

# Input : 첫째 줄에 도시의 갯수 N, 통로의 갯수 M, 메시지를 보내는 도시 C 입력 (1 <= N <= 30,000, 1 <= M <= 200,000, 1 <= C <= N)
#         둘째 줄부터 M+1번째 줄까지 통로에 대한 정보 X(출발 도시), Y(도착 도시), Z(소요 시간) 입력
# Output : C가 보낸 메시지를 받는 도시의 수, 총 소요 시간을 공백 기준으로 출력

import heapq

INF = int(1e9)

node, edge, start = map(int, input().split())
graph = [[] for _ in range(node + 1)]
distance = [INF] * (node + 1)

for _ in range(edge):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))                 # 출발 도시(x) ~ 도착 도시(y) 까지의 걸린 시간(z)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))       # queue에 삽입할 때는 (거리, 인접 node) 순서로
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for info in graph[now]:
            cost = dist + info[1]
            if cost < distance[info[0]]:
                distance[info[0]] = cost
                heapq.heappush(queue, (cost, info[0]))

dijkstra(start)

count = 0
time = 0
for index in range(len(distance)):
    if distance[index] != INF and index != start:
        count += 1
        time = max(time, distance[index])

print(count, time)