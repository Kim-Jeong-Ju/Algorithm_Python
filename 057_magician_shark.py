## 문제 057. 마법사 상어와 비바라기 --- 백준 No.17822

def after_move(now_cloud, command, N):
    direct, size = command[0], command[1]

    if direct == 1:         # 왼쪽 : y만 감소
        for a, [cloud_x, cloud_y] in enumerate(now_cloud):
            cloud_y -= size
            if cloud_y < 0:
                cloud_y += N * ((abs(cloud_y) // N) + 1)
                if cloud_y % N == 0: cloud_y = 0
            else: pass
            now_cloud[a] = [cloud_x, cloud_y]
    elif direct == 2:       # 왼쪽 위 대각선 : x&y 모두 감소
        for b, [cloud_x, cloud_y] in enumerate(now_cloud):
            cloud_x -= size
            cloud_y -= size
            if cloud_x < 0:
                cloud_x += (N * ((abs(cloud_x) // N) + 1))
                if cloud_x % N == 0: cloud_x = 0
            else: pass
            if cloud_y < 0:
                cloud_y += N * ((abs(cloud_y) // N) + 1)
                if cloud_y % N == 0: cloud_y = 0
            else: pass
            now_cloud[b] = [cloud_x, cloud_y]
    elif direct == 3:       # 위 : x만 감소
        for c, [cloud_x, cloud_y] in enumerate(now_cloud):
            cloud_x -= size
            if cloud_x < 0:
                cloud_x += (N * ((abs(cloud_x) // N) + 1))
                if cloud_x % N == 0: cloud_x = 0
            else: pass
            now_cloud[c] = [cloud_x, cloud_y]
    elif direct == 4:       # 오른쪽 위 대각선 : x 감소 y 증가
        for d, [cloud_x, cloud_y] in enumerate(now_cloud):
            cloud_x -= size
            cloud_y += size
            if cloud_x < 0:
                cloud_x += (N * ((abs(cloud_x) // N) + 1))
                if cloud_x % N == 0: cloud_x = 0
            else: pass
            if cloud_y >= N: cloud_y = cloud_y % N
            else: pass
            now_cloud[d] = [cloud_x, cloud_y]
    elif direct == 5:       # 오른쪽 : y만 증가
        for e, [cloud_x, cloud_y] in enumerate(now_cloud):
            cloud_y += size
            if cloud_y >= N: cloud_y = cloud_y % N
            else: pass
            now_cloud[e] = [cloud_x, cloud_y]
    elif direct == 6:       # 오른쪽 아래 대각선 : x&y 모두 증가
        for f, [cloud_x, cloud_y] in enumerate(now_cloud):
            cloud_x += size
            cloud_y += size
            if cloud_x >= N: cloud_x = cloud_x % N
            else: pass
            if cloud_y >= N: cloud_y = cloud_y % N
            else: pass
            now_cloud[f] = [cloud_x, cloud_y]
    elif direct == 7:       # 아래 : x만 증가
        for g, [cloud_x, cloud_y] in enumerate(now_cloud):
            cloud_x += size
            if cloud_x >= N: cloud_x = cloud_x % N
            else: pass
            now_cloud[g] = [cloud_x, cloud_y]
    else:                   # 왼쪽 아래 대각선 : x 증가 y 감소
        for h, [cloud_x, cloud_y] in enumerate(now_cloud):
            cloud_x += size
            cloud_y -= size
            if cloud_x >= N: cloud_x = cloud_x % N
            else: pass
            if cloud_y < 0:
                cloud_y += N * ((abs(cloud_y) // N) + 1)
                if cloud_y % N == 0: cloud_y = 0
            else: pass
            now_cloud[h] = [cloud_x, cloud_y]

    return now_cloud


def add_water(array, now_cloud, visited, N):
    for cloud_x, cloud_y in now_cloud:
        array[cloud_x][cloud_y] += 1

    for cloud_x, cloud_y in now_cloud:
        count = 0
        if cloud_x-1 >= 0 and cloud_y-1 >= 0 and array[cloud_x-1][cloud_y-1] > 0: count += 1    # 왼쪽 위 대각선
        if cloud_x-1 >= 0 and cloud_y+1 < N and array[cloud_x-1][cloud_y+1] > 0: count += 1     # 오른쪽 위 대각선
        if cloud_x+1 < N and cloud_y-1 >= 0 and array[cloud_x+1][cloud_y-1] > 0: count += 1     # 왼쪽 아래 대각선
        if cloud_x+1 < N and cloud_y+1 < N and array[cloud_x+1][cloud_y+1] > 0: count += 1      # 오른쪽 아래 대각선
        array[cloud_x][cloud_y] += count
        visited[cloud_x][cloud_y] = True

    return array, visited


def next_cloud(array, visited):
    next_cloud = []

    for row in range(N):
        for col in range(N):
            if visited[row][col] == False and array[row][col] >= 2:
                next_cloud.append([row, col])
                array[row][col] -= 2

    return next_cloud


N, M = map(int, input().split())
array, commands = [], []
for _ in range(N):
    array.append(list(map(int, input().split())))
for _ in range(M):
    commands.append(list(map(int, input().split())))

now_cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
for command in commands:
    visited = [[False for _ in range(N)] for _ in range(N)]
    now_cloud = after_move(now_cloud, command, N)
    array, visited = add_water(array, now_cloud, visited, N)
    now_cloud = next_cloud(array, visited)

print(sum([sum(water) for water in array]))