## 문제 056. 원판 돌리기 --- 백준 No.17822

def make_graph(N, M):                   # 인접한 node_index를 tuple 형태로 명시하는 graph 계산하는 function
    graph = {(row, col): [] for row in range(N) for col in range(M)}
    for a in range(N):
        for b in range(M):
            if a == 0:
                if b != M-1:                    # 가장 안쪽 원이면서 j != M 인 경우
                    graph[(a, b)].extend([(a, b-1), (a, b+1), (a+1, b)])
                else:                           # 가장 안쪽 원이면서 j == M 인 경우
                    graph[(a, b)].extend([(a, b-1), (a, 0), (a+1, b)])
            elif a == N-1:
                if b != M-1:                    # 가장 바깥쪽 원이면서 j != M 인 경우
                    graph[(a, b)].extend([(a-1, b), (a, b-1), (a, b+1)])
                else:                           # 가장 바깥쪽 원이면서 j == M 인 경우
                    graph[(a, b)].extend([(a-1, b), (a, b-1), (a, 0)])
            else:
                if b != M-1:                    # 중간에 있는 원이면서 j != M 인 경우
                    graph[(a, b)].extend([(a-1, b), (a, b-1), (a, b+1), (a+1, b)])
                else:                           # 중간에 있는 원이면서 j == M 인 경우
                    graph[(a, b)].extend([(a-1, b), (a, b-1), (a, 0), (a+1, b)])

    return graph


def disk_rotate(array, command):        # 회전 연산을 수행하는 function
    disk_idx, direct, size = command
    if direct == 0:         # 시계 방향으로 회전, idx ++ 1
        for a in range(disk_idx, len(array)+1, disk_idx):
            array[a-1] = array[a-1][-size:] + array[a-1][:-size]
    else:                   # 반시계 방향으로 회전, idx -- 1
        for b in range(disk_idx, len(array)+1, disk_idx):
            array[b-1] = array[b-1][size:] + array[b-1][:size]

    return array


def calc_num(array, graph, N, M):
    adj_keys = []
    for x, y in graph.keys():
        for adj_x, adj_y in graph[(x, y)]:
            if array[x][y] != 0 and array[adj_x][adj_y] == array[x][y]:
                if (x, y) not in adj_keys: adj_keys.append((x, y))
                if (adj_x, adj_y) not in adj_keys: adj_keys.append((adj_x, adj_y))

    if len(adj_keys) != 0:
        for row, col in adj_keys:
            array[row][col] = 0
    else:
        summation, zero_cnt = 0, 0
        for disk in array:
            summation += sum(disk)
            if 0 in disk: zero_cnt += disk.count(0)

        if zero_cnt != N * M:
            avg = summation / ((N * M) - zero_cnt)
        else:
            avg = 0

        for row in range(N):
            for col in range(M):
                if array[row][col] != 0:
                    if array[row][col] > avg: array[row][col] -= 1
                    elif array[row][col] < avg: array[row][col] += 1

    return array


N, M, T = map(int, input().split())

disks, commands = [], []
for _ in range(N):
    disks.append(list(map(int, input().split())))
for _ in range(T):
    commands.append(list(map(int, input().split())))

graph = make_graph(N, M)
for t in range(T):
    disks = disk_rotate(disks, commands[t])
    disks = calc_num(disks, graph, N, M)

answer = 0
for disk in disks:
    answer += sum(disk)

print(answer)