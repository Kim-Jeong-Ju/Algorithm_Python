## Minimum Spanning Tree(최소 신장 트리) - Kruskal's Algorithm Example Code

def find_parent(parent, x):         # 특정 원소가 속한 집합을 찾는 과정 -> 자기 자신을 root로 할 때까지 반복
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    else:
        return parent[x]

def union_parent(parent, a, b):     # 특정 두 원소를 하나의 집합으로 합치는 과정 -> 노드 번호가 작은 쪽이 부모가 되도록
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

node, edge = map(int, input().split())
parent = [0] * (node + 1)
for index in range(1, node + 1):    # 부모 테이블을 자기 자신으로 초기화
    parent[index] = index

edges = []                          # edge들의 정보를 담을 list 초기화
total_mst_cost = 0                  # 최소 신장 트리에 모든 edge cost의 합

for _ in range(edge):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))              # (거리, 출발, 도착) 순으로 삽입
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):    # 두 노드의 root가 같지 않은 것들끼리
        union_parent(parent, a, b)                          # 합치기 연산 수행
        total_mst_cost += cost

print(total_mst_cost)