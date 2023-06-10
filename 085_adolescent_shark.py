## 문제 085. 청소년 상어 --- 백준 No.19236 연습 문제

import copy
import sys
input = sys.stdin.readline

array = [[] for _ in range(4)]
for idx in range(4):
    info = list(map(int, input().split()))
    nums = info[0::2]
    dirs = info[1::2]

    for num, dir in zip(nums, dirs):
        array[idx].append([num, dir - 1])

# 0(Up), 1(Up-Left), 2(Left), 3(Down-Left), 4(Down), 5(Down-Right), 6(Right), 7(Up-Right) Sequence
da = [-1, -1, 0, 1, 1, 1, 0, -1]
db = [0, -1, -1, -1, 0, 1, 1, 1]


def find_fish(array, fish_num):
    fish_loc = [-1, -1]
    for a in range(4):
        for b in range(4):
            if array[a][b][0] == fish_num:
                fish_loc = [a, b]
                break

    return fish_loc


def dfs(array, row, col, max_score, eat_score):
    eat_score += array[row][col][0]             # 상어가 해당 위치의 물고기 eat
    max_score = max(max_score, eat_score)       # MAX update
    array[row][col][0] = 0                      # 먹은 이후의 fish_num만 먼저 update

    for fish_num in range(1, 17):                   # 해당 fish_num의 coord 찾기
        a, b = find_fish(array, fish_num)
        if a != -1 and b != -1:                     # 이미 상어에게 먹혔다면 pass
            before_dir = array[a][b][1]
            for dir in range(8):                        # 반시계로 45-angle을 회전하며 갈 수 있는 방향 search
                after_dir = (before_dir + dir) % 8
                aa = a + da[after_dir]
                bb = b + db[after_dir]
                if (0 <= aa < 4 and 0 <= bb < 4) and (aa != row or bb != col):     # Boundary 만족 & 상어의 위치가 아니라면
                    array[a][b][1] = after_dir
                    array[a][b], array[aa][bb] = array[aa][bb], array[a][b]
                    break

    shark_dir = array[row][col][1]              # 초반에 먹고 난 이후 fish_dir로 shark_dir을 update
    for jump in range(1, 4):                    # 갈 수 있는 방향(Size-Up 고려)을 search하며
        Arow = row + da[shark_dir] * jump
        Bcol = col + db[shark_dir] * jump
        if 0 <= Arow < 4 and 0 <= Bcol < 4 and array[Arow][Bcol][0] > 0:
            max_score = dfs(copy.deepcopy(array), Arow, Bcol, max_score, eat_score)

    return max_score

answer = dfs(array, 0, 0, 0, 0)
print(answer)