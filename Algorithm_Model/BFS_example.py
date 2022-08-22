## BFS(Breadth-First Search) Algorithm Example Code

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])             # deque 라이브러리로 empty queue 생성

    visited[start] = True       # 현재 확인중인 첫번째 start node를 방문 처리

    while queue:                    # 큐 내의 원소가 빌 때까지 반복
        node = queue.popleft()      # 큐에서 원소 하나 꺼내기
        print(node, end=" ")

        for vertex in graph[node]:          # 꺼낸 원소(node)와 인접한 node들을 모두 확인하며
            if not visited[vertex]:         # 방문 처리가 되어있지 않은 node라면
                queue.append(vertex)        # 큐에 삽입
                visited[vertex] = True      # 이후 그 node 방문 처리

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9    # 방문 여부를 기록하는 list -> 0번째 index까지 추가하여 총 9개 원소로 구성

bfs(graph, 1, visited)