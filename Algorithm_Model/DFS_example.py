## DFS(Depth-First Search) Algorithm Example Code

def dfs(graph, node, visited):
    visited[node] = True                    # 현재 확인중인 node를 방문 처리

    print(node, end=" ")

    for vertex in graph[node]:              # 현재 확인중인 node와 연결된 다른 node들에 대하여
        if not visited[vertex]:             # 이들을 방문하지 않았다면
            dfs(graph, vertex, visited)     # 재귀적으로 DFS 실행

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

dfs(graph, 1, visited)