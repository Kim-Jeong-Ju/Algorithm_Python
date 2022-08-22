## 문제 009. 미로 탈출

# N X M 직사각형 형태의 미로에 대하여 출발점인 (1, 1)에서 탈출점인 (N, M)까지 괴물이 있는 0은 피하고 괴물이
# 없는 1 부분을 지나가며 탈출해야 한다. 탈출하기 위해 최소한으로 움직여야 하는 칸 수를 구하는 프로그램을 작성하라.

# Input : 첫째 줄에 미로의 크기 N과 M 입력 (4 <= N, M <= 200)
#         둘째 줄부터 N+1번째 줄까지 각각 M개의 미로의 정보 입력
# Output : 최소로 이동 가능한 칸의 갯수 출력

from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):      # 미로 정보 입력
    graph.append(list(map(int, input())))

dx = [0, 0, -1, +1]     # 좌우상하 순서
dy = [-1, +1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()      # 큐에서 원소 하나 꺼내기
        for i in range(4):
            after_x = x + dx[i]     # 모든 경우에 따라 이동 후의 좌표
            after_y = y + dy[i]

            if after_x < 0 or after_x >= n or after_y < 0 or after_y >= m:      # 미로를 벗어나는 경우 무시
                continue

            if graph[after_x][after_y] == 0:    # 괴물이 있는 곳은 무시
                continue
            if graph[after_x][after_y] == 1:
                graph[after_x][after_y] = graph[x][y] + 1   # 현재의 위치 + 1 = 다음 갈 곳의 위치 : 이제까지 거쳐온 칸의 갯수
                queue.append((after_x, after_y))    # 다음 갈 곳의 위치를 큐에 삽입

    return graph[n-1][m-1]      # 최종 탈출점까지 거쳐온 칸의 갯수 출력

print(bfs(0, 0))