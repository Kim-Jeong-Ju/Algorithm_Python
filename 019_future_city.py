## 문제 019. 미래 도시

# 1번부터 N번까지의 회사가 서로 연결되어 있으며, 두 회사를 연결하는 도로는 양방향으로 이동 가능하다. 각 회사를 이동 시 정확히 1만큼의 시간이
# 소요되며, 방문 판매원 A는 1번 회사에서 출발하여 K번 회사를 거쳐 X번 회사로 가는 것이 목표일 때, A가 회사 사이를 이동하는 최단 시간을
# 구하는 프로그램을 작성하라.

# Input : 첫째 줄에 회사의 갯수 N과 도로의 갯수 M 입력 (1 <= N, M <= 100)
#         둘째 줄부터 M+1번째 줄까지 연결된 두 회사의 번호 입력, M+2번째 줄에는 X와 K가 공백으로 입력 (1 <= K <= 100)
# Output : 최소 이동 시간 출력, 단 도달할 수 없을 경우 -1 출력

INF = int(1e9)

node, edge = map(int, input().split())
graph = [[INF] * (node + 1) for _ in range(node + 1)]

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
for index in range(1, node + 1):
    graph[index][index] = 0

end, mid = map(int, input().split())

for k in range(1, node + 1):
    for a in range(1, node + 1):
        for b in range(1, node + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = graph[1][mid] + graph[mid][end]
if result >= INF:
    print(-1)
else:
    print(result)