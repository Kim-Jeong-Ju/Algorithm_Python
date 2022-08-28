## Topology Sorting Algorithm Example Code

from collections import deque

node, edge = map(int, input().split())
indegree = [0] * (node + 1)                 # 각 노드별 진입 차수를 기록하는 list
graph = [[] for _ in range(node + 1)]

for _ in range(edge):
    a, b = map(int, input().split())        # 출발 노드(a) ~ 도착 노드(b)
    graph[a].append(b)
    indegree[b] += 1                        # 도착 노드(b)의 진입 차수 1 증가

def topology_sort():
    after_topol_sort = []                   # 위상 정렬 수행 후 결과를 담을 array
    queue = deque()                         # empty queue 초기화 및 생성
    for index in range(1, node + 1):        # 모든 노드에 대하여
        if indegree[index] == 0:            # 진입 차수가 0인 노드들을
            queue.append(index)             # queue에 삽입

    while queue:
        now = queue.popleft()               # queue에서 노드 하나를 꺼내
        after_topol_sort.append(now)        # 위상 정렬 수행한 결과 array에 삽입
        for vertex in graph[now]:           # 현재 꺼낸 노드와 인접한 모든 노드들에 대해
            indegree[vertex] -= 1           # 진입 차수를 하나 제거
            if indegree[vertex] == 0:       # 새롭게 진입 차수 = 0이 된 노드들을
                queue.append(vertex)        # 새롭게 queue에 삽입

    for idx in after_topol_sort:
        print(idx, end=" ")

topology_sort()