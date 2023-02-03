## 문제 033. 숫자 변환하기 --- 프로그래머스 Lv.2 연습 문제

from collections import deque

def bfs(x, n, dp):
    queue = deque([x])
    dp[x] = 1

    while queue:
        now = queue.popleft()

        if now + n <= 1000000 and dp[now + n] == 0:
            dp[now + n] = dp[now] + 1
            queue.append(now + n)
        if now * 2 <= 1000000 and dp[now * 2] == 0:
            dp[now * 2] = dp[now] + 1
            queue.append(now * 2)
        if now * 3 <= 1000000 and dp[now * 3] == 0:
            dp[now * 3] = dp[now] + 1
            queue.append(now * 3)

    return dp


def solution(x, y, n):
    answer = 0

    dp = [0] * 1000001
    dp = bfs(x, n, dp)
    answer = dp[y] - 1

    return answer