## 문제 020. 마법사 상어와 토네이도 - 백준 No.20057

# Input : 첫째 줄에 격자의 크기 N 입력 (3 <= N <= 499)
#         둘째 줄부터 N+1번째 줄까지 각각의 격자 칸에 존재하는 모래의 양 A[r][c] 입력 (0 <= A[r][c] <= 1,000)
#         정 가운데 칸에 있는 모래의 양은 0
# Output : 격자 밖으로 나가게 되는 모래 양의 총합

import math

N = int(input())
center = N // 2

array = []
for _ in range(N):
    each_row = list(map(int, input().split()))
    array.append(each_row)

start_x, start_y = center, center

def left_move(graph, before_x, before_y, N):              #  왼쪽으로 1칸 움직이는 경우
    after_x = before_x
    after_y = before_y - 1

    array[after_x][after_y] += array[before_x][before_y]

    out_sum = 0

    if after_y - 2 < 0:          # 5% 칸 계산
        out_sum += math.floor(array[after_x][after_y-2] + (array[after_x][after_y] * 0.05))
    else:
        array[after_x][after_y-2] += array[after_x][after_y] * 0.05

    if after_x - 1 < 0 or after_y - 1 < 0:        # 위쪽 10% 칸 계산
        out_sum += math.floor(array[after_x-1][after_y-1] + (array[after_x][after_y] * 0.1))
    else:
        array[after_x-1][after_y-1] += array[after_x][after_y] * 0.1
    if after_x + 1 >= N or after_y - 1 < 0:        # 아래쪽 10% 칸 계산
        out_sum += math.floor(array[after_x+1][after_y-1] + (array[after_x][after_y] * 0.1))
    else:
        array[after_x+1][after_y-1] += array[after_x][after_y] * 0.1

    if after_x - 2 < 0:        # 위쪽 2% 칸 계산
        out_sum += math.floor(array[after_x-2][after_y] + (array[after_x][after_y] * 0.02))
    else:
        array[after_x-2][after_y] += array[after_x][after_y] * 0.02
    if after_x + 2 >= N:        # 아래쪽 2% 칸 계산
        out_sum += math.floor(array[after_x+2][after_y] + (array[after_x][after_y] * 0.02))
    else:
        array[after_x+2][after_y] += array[after_x][after_y] * 0.02

    if after_x - 1 < 0:        # 위쪽 7% 칸 계산
        out_sum += math.floor(array[after_x-1][after_y] + (array[after_x][after_y] * 0.07))
    else:
        array[after_x-1][after_y] += array[after_x][after_y] * 0.07
    if after_x + 1 >= N:        # 아래쪽 7% 칸 계산
        out_sum += math.floor(array[after_x+1][after_y] + (array[after_x][after_y] * 0.07))
    else:
        array[after_x+1][after_y] += array[after_x][after_y] * 0.07

    if after_x - 1 < 0 or after_y + 1 < 0:        # 위쪽 1% 칸 계산
        out_sum += math.floor(array[after_x-1][after_y+1] + (array[after_x][after_y] * 0.01))
    else:
        array[after_x-1][after_y+1] += array[after_x][after_y] * 0.01
    if after_x + 1 >= N or after_y + 1 < 0:        # 아래쪽 1% 칸 계산
        out_sum += math.floor(array[after_x+1][after_y+1] + (array[after_x][after_y] * 0.01))
    else:
        array[after_x+1][after_y+1] += array[after_x][after_y] * 0.01

    if after_y - 1 < 0:        # alpha% 칸 계산
        out_sum += math.floor(array[after_x][after_y-1] + (array[after_x][after_y] * 0.55))
    else:
        array[after_x][after_y-1] += array[after_x][after_y] * 0.55

    return out_sum

def right_move(graph, before_x, before_y, N):              #  오른쪽으로 1칸 움직이는 경우
    after_x = before_x
    after_y = before_y + 1

    array[after_x][after_y] += array[before_x][before_y]

    out_sum = 0

    if after_y + 2 >= N:          # 5% 칸 계산
        out_sum += math.floor(array[after_x][after_y+2] + (array[after_x][after_y] * 0.05))
    else:
        array[after_x][after_y+2] += array[after_x][after_y] * 0.05

    if after_x - 1 < 0 or after_y + 1 >= N:        # 위쪽 10% 칸 계산
        out_sum += math.floor(array[after_x-1][after_y+1] + (array[after_x][after_y] * 0.1))
    else:
        array[after_x-1][after_y+1] += array[after_x][after_y] * 0.1
    if after_x + 1 >= N or after_y + 1 >= N:        # 아래쪽 10% 칸 계산
        out_sum += math.floor(array[after_x+1][after_y+1] + (array[after_x][after_y] * 0.1))
    else:
        array[after_x+1][after_y+1] += array[after_x][after_y] * 0.1

    if after_x - 2 < 0:        # 위쪽 2% 칸 계산
        out_sum += math.floor(array[after_x-2][after_y] + (array[after_x][after_y] * 0.02))
    else:
        array[after_x-2][after_y] += array[after_x][after_y] * 0.02
    if after_x + 2 >= N:        # 아래쪽 2% 칸 계산
        out_sum += math.floor(array[after_x+2][after_y] + (array[after_x][after_y] * 0.02))
    else:
        array[after_x+2][after_y] += array[after_x][after_y] * 0.02

    if after_x - 1 < 0:        # 위쪽 7% 칸 계산
        out_sum += math.floor(array[after_x-1][after_y] + (array[after_x][after_y] * 0.07))
    else:
        array[after_x-1][after_y] += array[after_x][after_y] * 0.07
    if after_x + 1 >= N:        # 아래쪽 7% 칸 계산
        out_sum += math.floor(array[after_x+1][after_y] + (array[after_x][after_y] * 0.07))
    else:
        array[after_x+1][after_y] += array[after_x][after_y] * 0.07

    if after_x - 1 < 0 or after_y - 1 < 0:        # 위쪽 1% 칸 계산
        out_sum += math.floor(array[after_x-1][after_y-1] + (array[after_x][after_y] * 0.01))
    else:
        array[after_x-1][after_y-1] += array[after_x][after_y] * 0.01
    if after_x + 1 >= N or after_y - 1 < 0:        # 아래쪽 1% 칸 계산
        out_sum += math.floor(array[after_x+1][after_y-1] + (array[after_x][after_y] * 0.01))
    else:
        array[after_x+1][after_y-1] += array[after_x][after_y] * 0.01

    if after_y + 1 >= N:        # alpha% 칸 계산
        out_sum += math.floor(array[after_x][after_y+1] + (array[after_x][after_y] * 0.55))
    else:
        array[after_x][after_y+1] += array[after_x][after_y] * 0.55

    return out_sum

def up_move(graph, before_x, before_y, N):              #  위쪽으로 1칸 움직이는 경우 -- 미완
    after_x = before_x - 1
    after_y = before_y

    array[after_x][after_y] += array[before_x][before_y]

    out_sum = 0

    if after_x - 2 < 0:          # 5% 칸 계산
        out_sum += math.floor(array[after_x][after_y+2] + (array[after_x][after_y] * 0.05))
    else:
        array[after_x][after_y+2] += array[after_x][after_y] * 0.05

    if after_x - 1 < 0 or after_y + 1 >= N:        # 위쪽 10% 칸 계산
        out_sum += math.floor(array[after_x-1][after_y+1] + (array[after_x][after_y] * 0.1))
    else:
        array[after_x-1][after_y+1] += array[after_x][after_y] * 0.1
    if after_x + 1 >= N or after_y + 1 >= N:        # 아래쪽 10% 칸 계산
        out_sum += math.floor(array[after_x+1][after_y+1] + (array[after_x][after_y] * 0.1))
    else:
        array[after_x+1][after_y+1] += array[after_x][after_y] * 0.1

    if after_x - 2 < 0:        # 위쪽 2% 칸 계산
        out_sum += math.floor(array[after_x-2][after_y] + (array[after_x][after_y] * 0.02))
    else:
        array[after_x-2][after_y] += array[after_x][after_y] * 0.02
    if after_x + 2 >= N:        # 아래쪽 2% 칸 계산
        out_sum += math.floor(array[after_x+2][after_y] + (array[after_x][after_y] * 0.02))
    else:
        array[after_x+2][after_y] += array[after_x][after_y] * 0.02

    if after_x - 1 < 0:        # 위쪽 7% 칸 계산
        out_sum += math.floor(array[after_x-1][after_y] + (array[after_x][after_y] * 0.07))
    else:
        array[after_x-1][after_y] += array[after_x][after_y] * 0.07
    if after_x + 1 >= N:        # 아래쪽 7% 칸 계산
        out_sum += math.floor(array[after_x+1][after_y] + (array[after_x][after_y] * 0.07))
    else:
        array[after_x+1][after_y] += array[after_x][after_y] * 0.07

    if after_x - 1 < 0 or after_y - 1 < 0:        # 위쪽 1% 칸 계산
        out_sum += math.floor(array[after_x-1][after_y-1] + (array[after_x][after_y] * 0.01))
    else:
        array[after_x-1][after_y-1] += array[after_x][after_y] * 0.01
    if after_x + 1 >= N or after_y - 1 < 0:        # 아래쪽 1% 칸 계산
        out_sum += math.floor(array[after_x+1][after_y-1] + (array[after_x][after_y] * 0.01))
    else:
        array[after_x+1][after_y-1] += array[after_x][after_y] * 0.01

    if after_y + 1 >= N:        # alpha% 칸 계산
        out_sum += math.floor(array[after_x][after_y+1] + (array[after_x][after_y] * 0.55))
    else:
        array[after_x][after_y+1] += array[after_x][after_y] * 0.55

    return out_sum