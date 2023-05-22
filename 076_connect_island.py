## 문제 076. 섬 연결하기 --- 프로그래머스 Lv.3 연습 문제

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

    return parent


def solution(n, costs):
    answer = 0

    parent = [num for num in range(n)]
    costs = sorted(costs, key=lambda x: x[2])
    for a, b, cost in costs:
        if find_parent(parent, a) != find_parent(parent, b):
            parent = union_parent(parent, a, b)
            answer += cost

    return answer