## 문제 082. 다단계 칫솔 판매 --- 프로그래머스 Lv.3 연습 문제

from collections import deque


def dfs(name_to_cost, child_to_parent, start_name, start_cost):
    queue = deque()
    queue.append((start_name, start_cost))

    while queue:
        now_name, now_cost = queue.popleft()
        if now_name == "minho":
            name_to_cost[now_name] += now_cost
        else:
            if now_cost >= 10:
                parent_cost = int(now_cost * 0.1)
                child_cost = now_cost - parent_cost
                name_to_cost[now_name] += child_cost
                queue.append((child_to_parent[now_name], parent_cost))
            else:
                name_to_cost[now_name] += now_cost

    return name_to_cost


def solution(enroll, referral, seller, amount):
    answer = []

    add_calc = [[name, value * 100] for name, value in zip(seller, amount)]
    name_to_cost = {name: 0 for name in ["minho"] + enroll}

    child_to_parent = {}
    child_to_parent["minho"] = None
    for child, parent in zip(enroll, referral):
        if parent == "-":
            child_to_parent[child] = "minho"
        else:
            child_to_parent[child] = parent

    for start_name, start_cost in add_calc:
        name_to_cost = dfs(name_to_cost, child_to_parent, start_name, start_cost)

    for name in enroll:
        answer.append(name_to_cost[name])

    return answer