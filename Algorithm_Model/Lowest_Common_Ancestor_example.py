## Lowest Common Ancestor(LCA, 최소 공통 조상) Algorithm Example Code -- 이해 필요
## 최소 공통 조상을 구하는 문제의 경우, 최악의 경우에도 시간복잡도 O(NM)을 보장 -> N = 노드의 갯수, M = 쿼리의 갯수
## 개선된 LCA Algorithm의 시간복잡도 = O(MlogN)

# 1번 노드를 root로 하며 총 N개의 노드를 갖는 tree에 대하여 두 node 쌍이 M개가 주어졌을 때, 두 노드의
# 가장 가까운 공통 조상의 node를 구하는 프로그램을 작성하라. 실행 시간 제한은 O(NM)이다.
# 단, 2 <= N <= 50,000, 1 <= M <= 10,000

import sys
sys.setrecursionlimit(int(1e5))     # Run-Time Error를 피하기 위한 제한 시간 설정

LOG = 21

n = int(input())
normal_parent = [0] * (n + 1)                           # 각 node들의 부모 node에 대한 정보 table
advanced_parent = [[0] * LOG for _ in range(n + 1)]     # 각 node들의 2^i번째 부모 node들까지 기록하는 table
depth = [0] * (n + 1)                                   # 각 node들의 깊이값에 대한 정보 table
is_calc = [False] * (n + 1)                             # 각 node들의 깊이를 계산했는지에 대한 여부를 기록하는 table
graph = [[] for _ in range(n + 1)]                      # 그래프에 대한 정보

for _ in range(n - 1):                  # 그래프에서 인접한 node에 대한 정보 입력
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def normal_dfs_depth(node, height):                # 각 node들의 깊이값을 구하는 함수
    is_calc[node] = True                           # 깊이값을 계산했다는 처리
    depth[node] = height                           # 현재 탐색하고 있는 node의 깊이 기록

    for adjacent in graph[node]:                   # 현재 탐색하고 있는 node와 인접한 모든 node들에 대하여
        if is_calc[adjacent]:                      # 이전에 이미 깊이를 계산했다면 continue 처리
            continue

        normal_parent[adjacent] = node             # "인접 node의 부모 node = 현재 탐색하고 있는 node"로 처리
        normal_dfs_depth(adjacent, height + 1)     # 인접 node의 깊이 계산 -> 재귀 호출

def advanced_dfs_depth(node, height):
    is_calc[node] = True
    depth[node] = height

    for adjacent in graph[node]:
        if is_calc[adjacent]:
            continue

        advanced_parent[adjacent][0] = node        # "인접 node의 직계 부모 node = 현재 탐색하고 있는 node"로 처리
        advanced_dfs_depth(adjacent, height + 1)

def set_parent():                                  # 2^a ~ 2^LOG번째 부모들을 모두 기록하는 과정 수행
    advanced_dfs_depth(1, 0)

    for a in range(1, LOG):
        for b in range(1, n + 1):
            advanced_parent[b][a] = advanced_parent[advanced_parent[b][a - 1]][a - 1]       # 2^i = 2^(i-1) + 2^(i-1)

def normal_lca(a, b):                       # 일반적인 최소 공통 조상(LCA)를 찾는 함수
    while depth[a] != depth[b]:             # 두 노드의 깊이가 다르다면 깊이를 맞춰주는 반복 수행
        if depth[a] > depth[b]:
            a = normal_parent[a]
        else:
            b = normal_parent[b]

    while a != b:                           # 두 노드의 조상이 같아질때 까지 거슬러 올라가는 동작 수행
        a = normal_parent[a]
        b = normal_parent[b]

    return a

def advanced_lca(a, b):                     # 개선된 최소 공통 조상(LCA)를 찾는 함수 -> 2^i번째 부모node들을 기록하는 별도의 table 추가하여 시간복잡도 감소
    if depth[a] > depth[b]:                 # a노드보다 b노드의 깊이를 더 깊게 설정
        a, b = b, a

    for i in range(LOG - 1, -1, -1):        # LOG-1 부터 (-1)+1=0 까지 -1씩 감소하며 반복 수행
        if depth[b] - depth[a] >= (1 << i):
            b = advanced_parent[b][i]

    if a == b:
        return a

    for i in range(LOG - 1, -1, -1):
        if advanced_parent[a][i] != advanced_parent[b][i]:
            a = advanced_parent[a][i]
            b = advanced_parent[b][i]

    return advanced_parent[a][0]

normal_dfs_depth(1, 0)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(normal_lca(a, b))
print()
set_parent()
for _ in range(m):
    a, b = map(int, input().split())
    print(advanced_lca(a, b))