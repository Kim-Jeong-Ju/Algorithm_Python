## 문제 058. 아기 상어 --- 백준 No.16236

from collections import deque

def get_shortest_fish(array, now_x, now_y):
    fishes = []
    dist = [[0 for _ in range(N)] for _ in range(N)]
    dist[now_x][now_y] = 1
    queue = deque([[now_x, now_y]])

    while queue:
        a, b = queue.popleft()
        adjacents = [[a-1, b], [a, b-1], [a, b+1], [a+1, b]]
        for adj_a, adj_b in adjacents:
            if 0 <= adj_a < N and 0 <= adj_b < N and dist[adj_a][adj_b] == 0:
                if array[adj_a][adj_b] < array[now_x][now_y] and array[adj_a][adj_b] != 0:
                    dist[adj_a][adj_b] = dist[a][b] + 1
                    fishes.append((dist[adj_a][adj_b] - 1, adj_a, adj_b))
                elif array[adj_a][adj_b] == array[now_x][now_y] or array[adj_a][adj_b] == 0:
                    dist[adj_a][adj_b] = dist[a][b] + 1
                    queue.append([adj_a, adj_b])

    fishes = sorted(fishes, key=lambda x: (x[0], x[1], x[2]))
    return fishes


N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

now_x, now_y = -1, -1
for x in range(N):
    for y in range(N):
        if array[x][y] == 9: now_x, now_y = x, y

total_time, check = 0, [2, 0]
while True:
    array[now_x][now_y] = check[0]
    fishes = deque(get_shortest_fish(array, now_x, now_y))

    if not fishes: break

    min_dist, after_x, after_y = fishes.popleft()
    total_time += min_dist
    check[1] += 1

    if check[0] == check[1]:
        check[0] += 1
        check[1] = 0

    array[now_x][now_y] = 0
    now_x, now_y = after_x, after_y

print(total_time)