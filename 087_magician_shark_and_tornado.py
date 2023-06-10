## 문제 087. 마법사 상어와 토네이도 --- 백준 No.20057 연습 문제

import copy
import sys
input = sys.stdin.readline

N = int(input())
row = col = N // 2

array = []
for _ in range(N):
    array.append(list(map(int, input().split())))


def coord_check(A, B, N):
    if 0 <= A < N and 0 <= B < N:
        return True
    else:
        return False


def left_move(array, x, y, N):      # Left Move시 계산되는 모래의 양
    crit_sand = array[x][y]
    per5, per10, per7, per2, per1 = int(crit_sand*0.05), int(crit_sand*0.1), int(crit_sand*0.07), int(crit_sand*0.02), int(crit_sand*0.01)
    rest_sand = crit_sand - (per5+(2*per10)+(2*per7)+(2*per2)+(2*per1))
    delete_sand = 0

    if coord_check(x, y-1, N): array[x][y-1] += rest_sand       # ① alpha 좌표에 들어가는 모래의 양
    else: delete_sand += rest_sand

    if coord_check(x, y-2, N): array[x][y-2] += per5            # ② 5% 좌표에 들어가는 모래의 양
    else: delete_sand += per5

    if coord_check(x-1, y-1, N): array[x-1][y-1] += per10       # ③ 10% 좌표에 들어가는 모래의 양
    else: delete_sand += per10
    if coord_check(x+1, y-1, N): array[x+1][y-1] += per10
    else: delete_sand += per10

    if coord_check(x-1, y, N): array[x-1][y] += per7            # ④ 7% 좌표에 들어가는 모래의 양
    else: delete_sand += per7
    if coord_check(x+1, y, N): array[x+1][y] += per7
    else: delete_sand += per7

    if coord_check(x-2, y, N): array[x-2][y] += per2            # ⑤ 2% 좌표에 들어가는 모래의 양
    else: delete_sand += per2
    if coord_check(x+2, y, N): array[x+2][y] += per2
    else: delete_sand += per2

    if coord_check(x-1, y+1, N): array[x-1][y+1] += per1        # ⑥ 1% 좌표에 들어가는 모래의 양
    else: delete_sand += per1
    if coord_check(x+1, y+1, N): array[x+1][y+1] += per1
    else: delete_sand += per1

    array[x][y] = 0
    return array, delete_sand


def up_move(array, x, y, N):      # Up Move시 계산되는 모래의 양
    crit_sand = array[x][y]
    per5, per10, per7, per2, per1 = int(crit_sand*0.05), int(crit_sand*0.1), int(crit_sand*0.07), int(crit_sand*0.02), int(crit_sand*0.01)
    rest_sand = crit_sand - (per5+(2*per10)+(2*per7)+(2*per2)+(2*per1))
    delete_sand = 0

    if coord_check(x-1, y, N): array[x-1][y] += rest_sand       # ① alpha 좌표에 들어가는 모래의 양
    else: delete_sand += rest_sand

    if coord_check(x-2, y, N): array[x-2][y] += per5            # ② 5% 좌표에 들어가는 모래의 양
    else: delete_sand += per5

    if coord_check(x-1, y-1, N): array[x-1][y-1] += per10       # ③ 10% 좌표에 들어가는 모래의 양
    else: delete_sand += per10
    if coord_check(x-1, y+1, N): array[x-1][y+1] += per10
    else: delete_sand += per10

    if coord_check(x, y-1, N): array[x][y-1] += per7            # ④ 7% 좌표에 들어가는 모래의 양
    else: delete_sand += per7
    if coord_check(x, y+1, N): array[x][y+1] += per7
    else: delete_sand += per7

    if coord_check(x, y-2, N): array[x][y-2] += per2            # ⑤ 2% 좌표에 들어가는 모래의 양
    else: delete_sand += per2
    if coord_check(x, y+2, N): array[x][y+2] += per2
    else: delete_sand += per2

    if coord_check(x+1, y-1, N): array[x+1][y-1] += per1        # ⑥ 1% 좌표에 들어가는 모래의 양
    else: delete_sand += per1
    if coord_check(x+1, y+1, N): array[x+1][y+1] += per1
    else: delete_sand += per1

    array[x][y] = 0
    return array, delete_sand


def down_move(array, x, y, N):      # Down Move시 계산되는 모래의 양
    crit_sand = array[x][y]
    per5, per10, per7, per2, per1 = int(crit_sand*0.05), int(crit_sand*0.1), int(crit_sand*0.07), int(crit_sand*0.02), int(crit_sand*0.01)
    rest_sand = crit_sand - (per5+(2*per10)+(2*per7)+(2*per2)+(2*per1))
    delete_sand = 0

    if coord_check(x+1, y, N): array[x+1][y] += rest_sand       # ① alpha 좌표에 들어가는 모래의 양
    else: delete_sand += rest_sand

    if coord_check(x+2, y, N): array[x+2][y] += per5            # ② 5% 좌표에 들어가는 모래의 양
    else: delete_sand += per5

    if coord_check(x+1, y-1, N): array[x+1][y-1] += per10       # ③ 10% 좌표에 들어가는 모래의 양
    else: delete_sand += per10
    if coord_check(x+1, y+1, N): array[x+1][y+1] += per10
    else: delete_sand += per10

    if coord_check(x, y-1, N): array[x][y-1] += per7            # ④ 7% 좌표에 들어가는 모래의 양
    else: delete_sand += per7
    if coord_check(x, y+1, N): array[x][y+1] += per7
    else: delete_sand += per7

    if coord_check(x, y-2, N): array[x][y-2] += per2            # ⑤ 2% 좌표에 들어가는 모래의 양
    else: delete_sand += per2
    if coord_check(x, y+2, N): array[x][y+2] += per2
    else: delete_sand += per2

    if coord_check(x-1, y-1, N): array[x-1][y-1] += per1        # ⑥ 1% 좌표에 들어가는 모래의 양
    else: delete_sand += per1
    if coord_check(x-1, y+1, N): array[x-1][y+1] += per1
    else: delete_sand += per1

    array[x][y] = 0
    return array, delete_sand


def right_move(array, x, y, N):      # Right Move시 계산되는 모래의 양
    crit_sand = array[x][y]
    per5, per10, per7, per2, per1 = int(crit_sand*0.05), int(crit_sand*0.1), int(crit_sand*0.07), int(crit_sand*0.02), int(crit_sand*0.01)
    rest_sand = crit_sand - (per5+(2*per10)+(2*per7)+(2*per2)+(2*per1))
    delete_sand = 0

    if coord_check(x, y+1, N): array[x][y+1] += rest_sand       # ① alpha 좌표에 들어가는 모래의 양
    else: delete_sand += rest_sand

    if coord_check(x, y+2, N): array[x][y+2] += per5            # ② 5% 좌표에 들어가는 모래의 양
    else: delete_sand += per5

    if coord_check(x-1, y+1, N): array[x-1][y+1] += per10       # ③ 10% 좌표에 들어가는 모래의 양
    else: delete_sand += per10
    if coord_check(x+1, y+1, N): array[x+1][y+1] += per10
    else: delete_sand += per10

    if coord_check(x-1, y, N): array[x-1][y] += per7            # ④ 7% 좌표에 들어가는 모래의 양
    else: delete_sand += per7
    if coord_check(x+1, y, N): array[x+1][y] += per7
    else: delete_sand += per7

    if coord_check(x-2, y, N): array[x-2][y] += per2            # ⑤ 2% 좌표에 들어가는 모래의 양
    else: delete_sand += per2
    if coord_check(x+2, y, N): array[x+2][y] += per2
    else: delete_sand += per2

    if coord_check(x-1, y-1, N): array[x-1][y-1] += per1        # ⑥ 1% 좌표에 들어가는 모래의 양
    else: delete_sand += per1
    if coord_check(x+1, y-1, N): array[x+1][y-1] += per1
    else: delete_sand += per1

    array[x][y] = 0
    return array, delete_sand


def attack_tornado(array, aa, bb):
    da = [0, +1, 0, -1]      # 0(Left), 1(Down), 2(Right), 3(Up) Sequence
    db = [-1, 0, 1, 0]
    discard = 0
    
    for iter in range(1, N):
        if iter % 2 != 0:                   # iter가 홀수라면
            for a in range(iter):           # Left First * iter
                aa += da[0]
                bb += db[0]
                array, left_delete = left_move(array, aa, bb, N)
                discard += left_delete
            for b in range(iter):           # Down Second * iter
                aa += da[1]
                bb += db[1]
                array, down_delete = down_move(array, aa, bb, N)
                discard += down_delete

        else:                               # iter가 짝수라면
            if iter != N-1:                 # 마지막 Spin이 아닌 일반적인 경우에
                for c in range(iter):       # Right First * iter
                    aa += da[2]
                    bb += db[2]
                    array, right_delete = right_move(array, aa, bb, N)
                    discard += right_delete
                for d in range(iter):       # Up Second * iter
                    aa += da[3]
                    bb += db[3]
                    array, up_delete = up_move(array, aa, bb, N)
                    discard += up_delete
            else:
                for e in range(iter):       # Right First * iter
                    aa += da[2]
                    bb += db[2]
                    array, right_delete = right_move(array, aa, bb, N)
                    discard += right_delete
                for f in range(iter):       # Up Second * iter
                    aa += da[3]
                    bb += db[3]
                    array, up_delete = up_move(array, aa, bb, N)
                    discard += up_delete
                for g in range(iter):       # Left Third * iter
                    aa += da[0]
                    bb += db[0]
                    array, left_delete = left_move(array, aa, bb, N)
                    discard += left_delete

    return discard

answer = attack_tornado(array, row, col)
print(answer)