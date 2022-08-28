## DisJoint Set(서로소 집합 자료구조) Algorithm Example Code

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

cycle = False                       # 사이클 발생 여부 판별
for _ in range(edge):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
    else:
        union_parent(parent, a, b)

print("각 원소가 속한 집합(root) : ", end=" ")
for index in range(1, node + 1):
    print(find_parent(parent, index), end=" ")
print()

print("부모 테이블 : ", end=" ")
for index in range(1, node + 1):
    print(parent[index], end=" ")

if cycle:
    print("사이클이 발생했습니다")
else:
    print("사이클이 발생하지 않았습니다")