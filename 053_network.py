## 문제 053. 네트워크 --- 프로그래머스 Lv.3 연습 문제

def dfs(graph, node, visited, network):
    visited[node] = True
    network.append(node)

    for adjacent in graph[node]:
        if visited[adjacent] == False:
            dfs(graph, adjacent, visited, network)

    return network


def solution(n, computers):
    answer = 0

    graph = [[] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            if a != b and computers[a][b] == 1:
                graph[a].append(b)
                graph[b].append(a)
    for c in range(n):
        graph[c] = sorted(list(set(graph[c])))

    visited = [False for _ in range(n)]
    coms = [num for num in range(n)]
    check_net = []
    while False in visited:
        for com in coms:
            if com not in check_net:
                check_net.extend(dfs(graph, com, visited, check_net))
                answer += 1

    return answer