## Shortest Path - Dijkstra Algorithm Example Code
## 특정 node -> 다른 모든 node로 가는 최단 경로 계산

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

node, edge = map(int, input().split())
start = int(input())




graph1 = [[] for _ in range(node + 1)]       # graph 초기화
visited = [False] * (node + 1)              # 방문 여부를 기록하는 list 초기화
distance1 = [INF] * (node + 1)               # 최단 거리를 기록하는 table 초기화

for _ in range(edge):
    a, b, c = map(int, input().split())     # 출발 노드(a) ~ 도착 노드(b) 까지의 거리(c)
    graph1[a].append((b, c))                 # graph에는 index = 출발 노드, value = (도착 노드, 거리)

def get_shortest_node():                    # 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 반환
    min_value = INF
    idx = 0                                 # 다른 노드를 거쳐갈 때 최단 거리가 나오는 경우, 거쳐가는 노드 번호
    for i in range(node + 1):
        if distance1[i] < min_value and not visited[i]:
            min_value = distance1[i]
            idx = i
    return idx

def normal_dijkstra(start):                  # 일반적인 다익스트라 알고리즘 구현
    distance1[start] = 0                     # 출발 노드에 대한 최단 거리/방문 처리 초기화
    visited[start] = True
    for info in graph1[start]:
        distance1[info[0]] = info[1]

    for a in range(node - 1):                # 출발 노드를 제외한 나머지 모든 노드들에 대하여
        now = get_shortest_node()            # 현재 방문하지 않았으면서 최단 거리가 가장 짧은 노드 반환
        visited[now] = True                  # 방문 처리
        for b in graph1[now]:                # 확인 중인 노드와 연결된 노드들에 대하여
            cost = distance1[now] + b[1]     # 확인 중인 노드를 거쳐갔을 때의 거리 계산
            if cost < distance1[b[0]]:       # "계산한 거리값 < 원래 저장했던 최단 거리"이면
                distance1[b[0]] = cost       # 최단 거리 table 갱신

normal_dijkstra(start)

for vertex in range(node + 1):
    if distance1[vertex] != INF:
        print(distance1[vertex])
    else:
        print("INFINITE distance")




graph2 = [[] for _ in range(node + 1)]       # graph 초기화
distance2 = [INF] * (node + 1)               # 최단 거리를 기록하는 table 초기화

for _ in range(edge):
    a, b, c = map(int, input().split())      # 출발 노드(a) ~ 도착 노드(b) 까지의 거리(c)
    graph2[a].append((b, c))                 # graph에는 index = 출발 노드, value = (도착 노드, 거리)

def queue_dijkstra(start):                          # 우선순위 큐를 이용한 다익스트라 알고리즘 구현
    queue = []
    heapq.heappush(queue, (0, start))               # queue에는 (인접 node, 거리)가 아닌 (거리, 인접 node)로 저장
    distance2[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance2[now] < dist:
            continue

        for info in graph2[now]:
            cost = dist + info[1]                           # 현재 확인중인 노드를 거쳐 가는 경우의 거리 계산
            if distance2[info[0]] > cost:                   # 거쳐 가는 거리가 원래 저장되어 있던 거리보다 짧다면
                distance2[info[0]] = cost                   # 최단 거리 table 갱신
                heapq.heappush(queue, (cost, info[0]))      # queue에 추가

queue_dijkstra(start)

for vertex in range(node + 1):
    if distance2[vertex] != INF:
        print(distance2[vertex])
    else:
        print("INFINITE distance")