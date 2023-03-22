## 문제 049. 여행 경로 --- 프로그래머스 Lv.3 연습 문제

from collections import defaultdict

def solution(tickets):
    answer = []

    flights = defaultdict(list)
    for depart, arrive in tickets:
        flights[depart] += [arrive]
    flights = {depart: sorted(arrive, reverse=True) for depart, arrive in flights.items()}

    stack, route = ["ICN"], []
    while stack:
        now = stack[-1]
        if now not in flights.keys() or len(flights[now]) == 0:
            route.append(stack.pop())
        else:
            stack.append(flights[now][-1])
            flights[now].pop()

    answer = route[::-1]
    return answer