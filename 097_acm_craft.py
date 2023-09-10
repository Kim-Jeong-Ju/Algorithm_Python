## 문제 097. ACM Craft --- 백준 No.1005
## Nested Connection(예제 입력 2의 3번째 case)에 대한 처리 필요
## Tip) Topology Sorting(위상 정렬) & Memoization with DP(다이나믹 프로그래밍)

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for test in range(T):
    answer = 0

    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    links = [-1] + [0] * N

    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        before, after = map(int, input().split())
        graph[before].append(after)
        links[after] += 1
    point = int(input())

    dp = [0] * (N+1)
    queue = deque()
    for idx in range(1, N+1):
        if links[idx] == 0:
            queue.append(idx)
            dp[idx] = times[idx]

    while queue:
        A_node = queue.popleft()
        for B_node in graph[A_node]:
            links[B_node] -= 1
            dp[B_node] = max(dp[B_node], dp[A_node] + times[B_node])
            if links[B_node] == 0: queue.append(B_node)

        if links[point] == 0:
            answer = dp[point]
            break

    print(answer)